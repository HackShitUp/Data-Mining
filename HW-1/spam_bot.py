#Josh Choi
#© Nanogram, Inc.
#10/2/19

import pandas as pd
import numpy as np
import csv
import math
import operator

#Get the test and training data
spam_test = pd.read_csv('data/spam_test.csv');
spam_train = pd.read_csv('data/spam_train.csv');

#log the values
print("######## Spam Test ########")
print(spam_test)
print("######## Spam Train ########")
print(spam_train)






