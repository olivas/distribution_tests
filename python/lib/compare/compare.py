from .tests.norm_chisq import test_norm_chisq
from .tests.shape_chisq import test_shape_chisq
from .tests.bdm import test_bhattacharyya_distance_measure
from .tests.kolmogorov_smirnof import test_kolmogorov_smirnof

def _comparable(h1, h2):
    '''
    Returns True if two histograms are comparable,
    meaning they have the same name and binning.
    
    '''
    return ((h1.xmin == h2.xmin) and\
       (h1.xmax == h2.xmax) and\
       (h1.name == h2.name) and\
       (len(h1.bin_values) == len(h2.bin_values)))

def compare(hist1, hist2,
            test_norm = True, 
            test_shape = True, 
            test_bdm = False,
            test_ks = True,
            # Default thresholds: confidence = 3 sigma
            # on benchmark null-hypothesis trials
            # with 100-bin histogram, within [-2., 2.]
            # containing Poisson(lambda=1000) samples from
            # normal distribution (sigma = 1, mu = 0)
            # as in resources/scripts/perform_trials.py
            norm_pval = 0.73,
            shape_pval = 1.4e-2,
            bdm_pval = 0.43,
            ks_pval = 3.8e-2,
            ks_norm_pval = 1.9e-2,
            ks_shape_pval = 2.7e-2):
    r'''For all enabled test_{name}, compare hist1 and hist2.
    Allows setting the threshold for "disagreement" with {name}_pval,
    defaults correspond to 3-sigma significance in an artificial benchmark.
    Output:
        result : dict 
            name of test module  : p-value >= threshold
            Will be empty if no tests enabled, or histograms inconsistent.
    
    '''

    if not _comparable(hist1, hist2) :
        print("ERROR : histograms are inconsistent.")
        return False

    result = {}

    if test_norm:
        T, pval = test_norm_chisq(hist1, hist2)
        result["norm_chisq"] = bool(pval >= norm_pval)
        if pval < norm_pval:
            print "norm_chisq : T, pval = ",(T,pval)

    if test_shape:
        T, pval = test_shape_chisq(hist1, hist2)
        result["shape_chisq"] = bool(pval >= shape_pval)
        if pval < shape_pval:
            print "shape_chisq : T, pval = ",(T,pval)

    if test_bdm:
        T, pval = test_bhattacharyya_distance_measure(hist1, hist2)
        result["bdm"] = bool(pval >= bdm_pval)
        if pval < bdm_pval:
            print "bdm : T, pval = ",(T,pval)
    
    if test_ks:
        maxdf, p_combined, p_shape, p_norm = test_kolmogorov_smirnof(hist1, hist2) 
        result["ks"] = bool(p_combined >= ks_pval) 
        if p_combined < ks_pval:
            print "ks: maxdf, pval = ", (maxdf, p_combined)
            print "ks: pval_shape, pval_norm", (p_shape, p_norm)
        result["ks_shape_alone"] = bool(p_shape >= ks_shape_pval) 
        result["ks_norm_alone"] = bool(p_norm >= ks_norm_pval)
        

    return result
    
    
