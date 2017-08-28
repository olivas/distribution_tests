from math import sqrt,log10
# Test from F.Porter "Testing Consistency of Two Histograms" arXiv : 0804.0380# 

def test_bhattacharyya_distance_measure(h1,h2):
    r"""
    Compare histograms h1, h2 with the Bhattacharyya distance measure.
    Assumes the histograms have the same binning. 
    Treating their entries vectors, normalize, and take the dot product.
    Output:
        ts : float
            The BDM.
        p  : float
            An empirically derived measure of the p-value.
    
    """
    if sum(h1.bin_values) == 0 or sum(h2.bin_values) == 0:
        return 0., 0.
    # Bhattacharyya distance measure
    terms = [u*v for u,v in zip(h1.bin_values, h2.bin_values)]
    n1 = sum(h1.bin_values)
    n2 = sum(h2.bin_values)
    p = sqrt(n1*n2) # math.sqrt casts its arguments to a float
    T = sqrt(sum(terms))/p # => this avoids an integer division bug in this line
    return T
            
