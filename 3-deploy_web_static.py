#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
from datetime import datetime
from fabric.api import env, local, put, run
import os

env.hosts = ["54.144.138.183", "54.144.19.200"]


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    if local(f"tar -cvzf {file} web_static").failed:
        return None
    return file


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.isfile(archive_path):
        return False
    file = os.path.basename(archive_path)
    name = file.split(".")[0]

    if any([
        put(archive_path, f"/tmp/{file}").failed,
        run(f"rm -rf /data/web_static/releases/{name}/").failed,
        run(f"mkdir -p /data/web_static/releases/{name}/").failed,
        run(f"tar -xzf /tmp/{file} -C "
            f"/data/web_static/releases/{name}/").failed,
        run(f"rm /tmp/{file}").failed,
        run(f"mv /data/web_static/releases/{name}/web_static/* "
            f"/data/web_static/releases/{name}/").failed,
        run(f"rm -rf /data/web_static/releases/{name}/web_static").failed,
        run("rm -rf /data/web_static/current").failed,
        run(f"ln -s /data/web_static/releases/{name}/ "
            f"/data/web_static/current").failed
    ]):
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
