```
Josh Choi
Professor Yijun Zhao
Data Mining
11/08/19
```
# HW 3
#### 1. (60 points) Feature Selection
#### You will apply filter method to perform feature selection on a variant of the UCI vehicle dataset in the file ```veh-prim.arff```. 
#### (a) Make the class lables numeric (set "noncar" = 0 and "car" = 1) and calculate the Pearson Correlation Coefficient (PCC) of each feature with the numeric class labels. The PCC value is commonly referred to as _r_. List the features from highest _|r|_ to lowest, along with their _|r|_ values.
Note: For a simple method to calculate the PCC that is both computationally efficient and numerically stable, see the pseudo code in the ```pearson.html``` file.
```
=== Run information ===

Evaluator:    weka.attributeSelection.CorrelationAttributeEval 
Search:       weka.attributeSelection.Ranker -T -1.7976931348623157E308 -N -1
Relation:     DATASET
Instances:    846
Attributes:   37
              f0
              f1
              f2
              f3
              f4
              f5
              f6
              f7
              f8
              f9
              f10
              f11
              f12
              f13
              f14
              f15
              f16
              f17
              f18
              f19
              f20
              f21
              f22
              f23
              f24
              f25
              f26
              f27
              f28
              f29
              f30
              f31
              f32
              f33
              f34
              f35
              CLASS
Evaluation mode:    evaluate on all training data



=== Attribute Selection on all input data ===

Search Method:
	Attribute ranking.

Attribute Evaluator (supervised, Class (nominal): 37 CLASS):
	Correlation Ranking Filter
Ranked attributes:
 0.4369218    5 f4
 0.368269    14 f13
 0.3682237   15 f14
 0.3660251   17 f16
 0.3521413    8 f7
 0.3513499   23 f22
 0.3410426   27 f26
 0.3088108    2 f1
 0.299049    21 f20
 0.2907829   32 f31
 0.2660928   35 f34
 0.1957324    3 f2
 0.1569043   29 f28
 0.153096    26 f25
 0.1376362   20 f19
 0.1139447   18 f17
 0.0931737   33 f32
 0.087773     9 f8
 0.0697951    1 f0
 0.0568765   11 f10
 0.0566052   22 f21
 0.0421169   12 f11
 0.0388096   34 f33
 0.0352948    7 f6
 0.0314779   16 f15
 0.0308552   36 f35
 0.0208295   30 f29
 0.0179314   19 f18
 0.0156062   28 f27
 0.0130054   10 f9
 0.0092136    4 f3
 0.0089552   31 f30
 0.0077797   25 f24
 0.0055079   24 f23
 0.0021786   13 f12
 0.0000981    6 f5

Selected attributes: 5,14,15,17,8,23,27,2,21,32,35,3,29,26,20,18,33,9,1,11,22,12,34,7,16,36,30,19,28,10,4,31,25,24,13,6 : 36
```
#### (b) Why would one be interesed in the absolute value of _r_ rather than the raw value?

The PCC (aka Pearson Correlation Coefficient, or the correlation coefficient) is is a proxy that measures the degreee of linear relationship between 2 variables (typically _x_ and _y_) where a positive (+) correlation indicates that when _x_ increases or decreases, _y_ also increases or decreases respectively, and a negative (-) correlation indicates that when _x_ decreases or increases, _y_ increases or decreases, respectively. Typically, this PCC value ranges between -1 and 1.
```
-1.00 ≤ r ≤ 1.00
```
When using the ABSOLUTE VALUE of _r_, it denotes the strength of the linear relationship. When **|r|** is closer to 0, it indicates an absence in the linear relationship x, y. When **|r|** is closer to +1 or -1, it indicates a sronger (or perfect) relationship between x, y.

#### (c) From the sorted list obtained in (a), select the top _m_ features from the list, and run your KNN algorithm on the dataset restricted to only those _m_ features. **Use LOOCV to measure the performance and fix the KNN parameter to b k = 7 for all runs of LOOCV**. Which value of _m_ gives the highest LOOCV classification accuracy, and what is the value of this optimal accuracy?
```
=== Run information ===

Scheme:       weka.classifiers.lazy.IBk -K 7 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \"weka.core.EuclideanDistance -R first-last\""
Relation:     DATASET-weka.filters.unsupervised.attribute.Remove-R6-weka.filters.unsupervised.attribute.Remove-R12-weka.filters.unsupervised.attribute.Remove-R22-weka.filters.unsupervised.attribute.Remove-R22-weka.filters.unsupervised.attribute.Remove-R27-weka.filters.unsupervised.attribute.Remove-R4-weka.filters.unsupervised.attribute.Remove-R8-weka.filters.unsupervised.attribute.Remove-R22-weka.filters.unsupervised.attribute.Remove-R15-weka.filters.unsupervised.attribute.Remove-R22-weka.filters.unsupervised.attribute.Remove-R26-weka.filters.unsupervised.attribute.Remove-R12-weka.filters.unsupervised.attribute.Remove-R5-weka.filters.unsupervised.attribute.Remove-R22-weka.filters.unsupervised.attribute.Remove-R8-weka.filters.unsupervised.attribute.Remove-R14-weka.filters.unsupervised.attribute.Remove-R7-weka.filters.unsupervised.attribute.Remove-R1-weka.filters.unsupervised.attribute.Remove-R5
Instances:    846
Attributes:   18
              f1
              f2
              f4
              f7
              f13
              f14
              f16
              f17
              f19
              f20
              f22
              f25
              f26
              f28
              f31
              f32
              f34
              CLASS
Test mode:    846-fold cross-validation

=== Classifier model (full training set) ===

IB1 instance-based classifier
using 7 nearest neighbour(s) for classification


Time taken to build model: 0 seconds

=== Stratified cross-validation ===
=== Summary ===

Correctly Classified Instances         762               90.0709 %
Incorrectly Classified Instances        84                9.9291 %
Kappa statistic                          0.8016
Mean absolute error                      0.1659
Root mean squared error                  0.2758
Relative absolute error                 33.1546 %
Root relative squared error             55.1089 %
Total Number of Instances              846     

=== Detailed Accuracy By Class ===

                 TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
                 0.872    0.070    0.928      0.872    0.899      0.803    0.963     0.961     car
                 0.930    0.128    0.876      0.930    0.902      0.803    0.963     0.945     noncar
Weighted Avg.    0.901    0.098    0.902      0.901    0.901      0.803    0.963     0.953     

=== Confusion Matrix ===

   a   b   <-- classified as
 374  55 |   a = car
  29 388 |   b = noncar
```
### 2. (40 points) Ensemble Method
#### Suppose we need to build a predictive model for a binary classification task. We have 25 students in our class. Each of us worked independently and everyone is able to build a model with 60% accuracy.
** Notes — Majority Vote Model: **
<sup>n</sup>
    ∑(n|k) p<sup>k</sup>(1 - p)<sup>n-k</sup>
<sub>k>(n/2)</sub>

#### (a) If we take 3 models and build a majority vote classifier C<sub>3</sub>, what would be the accuracy of our new classifier C<sub>3</sub>? Show your work.
Given the accuracy for each classifier is 60%;

(0.4<sup>3</sup>) + 3.0(0.4<sup>2</sup>)(0.6) + 6.0(0.4<sup>1</sup>)(0.6<sup>0</sup>)

We get an error rate ~ 2.752 ~ 275.2%

#### (b) If we take 5 models and build a majority vote classifier C<sub>5</sub>, what would be the accuracy of our new classifier C<sub>5</sub>? Show your work.
Given the accuracy for each classifier is 60%;

(0.4<sup>5</sup>) + 5(0.4<sup>4</sup>)(0.6) + 10(0.4<sup>3</sup>)(0.6<sup>2</sup>)

We get an error rate ~ 31.744%.

#### (c) If we take all 25 models and build a majority vote classifier C<sub>25</sub>, what would be the accuracy of our new classifier C<sub>25</sub>? Show your work. *You may need to write a small program to compute this).
If we take 25 models to build a majority classifier, the error rate would decrease dramatically relative to (a) and (b).

#### (d) The performance you obtained for C<sub>25</sub> is too good to be true. What's the assumption in your calculations that often does not hold in reality?

#### (e) What would be the answer to (c) if everyone's model only has 45% accuracy? Show your work.
