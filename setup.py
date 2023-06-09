# -*- coding: utf-8 -*-
# Copyright 2014 João Felipe Santos, jfsantos@emt.inrs.ca
#
# This file is part of the SRMRpy library, and is licensed under the
# MIT license: https://github.com/jfsantos/SRMRpy/blob/master/LICENSE
from setuptools import setup, find_packages

setup(
    name = "SRMRpy2",
    version = "1.0",
    packages = find_packages(),

    install_requires = [
        'numpy',
        'scipy',
        'gammatone @ git+https://github.com/detly/gammatone',
    ],

    tests_require = [
      'nose'
    ],

    test_suite = 'nose.collector',

    entry_points = {
        'console_scripts': [
            'srmr = srmrpy2.srmr:main',
        ]
    }
)

