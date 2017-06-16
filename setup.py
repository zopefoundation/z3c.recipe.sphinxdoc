#!/usr/bin/env python
##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for z3c.recipe.sphinxdoc package
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()

setup(
    name="z3c.recipe.sphinxdoc",
    version='1.0.1.dev0',
    author='Paul Carduner, Zope Foundation and Contributors',
    author_email="zope-dev@zope.org",
    description="Use Sphinx to build documentation for zope.org.",
    long_description=(
        read(os.path.join('src','z3c','recipe','sphinxdoc','index.rst'))
        +'\n\n'+
        read('CHANGES.rst')
    ),
    keywords="buildout sphinx docs recipe",
    license="ZPL 2.1",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Framework :: Buildout',
    ],
    url='https://github.com/zopefoundation/z3c.recipe.sphinxdoc/',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['z3c','z3c.recipe'],
    install_requires=[
        'setuptools',
        'zc.buildout',
        'docutils',
        'Sphinx',
    ],
    extras_require={
        'test': [
            'zope.testrunner',
        ],
    },
    entry_points="""
    [zc.buildout]
    default = z3c.recipe.sphinxdoc:ZopeOrgSetup
    """,
    zip_safe=False,
    include_package_data=True,
)
