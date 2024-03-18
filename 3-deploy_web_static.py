#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
import os.path
from datetime import datetime
from fabric.api import env, local, put, run

env.hosts = ["104.196.168.90", "35.196.46.172"]


def create_archive_name():
    """Create a tar gzipped archive name."""
    dt = datetime.utcnow()
    return "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    )


def create_archive():
    """Create a tar gzipped archive of the directory web_static."""
    file = create_archive_name()
    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed:
        return None
    return file


def distribute_archive(archive_path):
    """Distribute an archive to a web server."""
    if not os.path.isfile(archive_path):
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
    if put(archive_path, "/tmp/{}".format(file)).failed:
        return False
    commands = [
        "rm -rf /data/web_static/releases/{}/".format(name),
        "mkdir -p /data/web_static/releases/{}/".format(name),
        "tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name),
        "rm /tmp/{}".format(file),
        "mv /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}/".format(name, name),
        "rm -rf /data/web_static/releases/{}/web_static".format(name),
        "rm -rf /data/web_static/current",
        "ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
            name
        ),
    ]
    for cmd in commands:
        if run(cmd).failed:
            return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    file = create_archive()
    if file is None:
        return False
    return distribute_archive(file)
