from srmr.srmr import srmr
from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt

def test_srmr():
    fs, s = read("test/test_preproc.wav")
    s = s/2**15
    ratio, avg_energy = srmr(s, fs)
    plt.imshow(np.flipud(avg_energy))
    plt.show()
    print("Ratio: %2.4f" % ratio)
    assert np.allclose(ratio, 5.941239326243227, rtol=1e-6, atol=1e-12)

if __name__ == '__main__':
    test_srmr()
