# -*- coding: utf-8 -*-
# Copyright 2014 João Felipe Santos, jfsantos@emt.inrs.ca
#
# This file is part of the SRMRpy library, and is licensed under the
# MIT license: https://github.com/jfsantos/SRMRpy/blob/master/LICENSE

from srmrpy import srmr
from scipy.io.matlab import loadmat
import numpy as np

def test_srmr():
    fs = 16000
    s = loadmat("test/test.mat")["s"][:,0]

    correct_ratios = loadmat("test/correct_ratios.mat")['correct_ratios'][0]
    ratio, avg_energy = srmr(s, fs)
    assert np.allclose(ratio, correct_ratios[1], rtol=1e-6, atol=1e-12)

    ratio_norm_fast, avg_energy_norm_fast = srmr(s, fs, fast=True, norm=True, max_cf=30)
    assert np.allclose(ratio_norm_fast, correct_ratios[2], rtol=1e-6, atol=1e-12)

    ratio_slow, avg_energy_slow = srmr(s, fs, fast=False)
    assert np.allclose(ratio_slow, correct_ratios[0], rtol=1e-6, atol=1e-12)

    ratio_norm, avg_energy_norm = srmr(s, fs, fast=False, norm=True, max_cf=30)
    assert np.allclose(ratio_norm, correct_ratios[3], rtol=1e-6, atol=1e-12)

if __name__ == '__main__':
    test_srmr()
