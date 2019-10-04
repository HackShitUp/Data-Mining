#Josh Choi
#© Nanogram, Inc.
#10/2/19

import pandas as pd
import numpy as np
import csv
import math
import operator


# Initialized dictionary for the training and test data sets
trainingDictionary = {};
testDictionary = {};

'''
MARK: - Class Vars
'''
# Path to training set
pathToTrainingSet = 'data/spam_train.csv';
# Path to test set
pathToTestSet = 'data/spam_test.csv';

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
   
   
   
'''
MARK: - Training Set
Here, we store the training data in a dictionary to optimize for efficiency in comparison
'''
with open(pathToTrainingSet) as csv_file:
    # Initialize the csv
    csv_reader = csv.reader(csv_file);
    # Iterator (for columns)
    i = 0;
    
    # Get the total number of columns for this file
    columnCount = countTotalColumns(pathToTrainingSet)
    
    # Loop through each row
    for row in csv_reader:
        # First row only identifies the attributes (i.e., f1 ... fn), so we just log them or increment i
        if i == 0:
            # Log the attributes
#            print(f'\n\nAttributes:\n{"   ".join(row)}\n\n')
            # Update the iterator
            i += 1
        else:
        # All the other rows store the actual values so we store them in the dictionary
            # Get the ID
            id = row[0]
            # Get the values from 1 - n (values excluding the ID)
            values = row[1:columnCount]
            # Update the dictionary to reflect the values for each row in this data set
            trainingDictionary[id] = values
            # Update the iterator
            i += 1
            
    # Log the total number of rows processed
#    print(f'Training Dictionary: {trainingDictionary}')
    
    
    
'''
MARK: - Test Set
Here, we store the teset data in a dictionary to optimize for efficiency in comparison
'''
with open(pathToTestSet) as csv_file:
    # Initialize the csv
    csv_reader = csv.reader(csv_file);
    # Iterator (for columns)
    i = 0;

    # Get the total number of columns for this file
    columnCount = countTotalColumns(pathToTestSet)

    # Loop through each row
    for row in csv_reader:
        # First row only identifies the attributes (i.e., f1 ... fn), so we just log them or increment i
        if i == 0:
            # Log the attributes
#            print(f'\n\nAttributes:\n{"   ".join(row)}\n\n')
            # Update the iterator
            i += 1
        else:
        # All the other rows store the actual values so we store them in the dictionary
            # Get the ID
            id = row[0]
            # Get the values from 1 - n (values excluding the ID)
            values = row[1:columnCount]
            # Update the dictionary to reflect the values for each row in this data set
            testDictionary[id] = values
            # Update the iterator
            i += 1

    # Log the total number of rows processed
#    print(f'testDictionary Dictionary: {testDictionary}')
    
    
    
'''
Abstract: This method calculates the distance between each data set and stores them in a dictionary. The LHS stores the row's label, and the RHS stores the comparable distance between each row from the test set to the training set. In other words:
Given B (test set) and A (training set)
1. Iterate through rows B.
2. Per each row of B, get columns from each row of A and execute the euclidean distance:
               ___________________________________________________
    d(x,y) = \/ SIGMA (B1 — A1)^2 + (B2 — A2)^2 + ... (Bn - An)^2

3. Using a dictionary, we store the distance value of B (Row N) and A (Row N) and the classification label of A like so:
[
    [1 : 0.01]  --> Row 1 from B
    [1 : 0.01]  --> Row 2 from B
    [0 : 0.01]  --> Row 3 from B
    [0 : 0.01]  --> Row N from B
]
4. Then, we sort the values from least to greatest to get the "K" nearest neighbors.
5. Finally, we grab the classification labels from the "K" nearest neighbors to report its test-accuracy.
'''

# Initialized dictionary of distance values per each row from A and its 'Label' value, calculated via each row from B (e.g., {0.01: 1, 0.02: 0, 0.8 : 1}
distanceDictionary = {}


#valueOfTrainingSetAtC = 0;
#summationValue = 0;
#distance = 0;
#
## Loop through each test set and get their key/values. Here, 't' represents the integer/iterator where 'tKey' and 'tValue' represents its key/value resepctively. In otherwords, 'tKey' = ID and 'tValue' = Features (excluding the last one because that's the label)
#for t, (tKey, tValue) in enumerate(testDictionary.items()):
#
#    # Loop through each value (aka its column/feature)
#    for c in tValue:
#
#        '''
#        MARK: - Euclidean Distance
#        let a = (x1 - y1)^2 + (x2 - y2)^2 + ... + (xn - yn)^2
#        let dxy = sqrt(a)
#        '''
#        valueOfTrainingSetAtC = list(trainingDictionary)[t][c]
#
#    # Get the square root of the summation
#    distance = math.sqrt(summationValue)
#
#    print(f'Distance: {distance}')
#
#    # Reset the distance
#    distance = 0
    
        




