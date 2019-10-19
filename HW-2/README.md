```
Josh Choi
Professor Yijun Zhao
Data Mining
10/18/19
```
# HW 2 — Data Mining

## 2a. 
*_(0.53, 0.77), (2.05, -0.62), (1.63, -0.91)_*
## 2b. 
w = ∑  α <sub>i</sub> y<sub>i</sub> x<sub>i</sub>
</br>
_*= (0.5641, 0.8187)*_

## 2c. 
y<sub>i</sub> (w<sup>T</sup> x<sub>i</sub> + b) = 1
</br>
y<sub>7</sub> (w<sup>T</sup> x<sub>7</sub> + b) = 1
</br>
[-0.299 + 0.6304] + b = 1
</br>
b = 1 - (0.3314)
</br>
_*b = 0.6686*_
## 2d. 
```
f(x) = (-0.5641, 0.8187)x + 0.6686
```
## 2e. 
= wx + b
</br>
= (-0.5641, 0.8187) (-1, 2) + 0.6686
</br>
= 2.2015 = 2.8701
</br>
*_= 1_*

## 3 
### Poly Kernel
*_Exponent = 1.0_*
```
correctly classififed: 717
correctly classififed: 129
```
*_Exponent = 2.0_*
```
correctly classififed: 810
correctly classififed: 36
```
*_Exponent = 4.0_*
```
correctly classififed: 791
correctly classififed: 355
```
### RBF Kernel
*_Gamma = 0.01_*
```
correctly classififed: 717
correctly classififed: 129
```
*_Gamma = 0.01_*
```
correctly classififed: 810
correctly classififed: 36
```
*_Gamma = 0.01_*
```
correctly classififed: 791
correctly classififed: 355
```
Because the noise interferes with the first runs during training, it outputs results that aren't expected thereby making it almost futile.

### 4
P(y = 'low') = 6/10
P(y = 'high') = 4/10

#### Education Level                 |               Career
```
P(x = 'high school' | y = 'low') = 4/6 + 1/2
P(x = 'high school' | y = 'low') = 1/4 + 1/2
P(x = 'college' | y = 'low') = 2/6 + 1/2
P(x = 'college' | y = 'high') = 3/4 + 1/2
```
#### Career
```
P(x = 'management' | y = 'low') = 2/6 + 1/2
P(x = 'management' | y = 'high') = 3/4 + 1/2
P(x = 'service' | y = 'low') = 4/6 + 1/2
P(x = 'service' | y = 'high') = 1/4 + 1/2
```
#### Years of Experience
```
P(x = 'less than 3' | y = 'low') = 2/6 + 1/3
P(x = 'less than 3' | y = 'high') = 1/4 + 1/3

P(x = '3 to 10' | y = 'low') = 2/6 + 1/3
P(x = '3 to 10' | y = 'low') = 1/4 + 1/3

P(x = 'more than 10' | y = 'low') = 2/6 + 1/3
P(x = 'more than 10' | y = 'high') = 2/4 + 1/3
```

#### x = {"high school", "service", "less than 3"}   --> *low*
```
P(y = 'low'|x) α P(x = 'high school' | y = 'low')*
P(x = 'service' | y = 'low')*P(x = 'less than 3' | y = 'low')*
P(y = 'low')
= 5/8 * 5/8 * 1/3 * 3/5
= 0.781
```

#### x = {"high school", "service", "less than 3"}   --> *low*
```
P(y = 'low'|x) α P(x = 'high school' | y = 'low')*
P(x = 'service' | y = 'low') * P(x = 'less than 3' | y = 'low')*
P(y = 'low')
= 5/8 * 5/8 * 1/3 * 3/5
= 0.781

P(y = 'high'|x) α P(x = 'high school' | y = 'high') * P(x = 'service' | y = 'high')*
P(x = 'less than 3'| y = 'high') * P(y = 'high')
= 1/3 * 1/3 * 2/7 * 2/5 = 0.0127

* 0.0781
```

#### x = {"college", "retail", "less than 3"}   --> *high*
```
P(y = 'low' | x) α P(x = 'college' | y = 'low') * P(x = 'retail' | y = 'low')*
P(x = 'less than 3' | y = 'low') * P(y = 'low')
= 3/8 * 1/8 * 1/3 * 3/5
= 0.0094

P(y = 'high' | x) α P(x = 'college' | y = 'high') * P(x = 'retai' | y = 'high')*
P(x = 'less than 3' | y = 'high') * P(y = 'high')
= 2/3 * 1/6 * 2/7 * 2/5
= 0.0127

* 0.0127
```

#### x = {"graduate", "service", "3 to 10"}   --> *low*
```
P(y = 'low' | x) α P(x = 'graduate' | y = 'low') * P(x = 'service' | y = 'low')
P(x = '3 to 10' | y = 'low') * P(y = 'low')
= 1/8 * 5/8 * 1/3 * 3/5
= 0.0156

P(y = 'high' | x) α P(x = 'graduate' | y = 'high') * P(x = 'service' | y = 'high')
P(x = '3 to 10' | y = 'high') * P(y = 'high')
= 1/7 * 1/3 * 2/7 * 2/5
= 0.0063
```