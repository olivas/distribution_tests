# distribution_tests
The project contains tools for testing two continuous distributions to determine
similarity.

# Introduction

The overall goal of this project is to provide tools to detect change (when no
change was intended) that affects your favorite continuous distribution as early
as possible.

On IceCube, like many experiments, it was too easy for developers to introduce
bugs that unit tests couldn't catch.  Like many bugs that make it through your
test suite, they're often caught very late after processing (or simulating)
many TBs worth of data.  This also wastes countless grad-student and postdoc
hours.

It was often lamented that "Writing physics tests are too hard..." and this was
commonly used as an excuse not to wwrite tests at all.  This project shows
that it's not hard at all to write "physics tests" (or more generally tests of
functions that produce distributions of continuous variables).

There are two cases where this project has been used on IceCube:
1. Automated continuous build system
2. Refactoring

This work was inspired by Frank Porter's paper [Testing the Consistency of
Two Histograms](https://arxiv.org/abs/0804.0380).  The two histograms
considered throughout this project are *benchmark* and *test* histograms.

Benchmark histograms are generated first and the test histograms will be
compared to these continually.  Benchmark histograms, ideally, will be
updated rarely, only when a change was made where the change in the
distribution was expected and desired.

# Dependencies

* Python 3 - numpy, scipy, matplotlib
* optional: cmake and C++11

# Quick Tutorial

To get started you first need to generate a set of benchmark histograms.

# Tests

For comparing two histograms the following tests are provided.

## Tests for Normalization

* Chi2

## Tests for Shape

* Chi2 
* Likelihood Ratio
* Likelihood Value
* Kolmogorov-Smirnov
* Bhattacharyya Distance Measure
* Cramer-von-Mises
* Anderson-Darling

# Future Plans
The next step for this project is to provide tools to train higher level
structures, like BDTs, neural nets, or Bayesian networks, to help users
filter out false positives.

# Contributors
* Alex Olivas - University of Maryland (UMD)
* Christoph Raab - Technical University of Munich (TUM)
* Thomas Stuttard - Neils Bohr Institute (NBI)
* Tomasz Palczewski - University of California at Berkeley (Cal)