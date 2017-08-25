import pylab
def draw(histogram, stats = True, color = "green", ylim = None, log = False, yerr = None):
    r"""Make a matplotlib figure of `histogram`.
    Arguments:
        stats : bool
            Draw a statistics box listing NaN count, under- and overflow.
        color : matplotlib color string
            Color of the histogram area.
        ylim : None or (float, float)
            Axis limits (ymin, ymax). If None, use 0.1 margin around data.
        log : bool
            Draw the y-axis in a logarithmic scale.
        yerr : None, float, or array/list of floats
            Error bars around the histogram.
    
    r"""
    if not ylim:
        if log:
            ymin = 0.9 * min([value for value in histogram.bin_values if value > 0])
        else:
            ymin = 0.9 * min(histogram.bin_values)
        ymax = 1.1 * max(histogram.bin_values)
    else:
        ymin, ymax = ylim

    pylab.ylim(ymin, ymax)

    xmin = 0.9 * histogram.xmin
    xmax = 1.1 * histogram.xmax
    pylab.xlim(xmin, xmax)

    pylab.title(histogram.name)

    binwidth = float(histogram.xmax - histogram.xmin)/len(histogram.bin_values)

    left_edges = [xmin + binwidth*i for i in range(len(histogram.bin_values))]

    pylab.bar(left_edges, 
              histogram.bin_values, 
              width = binwidth,
              linewidth = 0, 
              align = "edge",
              color = color,
              log = log,
              yerr = yerr)

    if stats:
        stats_text = "underflow = %d \n overflow = %d \n nan_count = %d" % \
                     (histogram.underflow, histogram.overflow, histogram.nan_count)
        pylab.figtext(0.70, 0.75, stats_text, horizontalalignment = "left")
    
