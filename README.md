[![Code Health](https://landscape.io/github/jfsantos/SRMRpy/master/landscape.svg?style=flat)](https://landscape.io/github/jfsantos/SRMRpy/master)

# SRMRpy: a Python implementation of the SRMR Toolbox

The speech-to-reverberation modulation energy ratio (SRMR) is a non-intrusive
metric for speech quality and intelligibility based on a modulation spectral
representation of the speech signal. The metric was proposed by Falk et al.
and recently updated for variability reduction and improved intelligibility
estimation both for normal hearing listeners and cochlear implant users.

This toolbox is a Python port of [SRMRToolbox](https://github.com/MuSAELab/SRMRToolbox), and includes the following implementations of the SRMR metric:

1. The original SRMR metric (used as one of the objective metrics in the [REVERB Challenge](http://reverb2014.dereverberation.com)).
2. The updated SRMR metric, incorporating updates for reduced variability.
3. A fast implementation of the original SRMR metric, using a
[gammatonegram](http://www.ee.columbia.edu/ln/rosa/matlab/gammatonegram/) to
replace the time-domain gammatone filterbank. The fast implementation can also
optionally use the updates for reduced variability.

These implementations have been shown to perform well with sampling rates of 8
and 16 kHz. They will run for other sampling rates, but a warning will be
shown as the metrics have not been tested under such conditions.

## Setup

Simply run `python setup.py install` from inside the `SRMRpy` folder to install this package and its dependencies.

## Usage

You can use SRMR as a function or with the `srmr` wrapper, which can be called from the command line. The parameters for the wrapper are the following:

```
positional arguments:
  path                  Path of the file or files to be processed. Can also be
                        a folder.

optional arguments:
  -h, --help            show this help message and exit
  -f, --fast            Use the faster version based on the gammatonegram
  -n, --norm            Use modulation spectrum energy normalization
  --ncochlearfilters N_COCHLEAR_FILTERS
                        Number of filters in the acoustic filterbank
  --mincf MIN_CF        Center frequency of the first modulation filter
  --maxcf MAX_CF        Center frequency of the last modulation filter
```

The `srmr` function accepts the same arguments, and the API is the following:

```
srmr(x, fs, n_cochlear_filters=23, low_freq=125, min_cf=4, max_cf=128, fast=True, norm=False)
```

where `x` is a Numpy array containing the signal and `fs` is an integer with the sampling rate.

## References

If you use this toolbox in your research, please cite the reference below:

_**[TASLP2010]** Tiago H. Falk, Chenxi Zheng, and Way-Yip Chan. A Non-Intrusive Quality and Intelligibility Measure of Reverberant and Dereverberated Speech, IEEE Trans Audio Speech Lang Process, Vol. 18, No. 7, pp. 1766-1774, Sept. 2010. [doi:10.1109/TASL.2010.2052247](http://dx.doi.org/10.1109/TASL.2010.2052247)_

If you use the normalized version of the metric, please cite the following reference in addition to **[TASLP2010]**:

_**[IWAENC2014]** João F. Santos, Mohammed Senoussaoui, and Tiago H. Falk. An updated objective intelligibility estimation metric for normal hearing listeners under noise and reverberation. In International Workshop on Acoustic Signal Enhancement (IWAENC). September 2014._

Likewise, if you use the CI-tailored version of the metric (with or without normalization), please cite this reference in addition to **[TASLP2010]**:

_**[TASLP2014]** João F. Santos and Tiago H. Falk. Updating the SRMR metric for improved intelligibility prediction for cochlear implant users. IEEE Transactions on Audio, Speech, and Language Processing, December 2014. [doi:10.1109/TASLP.2014.2363788](http://dx.doi.org/doi:10.1109/TASLP.2014.2363788)._
