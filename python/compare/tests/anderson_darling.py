from math import log
from scipy.special import binom
# Test from F.Porter "Testing Consistency of Two Histograms" arXiv : 0804.0380# 

def anderson_darling(h1, h2):
    r"""
    Compare histograms h1, h2 with the Anderson-Darling test.
    """
    result = 0.
    Nu = sum(h1.bin_values)
    Nv = sum(h2.bin_values)
    factor = 1./(Nu+Nv)
    sigma_j = 0.
    sigma_uj = 0.
    sigma_ui = 0.
    for i,u,v in enumerate(zip(h1.bin_values, h2.bin_values)):
        if u == 0 and v == 0:
            continue
        t = u + v

        sigma_j += t
        sigma_uj += u
        sigma_ui += v

        term1 = (1./Nu)*((Nu+Nv)*sigma_uj - Nu*sigma_j)**2
        term2 = (1./Nv)*((Nu+Nv)*sigma_vj - Nv*sigma_j)**2

        result += t*(term1 + term2)/(sigma_j *(Nu+Nv - sigma_j))
        
    return factor * result
