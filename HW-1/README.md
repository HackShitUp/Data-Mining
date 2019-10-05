# Josh Choi
# Data Mining HW-1
# 10/2/19



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

'''
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
'''
