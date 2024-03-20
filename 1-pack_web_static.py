#!/usr/bin/python3
# Fabfile produces a.tgz archive from the content of web_static.
from datetime import datetime
import os
from fabric.api import local


def do_pack():
    """Produce a tar gzipped archieve of the web_static dictory"""
    dt = datetime.utcnow()
    file_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                              dt.month,
                                                              dt.day,
                                                              dt.hour,
                                                              dt.minute,
                                                              dt.second)
    if not os.path.exists("versions"):
        result = local("mkdir -p versions")
        if result.failed:
            return None
    archive_cmd = "tar -cvzf {} web_static".format(file_path)
    if local(archive_cmd).failed:
        return None
    return file_path
