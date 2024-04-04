#!/usr/bin/python3
"""
Fabfile for distributing an archive to web servers.
"""
from os import path
from fabric.api import env, put, run

# Define the hosts
env.hosts = ['54.144.138.183', '54.144.19.200']


def deploy_archive(archive_path):
    """
    Distributes an archive to web servers.

    Parameters:
    archive_path (str): Path to the archive.

    Returns:
    bool: True if successful, False otherwise.
    """
    if not path.isfile(archive_path):
        return False

    filename = archive_path.split('/')[-1]
    base_name = filename.split('.')[0]

    tmp_path = f"/tmp/{filename}"
    release_path = f"/data/web_static/releases/{base_name}/"
    current_path = "/data/web_static/current"

    commands = [
        (put, archive_path, tmp_path),
        (run, f"rm -rf {release_path}"),
        (run, f"mkdir -p {release_path}"),
        (run, f"tar -xzf {tmp_path} -C {release_path}"),
        (run, f"rm {tmp_path}"),
        (run, f"mv {release_path}web_static/* {release_path}"),
        (run, f"rm -rf {release_path}web_static"),
        (run, f"rm -rf {current_path}"),
        (run, f"ln -s {release_path} {current_path}")
    ]

    for command, *args in commands:
        if command(*args).failed:
            return False

    return True
