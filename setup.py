#!/usr/bin/env python
import os
from setuptools import setup
from setuptools import find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name = 'Talkmore SMS',
    version = "0.0.1",
    description = "Talkmore SMS library for Python 3",
    author = "Kristoffer Dalby",
    author_email = "kradalby@kradalby.no",
    url = "https://github.com/kradalby/talkmoresms",
    keywords = ["sms", 'talkmore'],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description='\n\n'.join([read('README.md')]),
    test_suite = 'tests',
    install_requires=['requests'],
    packages=['talkmoresms'],
)
