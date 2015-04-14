# -*- coding: utf-8 -*-
# Copyright 2014 João Felipe Santos, jfsantos@emt.inrs.ca
#
# This file is part of the SRMRpy library, and is licensed under the
# MIT license: https://github.com/jfsantos/SRMRpy/blob/master/LICENSE

from srmrpy import SRMR
from scipy.io.matlab import loadmat
import numpy as np

def test_srmr():
    fs = 16000
    s = loadmat("test/test.mat")["s"][:,0]

    correct_ratios = loadmat("test/correct_ratios.mat")['correct_ratios'][0]
    srmr = SRMR(fs)
    out = srmr.predict(s, s, s)
    ratio, avg_energy = out['p']['srmr'], out['avg_energy']
    assert np.allclose(ratio, correct_ratios[1], rtol=1e-6, atol=1e-12)

def test_srmr_norm_fast():
    fs = 16000
    s = loadmat("test/test.mat")["s"][:,0]

    correct_ratios = loadmat("test/correct_ratios.mat")['correct_ratios'][0]
    srmr = SRMR(fs, fast=True, norm=True, max_cf=30)
    out = srmr.predict(s, s, s)
    ratio_norm_fast, avg_energy_norm_fast = out['p']['srmr'], \
                                          out['avg_energy']
    assert np.allclose(ratio_norm_fast, correct_ratios[2], rtol=1e-6, atol=1e-12)

def test_srmr_slow():
    fs = 16000
    s = loadmat("test/test.mat")["s"][:,0]

    correct_ratios = loadmat("test/correct_ratios.mat")['correct_ratios'][0]
    srmr = SRMR(fs, fast=False)
    out = srmr.predict(s, s, s)
    ratio_slow, avg_energy_slow = out['p']['srmr'], out['avg_energy']
    assert np.allclose(ratio_slow, correct_ratios[0], rtol=1e-6, atol=1e-12)

def test_srmr_norm():
    fs = 16000
    s = loadmat("test/test.mat")["s"][:,0]

    correct_ratios = loadmat("test/correct_ratios.mat")['correct_ratios'][0]
    srmr = SRMR(fs, fast=False, norm=True, max_cf=30)
    out = srmr.predict(s, s, s)
    ratio_norm, avg_energy_norm = out['p']['srmr'], out['avg_energy']
    assert np.allclose(ratio_norm, correct_ratios[3], rtol=1e-6, atol=1e-12)

if __name__ == '__main__':
    test_srmr()
    test_srmr_norm()
    test_srmr_norm_fast()
    test_srmr_slow()
