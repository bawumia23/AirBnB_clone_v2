#!/usr/bin/python3
"""Distributes an archive to web servers."""

import os
from fabric.api import env, put, run, settings, hide

env.hosts = ['<WEB_01_IP>', '<WEB_02_IP>']


def do_deploy(archive_path):
    """Deploy an archive to both web servers."""
    if not archive_path or not os.path.isfile(archive_path):
        return False

    filename = os.path.basename(archive_path)
    release_name = filename[:-4]
    release_path = '/data/web_static/releases/{}'.format(release_name)
    remote_archive = '/tmp/{}'.format(filename)

    try:
        with hide('running', 'stdout', 'stderr'):
            for host in env.hosts:
                with settings(host_string=host, warn_only=True):
                    put(archive_path, remote_archive)

                    result = run('mkdir -p {}'.format(release_path))
                    if result.failed:
                        return False

                    result = run(
                        'tar -xzf {} -C {}'.format(
                            remote_archive, release_path
                        )
                    )
                    if result.failed:
                        return False

                    result = run('rm -f {}'.format(remote_archive))
                    if result.failed:
                        return False

                    result = run(
                        'find {}/web_static -mindepth 1 -maxdepth 1 '
                        '-exec mv -t {} -- {{}} +'.format(
                            release_path, release_path
                        )
                    )
                    if result.failed:
                        return False

                    result = run(
                        'rm -rf {}/web_static'.format(release_path)
                    )
                    if result.failed:
                        return False

                    result = run(
                        'ln -sfn {} /data/web_static/current'.format(
                            release_path
                        )
                    )
                    if result.failed:
                        return False

        return True
    except Exception:
        return False


if __name__ == "__main__":
    print(do_deploy(""))
