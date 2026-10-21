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
    if not os.path.exists(archive_path):
        return False

    try:
        filename = os.path.basename(archive_path)
        name_without_ext = os.path.splitext(filename)[0]
        releases_path = "/data/web_static/releases/{}".format(name_without_ext)

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/{}".format(filename))

        # Uncompress the archive to the release folder
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf /tmp/{} -C {}/".format(filename, releases_path))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(filename))

        # Move contents from web_static subfolder and remove it
        run("mv {}/web_static/* {}/".format(releases_path, releases_path))
        run("rm -rf {}/web_static".format(releases_path))

        # Delete the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link to the new release
        run("ln -s {} /data/web_static/current".format(releases_path))

        print("New version deployed!")
        return True
    except Exception:
        return False
