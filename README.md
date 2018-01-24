<div align="center">
<img src="Otherfiles/logo.png" width=250px height=250px>
<br/>
<br/>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>
<a href="Document.ipynb"><img src="https://img.shields.io/badge/doc-latest-orange.svg"></a>
<a href="https://travis-ci.org/sepandhaghighi/pycm"><img src="https://travis-ci.org/sepandhaghighi/pycm.svg?branch=master"></a>
<a href="https://ci.appveyor.com/project/sepandhaghighi/pycm"><img src="https://ci.appveyor.com/api/projects/status/nbe96d7gk2693ju0?svg=true"></a>
<a href="https://codecov.io/gh/sepandhaghighi/pycm">
  <img src="https://codecov.io/gh/sepandhaghighi/pycm/branch/master/graph/badge.svg" />
</a>
<a class="badge-align" href="https://www.codacy.com/app/sepand-haghighi/pycm?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sepandhaghighi/pycm&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/5d9463998a0040d09afc2b80c389365c"/></a>
<a href="https://badge.fury.io/py/pycm"><img src="https://badge.fury.io/py/pycm.svg" alt="PyPI version" height="18"></a>
<a href="https://zenodo.org/badge/latestdoi/118506495"><img src="https://zenodo.org/badge/118506495.svg" alt="DOI"></a>

</div>

----------

## Overview	
In the field of machine learning and specifically the problem of statistical classification, a confusion matrix, also known as an error matrix, is a specific table layout that allows visualization of the performance of an algorithm, typically a supervised learning one (in unsupervised learning it is usually called a matching matrix). Each row of the matrix represents the instances in a predicted class while each column represents the instances in an actual class (or vice versa)		
pycm(python confusion matrix) is a multi class confusion matrix library in python.

## Installation		

### Source Code
- Download [Version 0.2](https://github.com/sepandhaghighi/pycm/archive/v0.2.zip) or [Latest Source ](https://github.com/sepandhaghighi/pycm/archive/master.zip)
- Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- Run `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install pycm` or `pip3 install pycm` (Need root access)

## Usage

```python
>>> from pycm import *
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(y_actu, y_pred)
>>> cm.statistic_result
{'FDR': {0: 0.4, 1: 0.5, 2: 0.4}, 'PPV': {0: 0.6, 1: 0.5, 2: 0.6}, 'TNR': {0: 0.77778, 1: 0.88889, 2: 0.66667}, 'POP': {0: 12, 1: 12, 2: 12}, 'TPR': {0: 1.0, 1: 0.33333, 2: 0.5}, 'F1': {0: 0.75, 1: 0.4, 2: 0.54545}, 'TOP': {0: 5, 1: 2, 2: 5}, 'MCC': {0: 0.68313, 1: 0.2582, 2: 0.16903}, 'P': {0: 3, 1: 3, 2: 6}, 'G': {0: 0.7746, 1: 0.40825, 2: 0.54772}, 'LR+': {0: 4.50005, 1: 3.0, 2: 1.50002}, 'TN': {0: 7, 1: 8, 2: 4}, 'FOR': {0: 0.0, 1: 0.2, 2: 0.42857}, 'FPR': {0: 0.22222, 1: 0.11111, 2: 0.33333}, 'BM': {0: 0.77778, 1: 0.22222, 2: 0.16667}, 'ACC': {0: 0.83333, 1: 0.75, 2: 0.58333}, 'DOR': {0: 'None', 1: 4.0, 2: 2.00003}, 'FN': {0: 0, 1: 2, 2: 3}, 'TP': {0: 3, 1: 1, 2: 3}, 'FNR': {0: 0.0, 1: 0.66667, 2: 0.5}, 'N': {0: 9, 1: 9, 2: 6}, 'LR-': {0: 0.0, 1: 0.75, 2: 0.75}, 'NPV': {0: 1.0, 1: 0.8, 2: 0.57143}, 'TON': {0: 7, 1: 10, 2: 7}, 'MK': {0: 0.6, 1: 0.3, 2: 0.17143}, 'PRE': {0: 0.25, 1: 0.25, 2: 0.5}, 'FP': {0: 2, 1: 1, 2: 2}}
>>> cm.classes
[0, 1, 2]
>>> cm.table
{0: {0: 3, 1: 0, 2: 0}, 1: {0: 0, 1: 1, 2: 2}, 2: {0: 2, 1: 1, 2: 3}}
>>> print(cm)
Predict          0        1        2        
Actual
0                3        0        0        
1                0        1        2        
2                2        1        3        




Classes                                                          0                       1                       2                       
ACC(accuracy)                                                    0.83333                 0.75                    0.58333                 
BM(Informedness or Bookmaker Informedness)                       0.77778                 0.22222                 0.16667                 
DOR(Diagnostic odds ratio)                                       None                    4.0                     2.00003                 
F1(F1 Score - harmonic mean of precision and sensitivity)        0.75                    0.4                     0.54545                 
FDR(false discovery rate)                                        0.4                     0.5                     0.4                     
FN(false negative/miss/Type II error)                            0                       2                       3                       
FNR(miss rate or false negative rate)                            0.0                     0.66667                 0.5                     
FOR(false omission rate)                                         0.0                     0.2                     0.42857                 
FP(false positive/Type I error/false alarm)                      2                       1                       2                       
FPR(fall-out or false positive rate)                             0.22222                 0.11111                 0.33333                 
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.40825                 0.54772                 
LR+(Positive likelihood ratio)                                   4.50005                 3.0                     1.50002                 
LR-(Negative likelihood ratio)                                   0.0                     0.75                    0.75                    
MCC(Matthews correlation coefficient)                            0.68313                 0.2582                  0.16903                 
MK(Markedness)                                                   0.6                     0.3                     0.17143                 
N(Condition negative)                                            9                       9                       6                       
NPV(negative predictive value)                                   1.0                     0.8                     0.57143                 
P(Condition positive)                                            3                       3                       6                       
POP(Population)                                                  12                      12                      12                      
PPV(precision or positive predictive value)                      0.6                     0.5                     0.6                     
PRE(Prevalence)                                                  0.25                    0.25                    0.5                     
TN(true negative/correct rejection)                              7                       8                       4                       
TNR(specificity or true negative rate)                           0.77778                 0.88889                 0.66667                 
TON(Test outcome negative)                                       7                       10                      7                       
TOP(Test outcome positive)                                       5                       2                       5                       
TP(true positive/hit)                                            3                       1                       3                       
TPR(sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333                 0.5    

>>> cm.matrix()
Predict          0        1        2        
Actual
0                3        0        0        
1                0        1        2        
2                2        1        3        

>>> cm.normalized_matrix()
Predict          0              1              2              
Actual
0                1.0            0.0            0.0            
1                0.0            0.33333        0.66667        
2                0.33333        0.16667        0.5            

>>> cm.params()
Classes                                                          0                       1                       2                       
ACC(accuracy)                                                    0.83333                 0.75                    0.58333                 
BM(Informedness or Bookmaker Informedness)                       0.77778                 0.22222                 0.16667                 
DOR(Diagnostic odds ratio)                                       None                    4.0                     2.00003                 
F1(F1 Score - harmonic mean of precision and sensitivity)        0.75                    0.4                     0.54545                 
FDR(false discovery rate)                                        0.4                     0.5                     0.4                     
FN(false negative/miss/Type II error)                            0                       2                       3                       
FNR(miss rate or false negative rate)                            0.0                     0.66667                 0.5                     
FOR(false omission rate)                                         0.0                     0.2                     0.42857                 
FP(false positive/Type I error/false alarm)                      2                       1                       2                       
FPR(fall-out or false positive rate)                             0.22222                 0.11111                 0.33333                 
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.40825                 0.54772                 
LR+(Positive likelihood ratio)                                   4.50005                 3.0                     1.50002                 
LR-(Negative likelihood ratio)                                   0.0                     0.75                    0.75                    
MCC(Matthews correlation coefficient)                            0.68313                 0.2582                  0.16903                 
MK(Markedness)                                                   0.6                     0.3                     0.17143                 
N(Condition negative)                                            9                       9                       6                       
NPV(negative predictive value)                                   1.0                     0.8                     0.57143                 
P(Condition positive)                                            3                       3                       6                       
POP(Population)                                                  12                      12                      12                      
PPV(precision or positive predictive value)                      0.6                     0.5                     0.6                     
PRE(Prevalence)                                                  0.25                    0.25                    0.5                     
TN(true negative/correct rejection)                              7                       8                       4                       
TNR(specificity or true negative rate)                           0.77778                 0.88889                 0.66667                 
TON(Test outcome negative)                                       7                       10                      7                       
TOP(Test outcome positive)                                       5                       2                       5                       
TP(true positive/hit)                                            3                       1                       3                       
TPR(sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333                 0.5                     


```
				

For more information visit [here](Document.ipynb "Document")

<div align="center">

<a href="https://asciinema.org/a/158541" target="_blank"><img src="https://asciinema.org/a/158541.png" /></a>

</div>

## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!							
or send an email to [sepand@qpage.ir](mailto:sepand@qpage.ir "sepand@qpage.ir"). 


## TODO		
- [x] Basic
  - [x] TP
  - [x] FP
  - [x] FN
  - [x] TN
  - [x] Population
  - [x] Condition positive
  - [x] Condition negative 
  - [x] Test outcome positive
  - [x] Test outcome negative
- [x] Class Statistics
  - [x] ACC
  - [x] BM
  - [x] DOR
  - [x] F1-Score
  - [x] FDR
  - [x] FNR
  - [x] FOR
  - [x] FPR
  - [x] LR+
  - [x] LR-
  - [x] MCC
  - [x] MK
  - [x] NPV
  - [x] PPV
  - [x] TNR
  - [x] TPR
  - [x] Prevalence
  - [x] G-measure
- [ ] Outputs
  - [ ] CSV File
  - [ ] HTML File
  - [x] Table
  - [x] Normalized Table
- [ ] Overall Statistics
  - [ ] Kappa
  - [ ] 95% CI


## Contribution			

You can fork the repository, improve or fix some part of it and then send the pull requests back if you want to see them here. I really appreciate that. ❤️			

Remember to write a few tests for your code before sending pull requests. 

Sepand Haghighi. “Pycm : Multi Class Confusion Matrix Library in Python”. Zenodo, January 22, 2018. doi:10.5281/zenodo.1157173.


## Cite

If you use pycm in your research , please cite this :

<pre>
Sepand Haghighi. “Pycm : Multi Class Confusion Matrix Library in Python”. Zenodo, January 22, 2018. doi:10.5281/zenodo.1157173.
</pre>
<pre>

@misc{https://doi.org/10.5281/zenodo.1157173,
  doi = {10.5281/zenodo.1157173},
  author = {Sepand Haghighi},
  keywords = {Machine Learning, statistics, confusion-matrix, statistical-analysis, matrices, matrix},
  title = {Pycm : Multi Class Confusion Matrix Library in Python},
  pages = {--},
  publisher = {Zenodo},
  year = {2018}
}


</pre>


## License

<a href="https://github.com/sepandhaghighi/pycm/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mashape/apistatus.svg"/></a>


## Donate to our project
								
<h3>Bitcoin :</h3>					

```12Xm1qL4MXYWiY9sRMoa3VpfTfw6su3vNq```			



<h3>Payping (For Iranian citizens) :</h3>

<a href="http://www.payping.net/sepandhaghighi" target="__blank"><img src="http://www.qpage.ir/images/payping.png" height=100px width=100px></a>
