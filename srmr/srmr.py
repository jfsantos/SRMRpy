import numpy as np
import scipy.signal as sig
from modulation_filters import *
from gammatone.fftweight import fft_gtgram
from segmentaxis import segment_axis

def srmr(x, fs, n_cochlear_filters=23, low_freq=125, min_cf=4, max_cf=128):
    wLengthS = .256
    wIncS = .064
    mfs = 400.0
    wLength = np.ceil(wLengthS*mfs)
    wInc = np.ceil(wIncS*mfs)
    # Computing gammatone envelopes
    gt_env = fft_gtgram(x, fs, 0.010, 0.0025, n_cochlear_filters, low_freq)
    
    # Computing modulation filterbank with Q = 2 and 8 channels
    MF = modulation_filterbank(compute_modulation_cfs(min_cf, max_cf, 8), mfs, 2)

    n_frames = 1+int(np.floor((gt_env.shape[1]-wLength)/wInc))
    w = sig.hamming(wLength)

    energy = np.zeros((n_cochlear_filters, 8, n_frames))
    for i, ac_ch in enumerate(gt_env):
        mod_out = modfilt(MF, ac_ch)
        for j, mod_ch in enumerate(mod_out):
            mod_out_frame = segment_axis(mod_ch, wLength, wInc, end='pad')
            energy[i,j,:] = np.sum((w*mod_out_frame)**2)
    
    # Not using K* yet
    avg_energy = np.mean(energy, axis=2)
    return np.sum(avg_energy[:, :4])/np.sum(avg_energy[:, 4:])

if __name__ == '__main__':
    x = np.random.rand(16000)
    ratio = srmr(x, 16000)
    print("Ratio = %2.2f" % ratio)
