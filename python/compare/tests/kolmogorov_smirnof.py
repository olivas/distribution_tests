from math import sqrt, fabs, exp, log, floor, ceil
from scipy.stats import chi2
def _round_int(x):
    if x>= 0:
        return int(x + 0.5)
    else:
        return int(x - 0.5)

def _kolmogorov_prob(z):
    r"""Compute the Kolmogorov-Smirnof p-value
    based on the test-statistic z. Code rewritten from ROOT,
    TMath::KolmogorovProb, by Rene Brun.
    
    """
    u = fabs(z)
    fj= [-2, -8, -18, -32]
    w = 2.50662827
    c1 = -1.2337005501361697
    c2 = -11.103304951225528
    c3 = -30.842513753404244
    if u<0.2:
         p=1
    elif u<0.755:
        v = 1./(u*u)
        p = 1 - w*(exp(c1*v) + exp(c2*v) + exp(c3*v))/u
    elif u<6.8116:
        v = u*u
        maxj = max(1, _round_int(3./u))
        rsum = 0
        for j in range(maxj):
            rsum += (-1)**j * exp(fj[j] * v)
        p = 2*rsum
    else: 
        p=0
    return p
    
# Both of the following tests are from F.Porter
# "Testing Consistency of Two Histograms" arXiv : 0804.0380
#   Code rewritten from CERN root (by Rene Brun, 
#   adapted from orginal HBOOK routine HDIFF)
def test_kolmogorov_smirnof(h1, h2):
    r"""Perform the Kolmogorov-Smirnof test for the histograms h1, h2
    which are assumed to have the same binning. The binning needs to be small
    compared to important features of the histograms.
    Output:
        dfmax : float
            Maximum distance between the cumulative distributions.
        p_shape : float
            Kolmogorov probability computed using the maximum distance,
            algorithm as in the ROOT implementation.
        p_norm : float
            Additional p-value testing for equal normalization.
        p_combined : float
            Combining the two former p-values according to Eadie et al. 
            ""Statistical Methods in Experimental Physics", 11.6.2.
            
        """
    #  Statistical test of compatibility in shape between
    #  data1 array and data2 array, using Kolmogorov test.
    #  The returned function value is the probability of test
    #  (much less than one means NOT compatible)
    #
    #  Description of the Kolmogorov test can be seen at:
    #  www.itl.nist.gov/div898/handbook/eda/section3/eda35g.htm
    #
    #  Note: The values of PROB for binned data will be shifted 
    #  slightly higher than expected, depending on the effects 
    #  of the binning.
    #  The probability value PROB is calculated correctly
    #  provided the user is aware that:
    #     1. The value of PROB should not be expected to have exactly the correct
    #     distribution for binned data.
    #     2. The user is responsible for seeing to it that the bin widths are
    #     small compared with any physical phenomena of interest.
    #     3. The effect of binning (if any) is always to make the value of PROB
    #     slightly too big. That is, setting an acceptance criterion of (PROB>0.05
    #     will assure that at most 5% of truly compatible histograms are rejected,
    #     and usually somewhat less."
    
    # Calculate quantities derived directly from histograms
    nbins1 = len(h1.bin_values)
    sum1 = sum(h1.bin_values)
    sum2 = sum(h2.bin_values)
    w1=0 # like sum1 but taken over the bins where both h1>0 and h2>0
    w2=0 # like sum2 but taken over the bins where both h1>0 and h2>0
    for u,v in zip(h1.bin_values, h2.bin_values):
        if u > 0 and v > 0: 
            w1 += u
            w2 += v
    esum1 = sum1**2 / float(w1)
    esum2 = sum2**2 / float(w2)
    s1 = 1.0/sum1
    s2 = 1.0/sum2
    
    # Calculate Kolmogorov-Smirnof test statistic
    rsum1 = 0.
    rsum2 = 0.
    dfmax = 0.
    for u,v in zip(h1.bin_values, h2.bin_values):
        if u > 0 and v > 0: 
            rsum1 += s1*u
            rsum2 += s2*v
            dfmax = max(dfmax,fabs(rsum1-rsum2))
    z = dfmax * sqrt(esum1*esum2/(esum1+esum2))
    
    # Calculate Kolmogorov probability
    p_shape = _kolmogorov_prob(z)
    
    # Calculate normalization p-value
    # Include underflow and overflow bins
    totsum1 = sum1 + h1.nan_count + h1.underflow + h1.overflow
    totsum2 = sum2 + h2.nan_count + h2.underflow + h2.overflow
    d12 = totsum1-totsum2
    chi2a = d12*d12/(totsum1+totsum2)
    p_norm = (1-chi2.cdf(chi2a, 1))
    
    # Combine probabilities for shape and normalization
    # see Eadie et al., section 11.6.2
    if (p_shape > 0 and p_norm > 0):
        p_combined = p_shape*p_norm*(1-log(p_shape*p_norm))
    else:
        p_combined = 0
    return dfmax, p_combined, p_shape, p_norm
    
    
