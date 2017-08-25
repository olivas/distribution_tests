from math import log
from scipy.special import binom
# Test from F.Porter "Testing Consistency of Two Histograms" arXiv : 0804.0380# 

def llh_value(h1, h2):
    r"""
    Compare histograms h1, h2 with the log likelihood value test.
    """
    result = 0.
    Nu = sum(h1.bin_values)
    Nv = sum(h2.bin_values)
    for u,v in zip(h1.bin_values, h2.bin_values):
        t = u + v
        term1 = log(binom(t,v))
        term2 = t*log(Nu/(Nu + Nv))
        term3 = v*log(Nv/Nu)
        result += term1 + term2 + term3
    return -result
