#!/usr/bin/python3
# This is a fabfile to delete out-of-date archives.
import os
from fabric.api import env, lcd, local, cd, run

# Define the hosts
env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_clean(number=0):
    """This function deletes out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = max(1, int(number))

    archives = sorted(os.listdir("versions"))
    for _ in range(number):
        if archives:
            archives.pop()
    with lcd("versions"):
        for archive in archives:
            local(f"rm ./{archive}")

    with cd("/data/web_static/releases"):
        archives = [a for a in run("ls -tr").split() if "web_static_" in a]
        for _ in range(number):
            if archives:
                archives.pop()
        for archive in archives:
            run(f"rm -rf ./{archive}")
