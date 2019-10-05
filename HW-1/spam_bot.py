#Josh Choi
#© Nanogram, Inc.
#10/2/19

from collections import OrderedDict
import pandas as pd
import numpy as np
import csv
import math
import operator



'''
MARK: - Class Vars
'''
# Path to training set
pathToTrainingSet = 'data/spam_train.csv';
# Path to test set
pathToTestSet = 'data/spam_test.csv';

'''
Initialized dictionaries used to store the data set's (1) ID as its key and (2) its features and label as its value as a Float array
'''
trainingDictionary = {};
testDictionary = {};

'''
Count the total number of columns/attributes in a given CSV file.
- Parameter pathToFile: A String value representing the path to the CSV file.
'''
def countTotalColumns(pathToFile):
    i = 0
    with open(pathToFile) as csv_file:
        csv_reader = csv.reader(csv_file);
        for row in csv_reader:
            i += 1;
    return i

# Prepare to loop through each of the CSV files and extract its data
paths = [pathToTrainingSet, pathToTestSet]

# Loop through the different CSV files
for path in paths:
   with open(path) as csv_file:
    # Initialize the csv
    csv_reader = csv.reader(csv_file);
    
    # Iterator (for columns)
    i = 0;
    
    # Get the total number of columns for this file
    columnCount = countTotalColumns(path)
    
    # Loop through each row
    for row in csv_reader:
        # First row only identifies the attributes (i.e., f1 ... fn), so we just log them or increment i
        if i != 0:
            # All the other rows store the actual values so we store them in the dictionary
            # Get the ID
            id = row[0]
            # Get the values from 1 - n (values excluding the ID)
            values = list(map(float, row[1:columnCount]))
            # Update the dictionary to reflect the values for each row in this data set
            (trainingDictionary if path == pathToTrainingSet else testDictionary)[id] = values
        
        # Update the iterator
        i += 1
            


'''
Abstract: This method calculates the distance between each data set and stores them in a dictionary. The LHS stores the row's label, and the RHS stores the comparable distance between each row from the test set to the training set. In other words:
Given B (test set) and A (training set)
1. Iterate through rows B.
2. Per each row of B, get columns from each row of A and execute the euclidean distance:
               ___________________________________________________
    d(x,y) = \/ SIGMA (B1 — A1)^2 + (B2 — A2)^2 + ... (Bn - An)^2

3. Using a dictionary, we store the distance value of B (Row N) and A (Row N) and the classification label of A like so:
[
    [0.01 : 1]  --> Row 1 from B
    [0.01 : 0]  --> Row 2 from B
    [0.01 : 1]  --> Row 3 from B
    [0.01 : 0]  --> Row N from B
]
4. Then, we sort the values from least to greatest to get the "K" nearest neighbors.
5. Finally, we grab the classification labels from the "K" nearest neighbors to report its test-accuracy.
'''
# Initialized dictionary of distance values per each row from A and its 'Label' value, calculated via each row from B (e.g., {0.01: 1, 0.02: 0, 0.8 : 1}
# LHS = KEY (AKA DISTANCE)
# RHS = VALUE (AKA LABEL)
distanceDictionary = {}

# Store the calculated distance
distance = 0.0;

# Loop through each test set and get their key/values. Here, 't' represents the integer/iterator where 'tKey' and 'tValue' represents its key/value resepctively. In otherwords, 'tKey' = ID and 'tValue' = Features (aka an array excluding the last one because that's the label)
for t, (tKey, tValues) in enumerate(testDictionary.items()):

    # Loop through each training set's rows
    for tr, (trKey, trValues) in enumerate(trainingDictionary.items()):
        '''
        MARK: - Euclidean Distance
        let a = (x1 - y1)^2 + (x2 - y2)^2 + ... + (xn - yn)^2
        let dxy = sqrt(a)
        '''
        # Loop through each training/test set's columns and calculate the distance per each training set's row
        for i, value in enumerate(trValues):
            # Get the summation
            distance += (tValues[i] - value) * (tValues[i] - value)
    
        # Get the square root after getting the summation
        distance = math.sqrt(distance)
        # Store the distance in the dictionary along with its classification
        distanceDictionary[distance] = trValues[-1]
        # Log this for visual
        print(f'Distance: {distance}')
        # Reset the distance value to recalculate the distance
        distance = 0

'''
MARK: - KNN
'''

## Question (1a) — Get all the values for k in our KNN implementation
kValues = [1, 5, 11, 21, 41, 61, 81, 101, 201, 401]
# Sort the dictionaries by their keys (aka distance) from least to greatest
sortedDictionary = OrderedDict(sorted(distanceDictionary.items()))

# Initialized array of Float values representing the classification per each distance calculated from the training set
classifications = []

#for k in kValues:
#    # Loop through the sorted dictionary's key (distance) and its value (label)
#    for n, (dxy, classification) in enumerate(sortedDictionary.items()):
#        # Append the classification to the list
#        classifications.append(classification)
#
#        # If we found k...
#        if (n + 1) == k:
#            # Get the accuracy of the input
#            totalCount = len(classifications)
#            occurence = classifications.count(1)
#            print(f'Prediction: {occurence/totalCount}')


# Get knn
for n, (knn, classification) in enumerate(sortedDictionary.items()):
    # Append the classification to the list
    classifications.append(classification)
    
    if (n + 1) == k:
        break
        

# Get the accuracy of the input
totalCount = len(classifications)
occurence = classifications.count(1)

print(f'Accuracy: {occurence/totalCount}')
