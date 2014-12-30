from srmr.srmr import srmr
from scipy.io.matlab import loadmat
import numpy as np
import matplotlib.pyplot as plt

def test_srmr():
    fs = 16000
    s = loadmat("test/test.mat")["s"][:,0]
    ratio, avg_energy = srmr(s, fs)
    #plt.imshow(np.flipud(avg_energy))
    #plt.show()
    print("Ratio (fast): %2.4f" % ratio)
    assert np.allclose(ratio, 6.062267651334784, rtol=1e-6, atol=1e-12)

    ratio_slow, avg_energy_slow = srmr(s, fs, fast=False)
    print("Ratio (slow): %2.4f" % ratio_slow)

if __name__ == '__main__':
    test_srmr()
