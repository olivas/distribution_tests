#!/usr/bin/env python3

# This is a binary classification problem

import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('training_data', help='CSV file with training data.')
args = parser.parse_args()

import csv
from sklearn import linear_model

test_results = list()      # Each element in this list is a list of
                           # results for the various histogram tests.

panic_dont_panic = list()  # For each test result this is the list
                           # of whether a bug was introduced or
                           # whether they're actually sampled from
                           # the same distribution or not.

with open(args.training_data) as csvfile:
     training_data = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         print(', '.join(row))

classifier = linear_model.LogisticRegression(solver='liblinear', C=1)

classifier.fit(predictors, ground_truth);

# test_results = list_of_p_values or the value of the test statistic
# then to get a result, just call classifier.predict(test_results)
# I'm assuming this'll work if the shape of the test_results is the
# same as the ground_truth elements.

