import pylab
from math import sqrt
from ..histogram.histogram import Histogram
from .draw import draw

def draw_comparisons(test_histogram, 
                     benchmark_histogram,
                     color = "green",
                     draw_ratio = False,
                     log = False):
    r"""Make a matplotlib figure of comparing test_histogram to benchmark_histogram.
        Arguments:
            draw_ratio : bool
                Draw a ratio test_histogram/benchmark_histogram in a third subplot,
                with error bars. Always linear y-scale. The histograms have to use
                the same binning!
            color : matplotlib color string
                Color of the histogram areas.
            log : bool
                Draw the y-axis in a logarithmic scale, but never for the ratio plot.

    r"""    
    pylab.subplot(221)
    draw(test_histogram, stats = False, color = color, log = log)
    pylab.title("%s - Test" % test_histogram.name)
    pylab.subplot(222)
    draw(benchmark_histogram, stats = False, color = color, log = log)
    pylab.title("%s - Benchmark" % benchmark_histogram.name)

    ratio_histogram = Histogram(test_histogram.xmin, 
                                test_histogram.xmax, 
                                len(test_histogram.bin_values),
                                test_histogram.name + "Ratio")

    if draw_ratio and sum(benchmark_histogram.bin_values) > 0:        
        for idx, bin_pairs in enumerate(zip(test_histogram.bin_values, benchmark_histogram.bin_values)):
            if bin_pairs[1] > 0 :
                ratio_histogram.bin_values[idx] = float(bin_pairs[0])/bin_pairs[1]
        pylab.subplot(223)

        yerr = [ (float(n)/m)*sqrt(1./n + 1./m) \
                 if n > 0 and m > 0 else 0.\
                 for n,m in zip(test_histogram.bin_values, benchmark_histogram.bin_values)]
                 
        ymin = 0.9 * min([value for value in ratio_histogram.bin_values if value > 0])
        ymax = 1.1 * max(ratio_histogram.bin_values)
        draw(ratio_histogram, stats = False, color = color, ylim = (ymin, ymax), yerr = yerr)
        pylab.axhline(float(sum(test_histogram.bin_values))/sum(benchmark_histogram.bin_values))
    

