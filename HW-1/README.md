# Josh Choi
# Data Mining HW-1
# 10/2/19


### 1. Execute ```spam_bot.py``` using python. To manipulate the values of _k_ (which is initialized to [1, 5, 11, 21, 41, 61, 81, 101, 201, 401]). To update this value, search for the variable, *kValues*.
```
python spam_bot.py
```
The program will log the answers to the questions. Based on the machine's CPU, RAM, and processor the runtime may vary. Benchmark generally ranges between 60 to 180 seconds.

Abstract: This method calculates the distance between each data set and stores them in a dictionary. The LHS stores the row's label, and the RHS stores the comparable distance between each row from the test set to the training set. In other words: Given B (test set) and A (training set)...
```
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
```


### 1D. What can you conclude by comparing the KNN performance in (a) and (b)?
One can conclude that normalizing one's datasets optimizes their algorithm for effiency in terms of benchmarking and dimensionality reduction. When datasets scale, kNN takes longer to execute. Hypothetically, if one were given 2 datasets, A and B, both with 2 features, when plotted on an _x and y_ graph, the algorithm would execute it fairly quickly and plot its points on a 2D plane. With n features (n > 2), this gets complicated. Normalization helps with simplfying this process.


### 2. Table 1 below contains a small training set. Each line includes an individual’s education, occupation choice, years of experience, and an indication of salary. Your task is to create a complete decision tree including the number of low’s & high’s , entropy at each step and the information gain for each feature examined at each node in the tree.

```
-------------------------------------------------------------------------------------------------------------------------
|        Education Level          |                Career                |                  Years of Experience         |
-------------------------------------------------------------------------------------------------------------------------
|    Highschoool   |    College   |      Management  |       Service     |   less than 3    |       3 — 10    |    10   |
-------------------------------------------------------------------------------------------------------------------------
    Low                 High                Low                 Low             Low             Low                 Low
    Low                 Low                 Low                 Low             High            Low                 High
    Low                 High                High                High            Low             High                High
    High                High                High                Low                             Low                 Low
    Low                 Low                 High                Low             
-------------------------------------------------------------------------------------------------------------------------
```

```
         n
H(x) = - ∑ (p(x<sub>i</sub>)log<sub>2</sub>(p(x<sub>i</sub>)))
       i = 1
        6, 4, 0.97
        Education gain = 0.97 - info([4, 1], [2, 3]) = 0.97 - (1/2 * 0.86 + 1/2 * 0.99) = 0.4 <sub>bits</sub>

1. High School 4, 1, 0.86
    Experience gain = 0.86 - info([1, 0], [2, 0], [1, 1]) = 4.6 <sub>bits</sub>
    Career gain = 0.86 - info([2, 1], [2, 0]) = 0.28 <sub>bits</sub>
2. College 2, 3, 0.99
    Experience gain = 0.99 - info[1, 1], [1, 0], [1, 1]) = 0.19 <sub>bits</sub>
    Career gain = 0.99 - info ([0, 2], [2, 1]) = 0.41 <sub>bits</sub>

* Career Gain:
    0.97 - info([2, 3], [4, 1]) = 0.04 <sub>bits</sub>
* Experience Gain:
    0.97 - info([2, 1], [2, 1], [2, 2]) = -0.1 <sub>bits</sub>

MARK: - Pruning
                                        [Education Level]
                                        /               \
                                [Experience]            [Career]
                                High School              College
                                /   |    \              /      \
                            [Low] [Low] [Career]       [High]    [Experience]
                                        /       \                /     |     \
                                    [Low]       [High]       [Low]   [High]  [Low]
                                      |            |
                                    2L, 0H       0L, 2H      
* Keep: 1; Prune: 2
```
```
                                        [Education Level]
                                        /               \
                                [Experience]            [Career]
                                High School              College
                                /   |    \              /      \
                            [Low] [Low] [Career]       [High]  [Experience]
                                        /       \        |      /     |     \
                                    [Low]       [High] 0L, 2H  [Low]   [High]  [Low]
                                                                         |
                                                                        [2L, 1H]
                                                                        /   |   \
                                                                [1L, 0H] [0L, 1H] [1L, 0H]

* Keep: 1; Prune: 3
* Keep: 1; Prune: 1
```
```
MARK: - Post Pruning
                                            [Education Level]
                                            /               \
                                    [Experience]            [Career]
                                    High School              College
                                    /   |    \              /      \
                                [Low] [Low] [Career]       [High]  [Low]
                                            /       \    
                                        [Low]       [High]
                                    (Management)    (Service)
```
