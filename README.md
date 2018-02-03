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
- Download [Version 0.4](https://github.com/sepandhaghighi/pycm/archive/v0.4.zip) or [Latest Source ](https://github.com/sepandhaghighi/pycm/archive/master.zip)
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
>>> cm.class_stat
{'G': {0: 0.7745966692414834, 1: 0.408248290463863, 2: 0.5477225575051661}, 'SOA2': {0: 'Excellent', 1: 'Intermediate to Good', 2: 'Intermediate to Good'}, 'LR+': {0: 4.5, 1: 2.9999999999999987, 2: 1.4999999999999998}, 'DOR': {0: 'None', 1: 3.999999999999998, 2: 1.9999999999999998}, 'TNR': {0: 0.7777777777777778, 1: 0.8888888888888888, 2: 0.6666666666666666}, 'FOR': {0: 0.0, 1: 0.19999999999999996, 2: 0.4285714285714286}, 'FN': {0: 0, 1: 2, 2: 3}, 'F1': {0: 0.75, 1: 0.4, 2: 0.5454545454545454}, 'P': {0: 3, 1: 3, 2: 6}, 'LR-': {0: 0.0, 1: 0.7500000000000001, 2: 0.75}, 'ACC': {0: 0.8333333333333334, 1: 0.75, 2: 0.5833333333333334}, 'PRE': {0: 0.25, 1: 0.25, 2: 0.5}, 'NPV': {0: 1.0, 1: 0.8, 2: 0.5714285714285714}, 'POP': {0: 12, 1: 12, 2: 12}, 'TN': {0: 7, 1: 8, 2: 4}, 'TOP': {0: 5, 1: 2, 2: 5}, 'FDR': {0: 0.4, 1: 0.5, 2: 0.4}, 'K': {0: 0.813953488372093, 1: 0.7391304347826088, 2: 0.4736842105263158}, 'F2': {0: 0.8823529411764706, 1: 0.35714285714285715, 2: 0.5172413793103449}, 'FP': {0: 2, 1: 1, 2: 2}, 'TON': {0: 7, 1: 10, 2: 7}, 'N': {0: 9, 1: 9, 2: 6}, 'TPR': {0: 1.0, 1: 0.3333333333333333, 2: 0.5}, 'SOA3': {0: 'Very Good', 1: 'Good', 2: 'Moderate'}, 'BM': {0: 0.7777777777777777, 1: 0.2222222222222221, 2: 0.16666666666666652}, 'TP': {0: 3, 1: 1, 2: 3}, 'SOA1': {0: 'Almost Perfect', 1: 'Substantial', 2: 'Moderate'}, 'RACC': {0: 0.10416666666666667, 1: 0.041666666666666664, 2: 0.20833333333333334}, 'FPR': {0: 0.2222222222222222, 1: 0.11111111111111116, 2: 0.33333333333333337}, 'ERR': {0: 0.16666666666666663, 1: 0.25, 2: 0.41666666666666663}, 'MCC': {0: 0.6831300510639732, 1: 0.25819888974716115, 2: 0.1690308509457033}, 'PPV': {0: 0.6, 1: 0.5, 2: 0.6}, 'FNR': {0: 0.0, 1: 0.6666666666666667, 2: 0.5}, 'MK': {0: 0.6000000000000001, 1: 0.30000000000000004, 2: 0.17142857142857126}, 'F0.5': {0: 0.6521739130434783, 1: 0.45454545454545453, 2: 0.5769230769230769}}
>>> cm.overall_stat
{'Strength_Of_Agreement': 'Fair', 'Overall_Kappa': 0.35483870967741943, 'Overall_ACC': 0.5833333333333334}
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




Overall Statistics : 

Overall_ACC                                                      0.58333
Overall_Kappa                                                    0.35484
Strength_Of_Agreement(Altman)                                    Fair
Strength_Of_Agreement(Fleiss)                                    Poor
Strength_Of_Agreement(Landis and Koch)                           Fair

Class Statistics :

Classes                                                          0                       1                       2                       
ACC(accuracy)                                                    0.83333                 0.75                    0.58333                 
BM(Informedness or Bookmaker Informedness)                       0.77778                 0.22222                 0.16667                 
DOR(Diagnostic odds ratio)                                       None                    4.0                     2.0                     
ERR(Error Rate)                                                  0.16667                 0.25                    0.41667                 
F0.5(F0.5 Score)                                                 0.65217                 0.45455                 0.57692                 
F1(F1 Score - harmonic mean of precision and sensitivity)        0.75                    0.4                     0.54545                 
F2(F2 Score)                                                     0.88235                 0.35714                 0.51724                 
FDR(false discovery rate)                                        0.4                     0.5                     0.4                     
FN(false negative/miss/Type II error)                            0                       2                       3                       
FNR(miss rate or false negative rate)                            0.0                     0.66667                 0.5                     
FOR(false omission rate)                                         0.0                     0.2                     0.42857                 
FP(false positive/Type I error/false alarm)                      2                       1                       2                       
FPR(fall-out or false positive rate)                             0.22222                 0.11111                 0.33333                 
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.40825                 0.54772                 
K(Kappa)                                                         0.81395                 0.73913                 0.47368                 
LR+(Positive likelihood ratio)                                   4.5                     3.0                     1.5                     
LR-(Negative likelihood ratio)                                   0.0                     0.75                    0.75                    
MCC(Matthews correlation coefficient)                            0.68313                 0.2582                  0.16903                 
MK(Markedness)                                                   0.6                     0.3                     0.17143                 
N(Condition negative)                                            9                       9                       6                       
NPV(negative predictive value)                                   1.0                     0.8                     0.57143                 
P(Condition positive)                                            3                       3                       6                       
POP(Population)                                                  12                      12                      12                      
PPV(precision or positive predictive value)                      0.6                     0.5                     0.6                     
PRE(Prevalence)                                                  0.25                    0.25                    0.5                     
RACC(Random Accuracy)                                            0.10417                 0.04167                 0.20833                 
SOA1(Strength of Agreement,Landis and Koch)                      Almost Perfect          Substantial             Moderate                
SOA2(Strength of Agreement,Fleiss)                               Excellent               Intermediate to Good    Intermediate to Good    
SOA3(Strength of Agreement,Altman)                               Very Good               Good                    Moderate                
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

>>> cm.stat()
Overall Statistics : 

Overall_ACC                                                      0.58333
Overall_Kappa                                                    0.35484
Strength_Of_Agreement(Altman)                                    Fair
Strength_Of_Agreement(Fleiss)                                    Poor
Strength_Of_Agreement(Landis and Koch)                           Fair

Class Statistics :

Classes                                                          0                       1                       2                       
ACC(accuracy)                                                    0.83333                 0.75                    0.58333                 
BM(Informedness or Bookmaker Informedness)                       0.77778                 0.22222                 0.16667                 
DOR(Diagnostic odds ratio)                                       None                    4.0                     2.0                     
ERR(Error Rate)                                                  0.16667                 0.25                    0.41667                 
F0.5(F0.5 Score)                                                 0.65217                 0.45455                 0.57692                 
F1(F1 Score - harmonic mean of precision and sensitivity)        0.75                    0.4                     0.54545                 
F2(F2 Score)                                                     0.88235                 0.35714                 0.51724                 
FDR(false discovery rate)                                        0.4                     0.5                     0.4                     
FN(false negative/miss/Type II error)                            0                       2                       3                       
FNR(miss rate or false negative rate)                            0.0                     0.66667                 0.5                     
FOR(false omission rate)                                         0.0                     0.2                     0.42857                 
FP(false positive/Type I error/false alarm)                      2                       1                       2                       
FPR(fall-out or false positive rate)                             0.22222                 0.11111                 0.33333                 
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.40825                 0.54772                 
K(Kappa)                                                         0.81395                 0.73913                 0.47368                 
LR+(Positive likelihood ratio)                                   4.5                     3.0                     1.5                     
LR-(Negative likelihood ratio)                                   0.0                     0.75                    0.75                    
MCC(Matthews correlation coefficient)                            0.68313                 0.2582                  0.16903                 
MK(Markedness)                                                   0.6                     0.3                     0.17143                 
N(Condition negative)                                            9                       9                       6                       
NPV(negative predictive value)                                   1.0                     0.8                     0.57143                 
P(Condition positive)                                            3                       3                       6                       
POP(Population)                                                  12                      12                      12                      
PPV(precision or positive predictive value)                      0.6                     0.5                     0.6                     
PRE(Prevalence)                                                  0.25                    0.25                    0.5                     
RACC(Random Accuracy)                                            0.10417                 0.04167                 0.20833                 
SOA1(Strength of Agreement,Landis and Koch)                      Almost Perfect          Substantial             Moderate                
SOA2(Strength of Agreement,Fleiss)                               Excellent               Intermediate to Good    Intermediate to Good    
SOA3(Strength of Agreement,Altman)                               Very Good               Good                    Moderate                
TN(true negative/correct rejection)                              7                       8                       4                       
TNR(specificity or true negative rate)                           0.77778                 0.88889                 0.66667                 
TON(Test outcome negative)                                       7                       10                      7                       
TOP(Test outcome positive)                                       5                       2                       5                       
TP(true positive/hit)                                            3                       1                       3                       
TPR(sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333                 0.5                     
                   
```
				

For more information visit [here](Document.ipynb "Document")

<div align="center">

<a href="https://asciinema.org/a/159577" target="_blank"><img src="https://asciinema.org/a/159577.png" /></a>

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
  - [x] ERR
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
  - [x] RACC
- [ ] Outputs
  - [ ] CSV File
  - [ ] HTML File
  - [x] Output File
  - [x] Table
  - [x] Normalized Table
- [x] Overall Statistics
  - [x] Kappa
  - [x] Overall ACC
  - [x] Strength of Agreement
    - [x] Landis and Koch
    - [x] Fleiss
    - [x] Altman


## Contribution			

You can fork the repository, improve or fix some part of it and then send the pull requests back if you want to see them here. I really appreciate that. ❤️			

Remember to write a few tests for your code before sending pull requests. 
e


## References

<blockquote>1- Landis JR, Koch GG. The measurement of observer agreement for categorical data. Biometrics 1977; 33:159–174 </blockquote>

<blockquote>2- Powers, D. M. W. (2011). Evaluation: from precision, recall and f-measure to roc, informedness, markedness & correlation. Journal of Machine Learning Technologies.</blockquote>


<blockquote>3-  C. Sammut, G. Webb, Encyclopedia of Machine Learning. Springer, 2011. Springer reference.</blockquote>

<blockquote>4- Fleiss, J. L. (1971). Measuring nominal scale agreement among many raters. Psychological Bulletin, 76(5), 378-382.
http://dx.doi.org/10.1037/h0031619</blockquote>

<blockquote>5- Altman D.G. 1991. Practical Statistics for Medical Research.
Chapman and Hall, London.</blockquote>




## Cite

If you use pycm in your research , please cite this :

<pre>
Sepand Haghighi. “Pycm : Multi Class Confusion Matrix Library in Python”. Zenodo, January 22, 2018. doi:10.5281/zenodo.1157173.
</pre>
<pre>

@misc{https://doi.org/10.5281/zenodo.1157173,
  doi = {10.5281/zenodo.1157173},
  author = {{Sepand Haghighi}},
  keywords = {Machine Learning,  statistics,  confusion-matrix,  statistical-analysis,  matrices,  matrix},
  title = {Pycm : Multi Class Confusion Matrix Library In Python},
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
