# Josh Choi
# Data Mining HW-1
# 10/2/19



## KNN
*KNN* is a classification algorithim. It finds the *k* nearest classifications and finds the plurality of the classifications for an unread dataset. For instance, given attributes _a_ and _b_, a new dataset _J_ is introduced. Find the nearest _k_ number of classifications adjacent to _J_, calculate its plurality to classify _J_. So, how do we do this? The hard part isn't finding the plurality. Rather, it's finding the *n* or the _k_ nearest neighbors with the new dataset. To do this, we have to calculate the distance using the Euclidean Distance:
```
SQUARE_ROOT(
    pow(SIGMA(xi - yi))
)
```

