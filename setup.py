#!/usr/bin/env python
# Filename: setup.py
"""
The scan_engine setup script.

"""
from setuptools import setup

with open('requirements.txt') as fobj:
    requirements = [l.strip() for l in fobj.readlines()]

try:
    with open("README.md") as fh:
        long_description = fh.read()
except UnicodeDecodeError:
    long_description = "scan_engine, parameter scan creator and engine."

setup(
    name='scan_engine',
    url='',
    description='',
    long_description=long_description,
    author='Loic Coyle',
    author_email='loic.thomas.coyle@cern.ch',
    packages=['scan_engine'],
    include_package_data=True,
    platforms='any',
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    # use_scm_version={
    #     'write_to': 'scan_engine/version.txt',
    #     'tag_regex': r'^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$',
    # },
    install_requires=requirements,
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
    ],
)

__author__ = 'Loic Coyle'
