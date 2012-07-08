#!/usr/bin/env python
"""Boundary Annotations API Client."""
__author__ = 'Greg Albrecht <gba@splunk.com>'
__copyright__ = 'Copyright 2012 Splunk, Inc.'
__license__ = 'Apache License 2.0'


import os
import setuptools

import version


def read_readme():
    """Reads in README file for use in setuptools."""
    with open('README.rst') as rmf:
        rmf.read()


def read_license():
    """Reads in LICENSE file for use in setuptools."""
    with open('LICENSE') as lcf:
        lcf.read()


def write_build_env(cmd, basename, filename):
    """Writes the build environment to the specified file - A TOTAL HACK."""
    env = "\n".join(['='.join(item) for item in os.environ.items()])
    fd = open(filename, 'wb')
    fd.write(env)
    fd.close()


setuptools.setup(
    name='boundary_annotations',
    version='1.0.2a',
    description='Boundary Annotations API Client',
    long_description=read_readme(),
    author='Greg Albrecht',
    author_email='gba@splunk.com',
    url='https://github.com/ampledata/boundary-annotations-python',
    license=read_license(),
    packages=setuptools.find_packages(exclude=('tests', 'docs')),
    setup_requires=['nose'],
    tests_require=['mock', 'coverage'],
    entry_points = {
        'egg_info.writers': [
            "build_env.txt = setup:write_build_env"
        ]
    }
)
