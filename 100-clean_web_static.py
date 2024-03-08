#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives, using the function do_clean.
"""

from fabric.api import *
import os

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """

    try:
        number = int(number)
    except ValueError:
        print("Invalid number. Please provide a valid integer.")
        return

    if number < 2:
        number = 1

    with lcd('versions'):
        local('ls -t | tail -n +{} | xargs -I {{}} rm {{}}'.format(number))

    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}'.format(number))


# Check if executed as standalone script
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Fabric script to delete out-of-date archives")
    parser.add_argument("number", type=int, nargs="?", default=0,
                        help="Number of archives to keep, including the most recent. Default is 0.")
    args = parser.parse_args()

    do_clean(args.number)
