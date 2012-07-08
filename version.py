#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Calculates the current version number.  If possible, this is the
output of “git describe”, modified to conform to the versioning
scheme that setuptools uses.  If “git describe” returns an error
(most likely because we're in an unpacked copy of a release tarball,
rather than in a git working copy), then we fall back on reading the
contents of the VERSION.txt file.

To use this script, simply import it your setup.py file, and use the
results of get_version() as your package version::

    from version import *

    setup(
        version=get_version(),
        ...
    )

This will automatically update the VERSION.txt file, if
necessary.  Note that the VERSION.txt file should *not* be
checked into git; please add it to your top-level .gitignore file.

You'll probably want to distribute the VERSION.txt file in your
sdist tarballs; to do this, just create a MANIFEST.in file that
contains the following line::

  include VERSION.txt

Derived from http://dcreager.net/2010/02/10/setuptools-git-version-numbers/

"""
__author__ = 'Douglas Creager <dcreager@dcreager.net>'
__copyright__ = 'This file is placed into the public domain.'
__all__ = ('get_version')


import os

from subprocess import Popen, PIPE


VERSION_FILE = 'VERSION.txt'
RELEASE_VERSION_FILE = 'RELEASE-VERSION.txt'


def _call_git_describe():
    try:
        git_cmd = ['git', 'describe', '--contains', '--all', 'HEAD']
        git_describe = Popen(git_cmd, stdout=PIPE, stderr=PIPE)
        git_describe.stderr.close()
        line = git_describe.stdout.readlines()[0]
        return line.strip()
    except:
        return None


def _read_version_file(version_file):
    try:
        vfile = open(version_file, 'r')
        try:
            version = vfile.readlines()[0]
            return version.strip()
        finally:
            vfile.close()
    except:
        return None


def _write_release_version(version):
    release_file = open(RELEASE_VERSION_FILE, 'w')
    release_file.write("%s\n" % version)
    release_file.close()


def get_version():
    build_number = os.environ.get('BUILD_NUMBER')
    git_branch = _call_git_describe()

    version = _read_version_file(VERSION_FILE)
    release_version = _read_version_file(RELEASE_VERSION_FILE)

    if release_version is not None:
        if git_branch is None:
            # We're probably a released version since there's no git branch.
            return release_version

    if build_number is not None:
        version = '.'.join([version, build_number])

    if git_branch is not None:
        branch = git_branch.split('/')[-1]
        version = '-'.join([version, branch])

    _write_release_version(version)
    return version


if __name__ == '__main__':
    print get_version()
