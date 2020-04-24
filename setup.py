#!/usr/bin/env python
# Filename: setup.py
"""
The scan_engine setup script.

"""
from setuptools import setup

with open('requirements.txt') as fobj:
    REQUIREMENTS = [l.strip() for l in fobj.readlines()]

with open("README.md") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name='scan_engine',
    url='https://github.com/loiccoyle/scan_engine',
    description='Parameter scan engine.',
    long_description=LONG_DESCRIPTION,
    author='Loic Coyle',
    author_email='loic.thomas.coyle@cern.ch',
    packages=['scan_engine'],
    platforms='any',
    install_requires=REQUIREMENTS,
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
    ],
)
