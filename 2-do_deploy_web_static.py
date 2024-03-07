#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy.
"""

from fabric.api import *
import os.path

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """

    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        filename = archive_path.split('/')[-1]
        folder_name = filename.replace('.tgz', '')

        run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.
            format(filename, folder_name))
        run('rm /tmp/{}'.format(filename))
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.
            format(folder_name, folder_name))
        run('rm -rf /data/web_static/releases/{}/web_static'.
            format(folder_name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.
            format(folder_name))
        print("New version deployed!")
        return True
    except:
        return False
