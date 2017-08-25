#!/usr/bin/env python3
import unittest
import numpy
from compare.compare import compare
from histogram.histogram import Histogram

# fill two histograms with gaussian data and compare them
# test normalization
# test shapes with different normalizations
# test failures (introduce bugs)

class TestNormalization(unittest.TestCase):
    def setUp(self):
        mu = 125.09
        sigma = 0.21
        self.distribution_sizes = [100000/10**n for n in range(5)]

        self.benchmark_histograms = {}
        self.test_histograms = {}
        for size in self.distribution_sizes:
            benchmark_distribution = numpy.random.normal(mu, sigma, size)            
            benchmark_histogram = Histogram(124, 126, 100, "benchmark_%d" % size)
            for m in benchmark_distribution:
                benchmark_histogram.fill(m)
            self.benchmark_histograms[benchmark_histogram.name] = benchmark_histogram
            
            test_distribution = numpy.random.normal(mu, sigma, size)
            test_histogram = Histogram(124, 126, 100, "test_%d" % size)
            for m in test_distribution:
                test_histogram.fill(m)
            self.test_histograms[test_histogram.name] = test_histogram
                
    def test_same_normalization(self):
        for name, benchmark_histogram in self.benchmark_histograms.items():
            test_histogram = self.test_histograms[name.replace("benchmark", "test")]
            compare(benchmark_histogram, test_histogram)

unittest.main()
