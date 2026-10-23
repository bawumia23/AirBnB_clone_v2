#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy.
"""
from fabric.api import put, run, env
import os

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_deploy(archive_path):
    """Distributes an archive to web servers."""
    if not archive_path or not os.path.isfile(archive_path):
        return False

    try:
        filename = os.path.basename(archive_path)
        release_name = os.path.splitext(filename)[0]
        release_path = "/data/web_static/releases/{}".format(
            release_name
        )
        archive_remote = "/tmp/{}".format(filename)
        current_link = "/data/web_static/current"

        put(archive_path, archive_remote)

        run("mkdir -p {}".format(release_path))
        run("tar -xzf {} -C {}".format(
            archive_remote, release_path
        ))
        run("rm -f {}".format(archive_remote))

        run("mv {}/web_static/* {}".format(
            release_path, release_path
        ))
        run("rm -rf {}/web_static".format(release_path))

        run("rm -rf {}".format(current_link))
        run("ln -s {} {}".format(
            release_path, current_link
        ))

        return True
    except Exception:
        return False
