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


RELEASE_VERSION_FILE = 'VERSION.txt'


def call_git_describe():
    try:
        git_cmd = ['git', 'describe', '--contains', '--all', 'HEAD']
        git_describe = Popen(git_cmd, stdout=PIPE, stderr=PIPE)
        git_describe.stderr.close()
        line = git_describe.stdout.readlines()[0]
        return line.strip()
    except:
        return None


def read_release_version():
    try:
        release_file = open(RELEASE_VERSION_FILE, 'r')
        try:
            version = release_file.readlines()[0]
            return version.strip()
        finally:
            release_file.close()
    except:
        return None


def write_release_version(version):
    release_file = open(RELEASE_VERSION_FILE, 'w')
    release_file.write("%s\n" % version)
    release_file.close()


def adapt_pep386(version):
    """Adapts git-describe version to be in line with PEP 386"""
    if version is not None and '-' in version:
        parts = version.split('-')
        parts[-2] = 'post'+parts[-2]
        version = '.'.join(parts[:-1])
        return version


def get_version():
    # Read in the version that's currently in VERSION.txt.
    release_version = read_release_version()
    git_branch = call_git_describe()
    build_number = os.environ.get('BUILD_NUMBER')

    if git_branch is not None and not 'release' in git_branch:
        _branch = git_branch.split('/')[-1]
        version = '_'.join([release_version, _branch])

    if build_number is not None:
        version = '.'.join([version, build_number])

    return version


if __name__ == '__main__':
    print get_version()
