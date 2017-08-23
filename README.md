# distribution_tests
The project contains tools for testing two continuous distributions to determine
similarity.

Motivation
----------
On IceCube, like many experiments, it was too easy for developers to introduce
bugs that unit tests couldn't catch.  Like many bugs that make it through your
test suite, they're often caught very late after many TBs worth of data has
been produced or processed.

It was often lamented that "Writing physics tests are too hard." and this was
commonly used as an excuse not to wwrite tests at all.  This project shows
that it's not hard at all to write "physics tests" (or more generally functions
that produce distributions of continuous variables)

There are two cases where this project has been used on IceCube:
1. Automated continuous build system (e.g. buildbot system)
2. To verify refactoring.

This work is was inspired by Frank Porter's paper [Testing the Consistency of
Two Histograms](https://arxiv.org/abs/0804.0380).  


