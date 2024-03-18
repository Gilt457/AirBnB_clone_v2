#!/usr/bin/env python3
"""
Fabfile to generate a .tgz archive from the contents of the web_static folder.
"""
from datetime import datetime
import os
from fabric.api import local


def do_pack():
    """Generate a .tgz archive of the web_static directory."""
    dt = datetime.utcnow()
    file_name = (
        f"versions/web_static_{dt.year}{dt.month:02d}{dt.day:02d}"
        f"{dt.hour:02d}{dt.minute:02d}{dt.second:02d}.tgz"
    )

    if not os.path.exists('versions'):
        if local("mkdir -p versions").failed:
            return None

    if local(f"tar -cvzf {file_name} web_static").failed:
        return None

    return file_name
