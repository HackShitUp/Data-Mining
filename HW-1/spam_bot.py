#Josh Choi
#© Nanogram, Inc.
#10/2/19

import pandas as pd
import numpy as np
import csv
import math
import operator

# Get the training set
spam_train = pd.read_csv('data/spam_train.csv');
# Get the test set
spam_test = pd.read_csv('data/spam_test.csv');

'''
Open the "spam_test" csv file and read the values
'''
with open('data/spam_test.csv') as csv_file:
    # Initialize the csv
    csv_reader = csv.reader(csv_file);
    # Iterator
    i = 0;
    
    for row in csv_reader:
        if i == 0:
            # Log the attributes
            print(f'\n\nAttributes:\n{"   ".join(row)}\n\n')
            i += 1
        else:
            # Log the dataset
            print(f'{row}')
            i += 1
        
    # Log the total number of rows processed
    print(f'Processed {i} rows')



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
def getDistancePerSet(spam_test, spam_train)



        
