#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using do_pack.
"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """Generates a .tgz archive from the web_static folder."""
    try:
        if not os.path.exists("versions"):
            local("mkdir -p versions")

        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)

        print("Packing web_static to {}".format(archive_path))
        result = local("tar -cvzf {} web_static".format(archive_path))

        if result.succeeded:
            return archive_path
        else:
            return None
    except Exception:
        return None
