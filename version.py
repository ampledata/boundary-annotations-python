#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generates a version string for this distribution.

The version string returned depends on several factors:

    1. If we're operating within a non-release git branch, include the branch.
    2. If we're operating within CI, include the build number.
    3. Otherwise return the version string in VERSION.txt

To use this script, simply import it your setup.py file, and use the
results of get_version() as your package version::

    import version

    setup(
        version=version.get_version(),
        ...
    )

This will automatically update the RELEASE-VERSION.txt file, if
necessary.
    * Note: RELEASE-VERSION.txt file should *not* be checked into git;
    please add it to your top-level .gitignore file.

You'll probably want to distribute the RELEASE-VERSION.txt file in your
sdist tarballs; to do this, just create a MANIFEST.in file that
contains the following line::

  include RELEASE-VERSION.txt

Derived from http://dcreager.net/2010/02/10/setuptools-git-version-numbers/
"""
__author__ = ' & '.join([
    'Douglas Creager <dcreager@dcreager.net>',
    'Greg Albrecht <gba@splunk.com>'])
__copyright__ = 'Apache License 2.0'
__all__ = ('get_version')


import os
import subprocess


VERSION_FILE = 'VERSION.txt'
RELEASE_VERSION_FILE = 'RELEASE-VERSION.txt'


def _call_git_describe():
    """Calls 'git describe' to retrieve the current branch.

    @return: Git Branch.
    @rtype: str
    """
    try:
        git_cmd = ['git', 'describe', '--contains', '--all', 'HEAD']
        git_describe = subprocess.Popen(
            git_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        git_describe.stderr.close()
        line = git_describe.stdout.readlines()[0]
        return line.strip()
    except (OSError, IndexError):
        return None


def _read_version_file(version_file):
    """Reads version string from version file.

    @param version_file: Version file to read.
    @type version_file: str

    @return: Version String.
    @rtype: str
    """
    try:
        vfile = open(version_file, 'r')
        try:
            version = vfile.readlines()[0]
            return version.strip()
        finally:
            vfile.close()
    except IOError:
        return None


def _write_release_version(version):
    """Writes RELEASE_VERSION_FILE containing generated version string."""
    release_file = open(RELEASE_VERSION_FILE, 'w')
    release_file.write(''.join([version, "\n"]))
    release_file.close()


def get_version():
    """Gets version information about this distribution.

    Parses some env variables, git branch, and ci build number to generate
    unique version strings.

    @return: Version String.
    @rtype: str
    """
    build_number = os.environ.get('BUILD_NUMBER')
    git_branch = _call_git_describe()

    version = _read_version_file(VERSION_FILE)
    release_version = _read_version_file(RELEASE_VERSION_FILE)

    # We're probably a released version since there's no git branch.
    if (release_version is not None and git_branch is None):
        return release_version

    # Append build number if we're running under CI.
    if build_number is not None:
        version = '.'.join([version, build_number])

    # Append git branch if we're building in a dev env.
    if git_branch is not None:
        branch = git_branch.split('/')[-1]
        version = '-'.join([version, branch])

    # Write out release version file if we're building a distribution.
    _write_release_version(version)

    return version


if __name__ == '__main__':
    print get_version()
