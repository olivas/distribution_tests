from math import log
# Test from F.Porter "Testing Consistency of Two Histograms" arXiv : 0804.0380# 

def llh_ratio(h1, h2):
    r"""
    Compare histograms h1, h2 with the log likelihood ratio test.
    """
    result = 0.
    Nu = sum(h1.bin_values)
    Nv = sum(h2.bin_values)
    for u,v in zip(h1.bin_values, h2.bin_values):
        t = u + v
        if u == 0 and v == 0:
            result += 1
            continue
        if u == 0:
            result += t*log(Nu/(Nu+Nv))
            continue        
        if v == 0:
            result += t*log(Nv/(Nu+Nv))
            continue
        term1 = t*log((1+v/u)/(1+Nv/Nu))
        term2 = v*log((Nv/Nu)*(u/v))
        result += term1 + term2
    return -2*result
