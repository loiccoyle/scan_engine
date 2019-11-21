#!/usr/bin/env python
# Filename: setup.py
"""
The scan_engine setup script.

"""
from setuptools import setup

with open('requirements.txt') as fobj:
    REQUIREMENTS = [l.strip() for l in fobj.readlines()]

try:
    with open("README.md") as fh:
        LONG_DESCRIPTION = fh.read()
except UnicodeDecodeError:
    LONG_DESCRIPTION = "scan_engine, parameter scan creator and engine."

setup(
    name='scan_engine',
    url='',
    description='',
    long_description=LONG_DESCRIPTION,
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
    install_requires=REQUIREMENTS,
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
    ],
)

__author__ = 'Loic Coyle'
