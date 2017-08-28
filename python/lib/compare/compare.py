from .tests import norm_chisq 
from .tests import shape_chisq
from .tests import bdm 
from .tests import kolmogorov_smirnof 
from .tests import llh_ratio 
from .tests import llh_value 
from .tests import cramer_von_mises
from .tests import anderson_darling

def _comparable(h1, h2):
    '''
    Returns True if two histograms are comparable,
    meaning they have the same name and binning.    
    '''
    return ((h1.xmin == h2.xmin) and\
       (h1.xmax == h2.xmax) and\
       (len(h1.bin_values) == len(h2.bin_values)))

def compare(hist1, hist2,
            test_norm_chisq = True, 
            test_shape_chisq = True, 
            test_bdm = False,
            test_ks = True,
            test_llh_ratio = True,
            test_llh_value = True,
            test_cramer_von_mises = True,
            test_anderson_darling = True):
    r'''For all enabled test_{name}, compare hist1 and hist2.
    Output:
        result : dict 
            test name : value of test statistic 
            Will be empty if no tests enabled, or histograms inconsistent.    
    '''

    result = {}
    if not _comparable(hist1, hist2) :
        print("ERROR : histograms %s and %s are inconsistent." % (hist1.name, hist2.name))
        return result
    
    if test_norm_chisq:
        result["norm_chisq"] = norm_chisq.test_norm_chisq(hist1, hist2)

    if test_shape_chisq:
        result["shape_chisq"] = shape_chisq.test_shape_chisq(hist1, hist2)

    if test_llh_ratio:
        result["llh_ratio"] = llh_ratio.test_llh_ratio(hist1, hist2)

    if test_llh_value:
        result["llh_value"] = llh_value.test_llh_value(hist1, hist2)

    if test_cramer_von_mises:
        result["cramer_von_mises"] = cramer_von_mises.test_cramer_von_mises(hist1, hist2)

    if test_anderson_darling:
        result["anderson_darling"] = anderson_darling.test_anderson_darling(hist1, hist2)

    if test_bdm:
        result["bdm"] = bdm.test_bhattacharyya_distance_measure(hist1, hist2)
    
    if test_ks:
        result["ks"] = kolmogorov_smirnof.test_kolmogorov_smirnof(hist1, hist2)

    return result
    
    
