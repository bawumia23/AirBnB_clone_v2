#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers,
using the function deploy.
"""
from fabric.api import env
from importlib import import_module

do_pack = import_module('1-pack_web_static').do_pack
do_deploy = import_module('2-do_deploy_web_static').do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']


def deploy():
    """Creates and distributes an archive to web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
