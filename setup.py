# -*- coding: utf-8 -*-
# Copyright 2014 João Felipe Santos, jfsantos@emt.inrs.ca
#
# This file is part of the SRMRpy library, and is licensed under the
# MIT license: https://github.com/jfsantos/SRMRpy/blob/master/LICENSE
from setuptools import setup, find_packages

setup(
    name = "SRMRpy",
    version = "1.0.0",
    packages = find_packages(),

    install_requires = [
        'numpy',
        'scipy',
        'Gammatone @ https://github.com/detly/gammatone/archive/master.zip#egg=Gammatone',
    ],

    tests_require = [
      'nose'
    ],

    test_suite = 'nose.collector',

    entry_points = {
        'console_scripts': [
            'srmr = srmrpy.srmr:main',
        ]
    }
)

