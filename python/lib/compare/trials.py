from ..compare_histograms import tests
import tests.bdm, tests.kolmogorov_smirnof, tests.norm_chisq, tests.shape_chisq
from icecube.production_histograms.histogram_modules.histogram_module import Histogram
from scipy.stats import poisson, norm
import numpy as np
import matplotlib.pyplot as plt

_default_histogram = {\
            'xmin':-2,
            'xmax':2,
            'nbins':100,
            'name':'h',
            }
def make_random_histo(n,**kwargs):
    r"""Create a histogram with binning according to parameters in `kwargs`,
    fill it with `n` samples of a normal distribution.
    
    """
    for key,val in _default_histogram.items():
        kwargs.setdefault(key,val)
    h = Histogram(**kwargs)
    for x in np.random.normal(size=n):
        h.fill(x)
    return h
    
def make_flat_histo(n, **kwargs):
    r"""Create a histogram with binning according to parameters in `kwargs`,
    fill it with `n` samples of a flat distribution within the histogram range.
    
    """
    for key,val in _default_histogram.items():
        kwargs.setdefault(key,val)
    h = Histogram(**kwargs)
    for x in np.random.uniform(low=kwargs['xmin'], high=kwargs['xmax'], size=n):
        h.fill(x)
    return h
        
def trials_null(mu, n_hist,test_function,histogram_parameters=_default_histogram): 
    r"""Perform `n_hist` trials of the null hypothesis, comparing histograms with a
    number of entries sampled from a Poissonian(`mu`) using `test_function`.
    
    """
    bm = make_random_histo(mu,**histogram_parameters)
    test_results = []
    for i in range(n_hist):
        th = make_random_histo(poisson.rvs(mu),**histogram_parameters)
        test_results.append(test_function(bm,th))
    return test_results
    
def test_all_functions(mu,n_iter=1000):
    r"""Find test_ functions and pass it to `trials_null`.
    
    """
    namespace = tests
    trials = {}
    for module_name in dir(namespace):
        if module_name.startswith('_'):
            continue
        module = getattr(namespace,module_name)
        for function_name in dir(module):
            if function_name.startswith('_'):
                continue        
            function = getattr(module,function_name)
            if not hasattr(function,'func_name'):
                continue
            if function_name.startswith('test_'):
                trials[module_name] = trials_null(mu,n_iter, function)
                # Only test first matching function, so break now
                break
    if not trials:
        print('Found no histogram test functions!')
    return trials
    
def analyze_trials(trials_dict):
    r"""Analyze the output of `test_all_functions`, print results.
    
    """
    alpha_3sig = norm.cdf(-3.)
    for t_name, trials in trials_dict.items():
        p = zip(*trials)[1]
        p_3sig = np.percentile(p, 100 * alpha_3sig)
        print('%s:\t 3 sigma significance at %.2e'%(t_name, p_3sig))
        
def plot_trials(trials_dict):
    r"""Plot histogram of p-values in `trials_dict`
    as returned by `test_all_functions`.
    
    """
    for k,t in trials_dict.items():
        plt.hist(zip(*t)[1],bins=100,label=k,histtype='step')
    plt.legend()
    plt.xlabel('p')
    plt.ylabel('trials')
    plt.show()
