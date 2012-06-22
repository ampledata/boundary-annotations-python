#!/usr/bin/env python
"""Boundary Annotations API Client."""
__author__ = 'Greg Albrecht <gba@splunk.com>'
__copyright__ = 'Copyright 2012 Splunk, Inc.'
__license__ = 'Apache License 2.0'


from setuptools import setup, find_packages


def read_readme():
    """Reads in README file for use in setuptools."""
    with open('README.rst') as rmf:
        rmf.read()


def read_license():
    """Reads in LICENSE file for use in setuptools."""
    with open('LICENSE') as lcf:
        lcf.read()


setup(
    name='boundary_annotations',
    version='1.0.1',
    description='Boundary Annotations API Client',
    long_description=read_readme(),
    author='Greg Albrecht',
    author_email='gba@splunk.com',
    url='https://github.com/ampledata/boundary-annotations-python',
    license=read_license(),
    packages=find_packages(exclude=('tests', 'docs')),
    setup_requires=['nose', 'mock']
)
