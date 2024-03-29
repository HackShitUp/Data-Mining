```
Josh Choi
Yijun Zhao
Data Mining
12/6/19
```

# HW 5
1. (40 points) Consider a dataset for frequent set mining as in the following table where we have 6 binary features and each row represents a transaction:
```
001010 
011101 
100010 
111000 
000100 
100101 
001111 
101010 
100100
011001
```
(a) Illustrate the first three levels of the Apriori algorithm (set sizes 1, 2 and 3) for support threshold of 3 transactions, by identifying candidate sets and calculating their support. What are the maximal frequent sets discovered in the first 3 levels?
```
C1
|       100000      |       5        |
|:-----------------:|:--------------:|
|       010000      |       3        |
|       001000      |       5        |
|       000100      |       5        |
|       000000      |       4        |
|       000001      |       4        |

L1
|       100000      |       5        |
|:-----------------:|:--------------:|
|       010000      |       3        |
|       001000      |       6        |
|       000100      |       5        |
|       000010      |       4        |
|       000001      |       4        |



C2
|       110000      |        1       |
|:-----------------:|:--------------:|
|       101000      |        2       |
|       100100      |        2       |
|       1000010     |        2       |
|       1000001     |        1       |
|       011000      |        3       |
|       010100      |        1       |
|       010010      |        0       |
|       010001      |        2       |
|       001100      |        2       |
|       001010      |        3       |
|       001001      |        3       |
|       000110      |        1       |
|       000101      |        3       |
|       000011      |        1       |

L2
|       011000      |       3        |
|:-----------------:|:--------------:|
|       001010      |       3        |
|       001001      |       3        |
|       000101      |       3        |



C3
|       011010      |       0        |
|:-----------------:|:--------------:|
|       011001      |       2        |
|       001011      |       1        |
|       001101      |       2        |

L3
|       011001      |       2        |
|:-----------------:|:--------------:|
|       001101      |       2        |
```


(b) Pick one of the maximal sets and check if any of its subsets are association rules with frequency at least 0.3 and confidence at least 0.6. Pleas explain your answer and show your work.
```
011001 : 2
011000 : 3, 001001 : 3
010000 : 3, 001000 : 6, 000001 : 4

011000  ->  000001  ->  confidence = 2/3  
001001  ->  010000  ->  confidene = 2/3
010000  ->  001001  ->  confidence = 2/3

001000 -> 010001 (confidence = 2/6)
000001 -> 011000 (confidence = 2/4)
```

2. (30 points) In the GSP algorithm, suppose we have the length-3 frequent pattern set L3 as follows:
< {2} {3} {4} >
<{2 5} {3}>
< {3} {4} {5}> 
< {1} {2} {3} >
<{1} {2 5}>
< {1} {5} {3} >
<{5} {3 4}>
Generate length-4 candidates set C4 and frequent pattern set L4. Show your work by writing down the details of the join and prune steps.
```
<{1} {2} {3} {4}>
<{1} {2 5} {3}>
<{1} {5} {3 4}>
<{2 5} {3} {4}>
<{2} {3} {4} {5}>
```

3. (30 points) For the following two time series:
```
X =[3944433946383943]
Y =[3744414439393940]
```
(a) Calculate the L1 norm between X and Y
_L<sub>1</sub>_ norm between _X_ and _Y_:
```
|39 - 37| + |44 - 44| + |43-41| + |39-44| + |46-39| + |38-39| + |39-39| + |43-40| = 20
```
(b) Calculate the DTW distance between X and Y and point out the optimal warping path. (The local cost function is defined as the absolute difference of the two values, e.g., c(x1, y1) = d(39, 37) = 2)
```
40      1       4       3       1       6       2       1       **3**
39      0       5       4       0       5       1       **0**       4
39      0       5       4       0       5       1       **0**       4
39      0       5       4       0       5       **1**       0       4
44      5       0       1       5       **2**       6       5       1
41      2       3       **2       2**       5       3       2       2
44      5       **0**       1       5       2       6       5       1
37     **2**       7       6       2       9       1       2       6
        39      44      43    39     46      38    39    43

```

