#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


VERSION = '0.0.2'

setup(
    name='cc-onepassword',  # package name
    version=VERSION,  # package version
    description='my onepassword package',  # package description
    packages=find_packages(),
    url="https://github.com/houm01/cc-onepassword",
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown'
)

