#!/usr/bin/python3
"""Generates a .tgz archive from the web_static folder."""

from datetime import datetime
import os
from fabric.api import local


def do_pack():
    """Generate a .tgz archive and return its path, or None on failure."""
    try:
        if not os.path.isdir("web_static"):
            return None

        if not os.path.isdir("versions"):
            os.makedirs("versions")

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)

        result = local(
            "tar -czvf {} web_static".format(archive_path),
            capture=True
        )

        if result.failed:
            return None

        return archive_path
    except (OSError, IOError):
        return None


if __name__ == "__main__":
    print(do_pack())
