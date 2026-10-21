#!/usr/bin/python3
"""Creates and distributes an archive to web servers."""

import importlib.util


def load_module(name, path):
    """Load a Python module from a file path."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pack_module = load_module("pack", "1-pack_web_static.py")
deploy_module = load_module("deploy", "2-do_deploy_web_static.py")


def deploy():
    """Create an archive and deploy it to web servers."""
    archive_path = pack_module.do_pack()
    if not archive_path:
        return False

    return deploy_module.do_deploy(archive_path)


if __name__ == "__main__":
    print(deploy())
