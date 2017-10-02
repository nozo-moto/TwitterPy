#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from TwitterPy import __author__, __version__, __license__
 
setup(
        name             = 'TwitterPy',
        version          = __version__,
        description      = 'twitter library for python',
        license          = __license__,
        author           = __author__,
        author_email     = 'junion@junion.org',
        url              = 'https://github.com/nozomi0966/TwitterPy.git',
        keywords         = 'twitter python',
        packages         = find_packages(),
        install_requires = [],
        )