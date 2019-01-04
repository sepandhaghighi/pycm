<div align="center">
<img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/logo.png" width=250px height=250px>
<br/>
<br/>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>
<a href="/Document"><img src="https://img.shields.io/badge/doc-latest-orange.svg"></a>
<a href="https://codecov.io/gh/sepandhaghighi/pycm">
  <img src="https://codecov.io/gh/sepandhaghighi/pycm/branch/master/graph/badge.svg" />
</a>
<a href="https://badge.fury.io/py/pycm"><img src="https://badge.fury.io/py/pycm.svg" alt="PyPI version" height="18"></a>
<a href="https://anaconda.org/sepandhaghighi/pycm"><img src="https://anaconda.org/sepandhaghighi/pycm/badges/version.svg"></a>
</div>

----------
## Table of contents					
   * [Overview](https://github.com/sepandhaghighi/pycm#overview)
   * [Installation](https://github.com/sepandhaghighi/pycm#installation)
   * [Usage](https://github.com/sepandhaghighi/pycm#usage)
   * [Document](https://github.com/sepandhaghighi/pycm/tree/master/Document)
   * [Issues & Bug Reports](https://github.com/sepandhaghighi/pycm#issues--bug-reports)
   * [Todo](https://github.com/sepandhaghighi/pycm/blob/master/TODO.md)
   * [Outputs](https://github.com/sepandhaghighi/pycm#outputs)
   * [Dependencies](https://github.com/sepandhaghighi/pycm#dependencies)
   * [Contribution](https://github.com/sepandhaghighi/pycm#contribution)
   * [References](https://github.com/sepandhaghighi/pycm#references)
   * [Cite](https://github.com/sepandhaghighi/pycm#cite)
   * [Authors](https://github.com/sepandhaghighi/pycm/blob/master/AUTHORS.md)
   * [License](https://github.com/sepandhaghighi/pycm#license)
   * [Donate](https://github.com/sepandhaghighi/pycm#donate-to-our-project)
   * [Changelog](https://github.com/sepandhaghighi/pycm/blob/master/CHANGELOG.md)

## Overview

<p align="justify">	
PyCM is a multi-class confusion matrix library written in Python that supports both input data vectors and direct matrix, and a proper tool for post-classification model evaluation that supports most classes and overall statistics parameters.	
PyCM is the swiss-army knife of confusion matrices, targeted mainly at data scientists that need a broad array of metrics for predictive models and an accurate evaluation of large variety of classifiers.

</p>

<div align="center">
<img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/block_diagram.jpg">
<p>Fig1. PyCM Block Diagram</p>
</div>


<table>
	<tr> 
		<td align="center">Open Hub</td>
		<td align="center"><a href="https://www.openhub.net/p/pycm"><img src="https://www.openhub.net/p/pycm/widgets/project_thin_badge.gif"></a></td>	
	</tr>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/count/pycm"><img src="http://pepy.tech/badge/pycm"></a></td>
	</tr>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center"><a href="https://github.com/sepandhaghighi/pycm"><img src="https://img.shields.io/github/stars/sepandhaghighi/pycm.svg?style=social&label=Stars"></a></td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">master</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center">Travis</td>
		<td align="center"><a href="https://travis-ci.org/sepandhaghighi/pycm"><img src="https://travis-ci.org/sepandhaghighi/pycm.svg?branch=master"></a></td>
		<td align="center"><a href="https://travis-ci.org/sepandhaghighi/pycm"><img src="https://travis-ci.org/sepandhaghighi/pycm.svg?branch=dev"></a></td>
	</tr>
	<tr>
		<td align="center">AppVeyor</td>
		<td align="center"><a href="https://ci.appveyor.com/project/sepandhaghighi/pycm"><img src="https://ci.appveyor.com/api/projects/status/nbe96d7gk2693ju0/branch/master?svg=true"></a></td>
		<td align="center"><a href="https://ci.appveyor.com/project/sepandhaghighi/pycm"><img src="https://ci.appveyor.com/api/projects/status/nbe96d7gk2693ju0/branch/dev?svg=true"></a></td>
	</tr>
</table>


<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td align="center"><a class="badge-align" href="https://www.codacy.com/app/sepand-haghighi/pycm?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sepandhaghighi/pycm&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/5d9463998a0040d09afc2b80c389365c"/></a></td>	
		<td align="center"><a href="https://www.codefactor.io/repository/github/sepandhaghighi/pycm/overview/dev"><img src="https://www.codefactor.io/repository/github/sepandhaghighi/pycm/badge/dev" alt="CodeFactor" /></a></td>	
		<td align="center"><a href="https://codebeat.co/projects/github-com-sepandhaghighi-pycm-dev"><img alt="codebeat badge" src="https://codebeat.co/badges/f6642af1-c343-48c2-bd3e-eee802facf39" /></a></td>	
	</tr>
</table>



## Installation		

### Source code
- Download [Version 1.8](https://github.com/sepandhaghighi/pycm/archive/v1.8.zip) or [Latest Source ](https://github.com/sepandhaghighi/pycm/archive/dev.zip)
- Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- Run `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install pycm==1.8` or `pip3 install pycm==1.8` (Need root access)

### Conda

- Check [Conda Managing Package](https://conda.io/docs/user-guide/tasks/manage-pkgs.html#installing-packages-from-anaconda-org)
- `conda install -c sepandhaghighi pycm` (Need root access)

### Easy install

- Run `easy_install --upgrade pycm` (Need root access)

## Usage

		
### From vector
```pycon
>>> from pycm import *
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2] # or y_actu = numpy.array([2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2])
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2] # or y_pred = numpy.array([0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2])
>>> cm = ConfusionMatrix(actual_vector=y_actu, predict_vector=y_pred) # Create CM From Data
>>> cm.classes
[0, 1, 2]
>>> cm.table
{0: {0: 3, 1: 0, 2: 0}, 1: {0: 0, 1: 1, 2: 2}, 2: {0: 2, 1: 1, 2: 3}}
>>> print(cm)
Predict          0    1    2    
Actual
0                3    0    0    

1                0    1    2    

2                2    1    3    





Overall Statistics : 

95% CI                                                           (0.30439,0.86228)
AUNP                                                             0.66667
AUNU                                                             0.69444
Bennett S                                                        0.375
CBA                                                              0.47778
Chi-Squared                                                      6.6
Chi-Squared DF                                                   4
Conditional Entropy                                              0.95915
Cramer V                                                         0.5244
Cross Entropy                                                    1.59352
Gwet AC1                                                         0.38931
Hamming Loss                                                     0.41667
Joint Entropy                                                    2.45915
KL Divergence                                                    0.09352
Kappa                                                            0.35484
Kappa 95% CI                                                     (-0.07708,0.78675)
Kappa No Prevalence                                              0.16667
Kappa Standard Error                                             0.22036
Kappa Unbiased                                                   0.34426
Lambda A                                                         0.16667
Lambda B                                                         0.42857
Mutual Information                                               0.52421
NIR                                                              0.5
Overall ACC                                                      0.58333
Overall CEN                                                      0.46381
Overall J                                                        (1.225,0.40833)
Overall MCC                                                      0.36667
Overall MCEN                                                     0.51894
Overall RACC                                                     0.35417
Overall RACCU                                                    0.36458
P-Value                                                          0.38721
PPV Macro                                                        0.56667
PPV Micro                                                        0.58333
Phi-Squared                                                      0.55
RCI                                                              0.34947
RR                                                               4.0
Reference Entropy                                                1.5
Response Entropy                                                 1.48336
SOA1(Landis & Koch)                                              Fair
SOA2(Fleiss)                                                     Poor
SOA3(Altman)                                                     Fair
SOA4(Cicchetti)                                                  Poor
Scott PI                                                         0.34426
Standard Error                                                   0.14232
TPR Macro                                                        0.61111
TPR Micro                                                        0.58333
Zero-one Loss                                                    5

Class Statistics :

Classes                                                          0                       1                       2                       
ACC(Accuracy)                                                    0.83333                 0.75                    0.58333                 
AUC(Area under the roc curve)                                    0.88889                 0.61111                 0.58333                 
AUCI(Auc value interpretation)                                   Very Good               Fair                    Poor                    
BM(Informedness or bookmaker informedness)                       0.77778                 0.22222                 0.16667                 
CEN(Confusion entropy)                                           0.25                    0.49658                 0.60442                 
DOR(Diagnostic odds ratio)                                       None                    4.0                     2.0                     
DP(Discriminant power)                                           None                    0.33193                 0.16597                 
DPI(Discriminant power interpretation)                           None                    Poor                    Poor                    
ERR(Error rate)                                                  0.16667                 0.25                    0.41667                 
F0.5(F0.5 score)                                                 0.65217                 0.45455                 0.57692                 
F1(F1 score - harmonic mean of precision and sensitivity)        0.75                    0.4                     0.54545                 
F2(F2 score)                                                     0.88235                 0.35714                 0.51724                 
FDR(False discovery rate)                                        0.4                     0.5                     0.4                     
FN(False negative/miss/type 2 error)                             0                       2                       3                       
FNR(Miss rate or false negative rate)                            0.0                     0.66667                 0.5                     
FOR(False omission rate)                                         0.0                     0.2                     0.42857                 
FP(False positive/type 1 error/false alarm)                      2                       1                       2                       
FPR(Fall-out or false positive rate)                             0.22222                 0.11111                 0.33333                 
G(G-measure geometric mean of precision and sensitivity)         0.7746                  0.40825                 0.54772                 
GI(Gini index)                                                   0.77778                 0.22222                 0.16667                 
IS(Information score)                                            1.26303                 1.0                     0.26303                 
J(Jaccard index)                                                 0.6                     0.25                    0.375                   
LS(Lift score)                                                   2.4                     2.0                     1.2                     
MCC(Matthews correlation coefficient)                            0.68313                 0.2582                  0.16903                 
MCEN(Modified confusion entropy)                                 0.26439                 0.5                     0.6875                  
MK(Markedness)                                                   0.6                     0.3                     0.17143                 
N(Condition negative)                                            9                       9                       6                       
NLR(Negative likelihood ratio)                                   0.0                     0.75                    0.75                    
NPV(Negative predictive value)                                   1.0                     0.8                     0.57143                 
P(Condition positive or support)                                 3                       3                       6                       
PLR(Positive likelihood ratio)                                   4.5                     3.0                     1.5                     
PLRI(Positive likelihood ratio interpretation)                   Poor                    Poor                    Poor                    
POP(Population)                                                  12                      12                      12                      
PPV(Precision or positive predictive value)                      0.6                     0.5                     0.6                     
PRE(Prevalence)                                                  0.25                    0.25                    0.5                     
RACC(Random accuracy)                                            0.10417                 0.04167                 0.20833                 
RACCU(Random accuracy unbiased)                                  0.11111                 0.0434                  0.21007                 
TN(True negative/correct rejection)                              7                       8                       4                       
TNR(Specificity or true negative rate)                           0.77778                 0.88889                 0.66667                 
TON(Test outcome negative)                                       7                       10                      7                       
TOP(Test outcome positive)                                       5                       2                       5                       
TP(True positive/hit)                                            3                       1                       3                       
TPR(Sensitivity, recall, hit rate, or true positive rate)        1.0                     0.33333                 0.5                     
Y(Youden index)                                                  0.77778                 0.22222                 0.16667                 
dInd(Distance index)                                             0.22222                 0.67586                 0.60093                 
sInd(Similarity index)                                           0.84287                 0.52209                 0.57508                 

>>> cm.print_matrix()
Predict          0    1    2    
Actual
0                3    0    0    

1                0    1    2    

2                2    1    3    

>>> cm.print_normalized_matrix()
Predict          0          1          2          
Actual
0                1.0        0.0        0.0        

1                0.0        0.33333    0.66667    

2                0.33333    0.16667    0.5        

>>> cm.print_matrix(one_vs_all=True,class_name=0)   # One-Vs-All, new in version 1.4
Predict          0    ~    
Actual
0                3    0    

~                2    7    


```
### Direct CM
```pycon
>>> from pycm import *
>>> cm2 = ConfusionMatrix(matrix={"Class1": {"Class1": 1, "Class2":2}, "Class2": {"Class1": 0, "Class2": 5}}) # Create CM Directly
>>> cm2
pycm.ConfusionMatrix(classes: ['Class1', 'Class2'])
>>> print(cm2)
Predict          Class1    Class2    
Actual
Class1           1         2         

Class2           0         5         





Overall Statistics : 

95% CI                                                           (0.44994,1.05006)
AUNP                                                             0.66667
AUNU                                                             0.66667
Bennett S                                                        0.5
CBA                                                              0.52381
Chi-Squared                                                      1.90476
Chi-Squared DF                                                   1
Conditional Entropy                                              0.34436
Cramer V                                                         0.48795
Cross Entropy                                                    1.2454
Gwet AC1                                                         0.6
Hamming Loss                                                     0.25
Joint Entropy                                                    1.29879
KL Divergence                                                    0.29097
Kappa                                                            0.38462
Kappa 95% CI                                                     (-0.354,1.12323)
Kappa No Prevalence                                              0.5
Kappa Standard Error                                             0.37684
Kappa Unbiased                                                   0.33333
Lambda A                                                         0.33333
Lambda B                                                         0.0
Mutual Information                                               0.1992
NIR                                                              0.625
Overall ACC                                                      0.75
Overall CEN                                                      0.44812
Overall J                                                        (1.04762,0.52381)
Overall MCC                                                      0.48795
Overall MCEN                                                     0.29904
Overall RACC                                                     0.59375
Overall RACCU                                                    0.625
P-Value                                                          0.36974
PPV Macro                                                        0.85714
PPV Micro                                                        0.75
Phi-Squared                                                      0.2381
RCI                                                              0.20871
RR                                                               4.0
Reference Entropy                                                0.95443
Response Entropy                                                 0.54356
SOA1(Landis & Koch)                                              Fair
SOA2(Fleiss)                                                     Poor
SOA3(Altman)                                                     Fair
SOA4(Cicchetti)                                                  Poor
Scott PI                                                         0.33333
Standard Error                                                   0.15309
TPR Macro                                                        0.66667
TPR Micro                                                        0.75
Zero-one Loss                                                    2

Class Statistics :

Classes                                                          Class1                  Class2                  
ACC(Accuracy)                                                    0.75                    0.75                    
AUC(Area under the roc curve)                                    0.66667                 0.66667                 
AUCI(Auc value interpretation)                                   Fair                    Fair                    
BM(Informedness or bookmaker informedness)                       0.33333                 0.33333                 
CEN(Confusion entropy)                                           0.5                     0.43083                 
DOR(Diagnostic odds ratio)                                       None                    None                    
DP(Discriminant power)                                           None                    None                    
DPI(Discriminant power interpretation)                           None                    None                    
ERR(Error rate)                                                  0.25                    0.25                    
F0.5(F0.5 score)                                                 0.71429                 0.75758                 
F1(F1 score - harmonic mean of precision and sensitivity)        0.5                     0.83333                 
F2(F2 score)                                                     0.38462                 0.92593                 
FDR(False discovery rate)                                        0.0                     0.28571                 
FN(False negative/miss/type 2 error)                             2                       0                       
FNR(Miss rate or false negative rate)                            0.66667                 0.0                     
FOR(False omission rate)                                         0.28571                 0.0                     
FP(False positive/type 1 error/false alarm)                      0                       2                       
FPR(Fall-out or false positive rate)                             0.0                     0.66667                 
G(G-measure geometric mean of precision and sensitivity)         0.57735                 0.84515                 
GI(Gini index)                                                   0.33333                 0.33333                 
IS(Information score)                                            1.41504                 0.19265                 
J(Jaccard index)                                                 0.33333                 0.71429                 
LS(Lift score)                                                   2.66667                 1.14286                 
MCC(Matthews correlation coefficient)                            0.48795                 0.48795                 
MCEN(Modified confusion entropy)                                 0.38998                 0.51639                 
MK(Markedness)                                                   0.71429                 0.71429                 
N(Condition negative)                                            5                       3                       
NLR(Negative likelihood ratio)                                   0.66667                 0.0                     
NPV(Negative predictive value)                                   0.71429                 1.0                     
P(Condition positive or support)                                 3                       5                       
PLR(Positive likelihood ratio)                                   None                    1.5                     
PLRI(Positive likelihood ratio interpretation)                   None                    Poor                    
POP(Population)                                                  8                       8                       
PPV(Precision or positive predictive value)                      1.0                     0.71429                 
PRE(Prevalence)                                                  0.375                   0.625                   
RACC(Random accuracy)                                            0.04688                 0.54688                 
RACCU(Random accuracy unbiased)                                  0.0625                  0.5625                  
TN(True negative/correct rejection)                              5                       1                       
TNR(Specificity or true negative rate)                           1.0                     0.33333                 
TON(Test outcome negative)                                       7                       1                       
TOP(Test outcome positive)                                       1                       7                       
TP(True positive/hit)                                            1                       5                       
TPR(Sensitivity, recall, hit rate, or true positive rate)        0.33333                 1.0                     
Y(Youden index)                                                  0.33333                 0.33333                 
dInd(Distance index)                                             0.66667                 0.66667                 
sInd(Similarity index)                                           0.5286                  0.5286                                 
                                  
>>> cm3 = ConfusionMatrix(matrix={"Class1": {"Class1": 1, "Class2":0}, "Class2": {"Class1": 2, "Class2": 5}},transpose=True) # Transpose Matrix      
>>> cm3.print_matrix()
Predict          Class1    Class2    
Actual
Class1           1         2         

Class2           0         5         

```
* `matrix()` and `normalized_matrix()` renamed to `print_matrix()` and `print_normalized_matrix()` in `version 1.5`			

### Activation threshold
`threshold` is added in `version 0.9` for real value prediction.			
						
For more information visit [Example3](http://www.pycm.ir/doc/Example3.html "Example3")

### Load from file			
`file` is added in `version 0.9.5` in order to load saved confusion matrix with `.obj` format generated by `save_obj` method.

For more information visit [Example4](http://www.pycm.ir/doc/Example4.html "Example4")

### Sample weights
`sample_weight` is added in `version 1.2`

For more information visit [Example5](http://www.pycm.ir/doc/Example5.html "Example5")

### Transpose
`transpose` is added in `version 1.2` in order to transpose input matrix (only in `Direct CM` mode)

### Relabel		
`relabel` method is added in `version 1.5` in order to change ConfusionMatrix classnames.		

```pycon
>>> cm.relabel(mapping={0:"L1",1:"L2",2:"L3"})
>>> cm
pycm.ConfusionMatrix(classes: ['L1', 'L2', 'L3'])
```

### Online help

`online_help` function is added in `version 1.1` in order to open each statistics definition in web browser


```pycon

>>> from pycm import online_help
>>> online_help("J")
>>> online_help("SOA1(Landis & Koch)")
>>> online_help(2)

```
* List of items are available by calling `online_help()` (without argument)				

### Acceptable data types			
1. `actual_vector` : python `list` or numpy `array` of any stringable objects
2. `predict_vector` : python `list` or numpy `array` of any stringable objects
3. `matrix` : `dict`
4. `digit`: `int`	
5. `threshold` : `FunctionType (function or lambda)`	
6. `file` : `File object`
7. `sample_weight` : python `list` or numpy `array` of any stringable objects
8. `transpose` : `bool`

* Run `help(ConfusionMatrix)` for `ConfusionMatrix` object details



				

For more information visit [here](https://github.com/sepandhaghighi/pycm/tree/master/Document "Document")

<div align="center">

<a href="https://asciinema.org/a/171863" target="_blank"><img src="https://asciinema.org/a/171863.png" /></a>
</div>

## Issues & bug reports			

Just fill an issue and describe it. We'll check it ASAP!							
or send an email to [shaghighi@ce.sharif.edu](mailto:shaghighi@ce.sharif.edu "shaghighi@ce.sharif.edu"). 


## Todo	

Moved [here](https://github.com/sepandhaghighi/pycm/blob/master/TODO.md)

## Outputs	

1. [HTML](http://www.pycm.ir/test.html)
2. [CSV](https://github.com/sepandhaghighi/pycm/blob/master/Otherfiles/test.csv)
3. [PyCM](https://github.com/sepandhaghighi/pycm/blob/master/Otherfiles/test.pycm)			
4. [OBJ](https://github.com/sepandhaghighi/pycm/blob/master/Otherfiles/test.obj)	


## Dependencies

<a href="https://requires.io/github/sepandhaghighi/pycm/requirements/?branch=dev"><img src="https://requires.io/github/sepandhaghighi/pycm/requirements.svg?branch=dev" alt="Requirements Status" /></a>

## Contribution			

Changes and improvements are more than welcome! ❤️ Feel free to fork and open a pull request. Please make your changes in a specific branch and request to pull into `dev` 			

Remember to write a few tests for your code before sending pull requests. 



## References			

<blockquote>1- J. R. Landis, G. G. Koch, “The measurement of observer agreement for categorical data. Biometrics,” in International Biometric Society,  pp. 159–174, 1977. </blockquote>

<blockquote>2- D. M. W. Powers, “Evaluation: from precision, recall and f-measure to roc, informedness, markedness & correlation,” in Journal of Machine Learning Technologies, pp.37-63, 2011.</blockquote>


<blockquote>3-  C. Sammut, G. Webb, “Encyclopedia of Machine Learning” in Springer, 2011.</blockquote>

<blockquote>4- J. L. Fleiss, “Measuring nominal scale agreement among many raters,” in Psychological Bulletin, pp. 378-382. </blockquote>

<blockquote>5- D.G. Altman, “Practical Statistics for Medical Research,” in Chapman and Hall, 1990.</blockquote>

<blockquote>6- K. L. Gwet, “Computing inter-rater reliability and its variance in the presence of high agreement,” in The British Journal of Mathematical and Statistical Psychology, pp. 29–48, 2008.”</blockquote>

<blockquote>7- W. A. Scott, “Reliability of content analysis: The case of nominal scaling,” in Public Opinion Quarterly, pp. 321–325, 1955.</blockquote>

<blockquote>8- E. M. Bennett, R. Alpert, and A. C. Goldstein, “Communication through limited response questioning,” in The Public Opinion Quarterly, pp. 303–308, 1954.</blockquote>

<blockquote>9- D. V. Cicchetti, "Guidelines, criteria, and rules of thumb for evaluating normed and standardized assessment instruments in psychology," in Psychological Assessment, pp. 284–290, 1994.</blockquote>

<blockquote>10- R.B. Davies, "Algorithm AS155: The Distributions of a Linear Combination of χ2 Random Variables," in Journal of the Royal Statistical Society, pp. 323–333, 1980.</blockquote>

<blockquote>11- S. Kullback, R. A. Leibler "On information and sufficiency," in Annals of Mathematical Statistics, pp. 79–86, 1951.</blockquote>

<blockquote>12- L. A. Goodman, W. H. Kruskal, "Measures of Association for Cross Classifications, IV: Simplification of Asymptotic Variances," in Journal of the American Statistical Association, pp. 415–421, 1972.</blockquote>

<blockquote>13- L. A. Goodman, W. H. Kruskal, "Measures of Association for Cross Classifications III: Approximate Sampling Theory," in Journal of the American Statistical Association, pp.  310–364, 1963. </blockquote>

<blockquote>14- T. Byrt, J. Bishop and J. B. Carlin, “Bias, prevalence, and kappa,” in Journal of Clinical Epidemiology pp. 423-429, 1993.</blockquote>

<blockquote>15- M. Shepperd, D. Bowes, and T. Hall, “Researcher Bias: The Use of Machine Learning in Software Defect Prediction,” in IEEE Transactions on Software Engineering, pp. 603-616, 2014.</blockquote>

<blockquote>16- X. Deng, Q. Liu, Y. Deng, and S. Mahadevan, “An improved method to construct basic probability assignment based on the confusion matrix for classification problem, ” in Information Sciences, pp.250-261, 2016.</blockquote>

<blockquote>17- Wei, J.-M., Yuan, X.-Y., Hu, Q.-H., Wang, S.-Q.: A novel measure for evaluating
classifiers. Expert Systems with Applications, Vol 37, 3799–3809 (2010).</blockquote>

<blockquote>18- Kononenko I. and Bratko I. Information-based evaluation criterion for classifier’s
performance. Machine Learning, 6:67–80, 1991.</blockquote>

<blockquote>19- Delgado R., Núñez-González J.D. (2019) Enhancing Confusion Entropy as Measure for Evaluating Classifiers. In: Graña M. et al. (eds) International Joint Conference SOCO’18-CISIS’18-ICEUTE’18. SOCO’18-CISIS’18-ICEUTE’18 2018. Advances in Intelligent Systems and Computing, vol 771. Springer, Cham </blockquote>


<blockquote>20- Gorodkin J (2004) Comparing two K-category assignments by a K-category
correlation coefficient. Computational Biology and Chemistry 28: 367–374 </blockquote>

<blockquote>21- Freitas C.O.A., de Carvalho J.M., Oliveira J., Aires S.B.K., Sabourin R. (2007) Confusion Matrix Disagreement for Multiple Classifiers. In: Rueda L., Mery D., Kittler J. (eds) Progress in Pattern Recognition, Image Analysis and Applications. CIARP 2007. Lecture Notes in Computer Science, vol 4756. Springer, Berlin, Heidelberg</blockquote>

<blockquote>22- Branco P., Torgo L., Ribeiro R.P. (2017) Relevance-Based Evaluation Metrics for Multi-class Imbalanced Domains. In: Kim J., Shim K., Cao L., Lee JG., Lin X., Moon YS. (eds) Advances in Knowledge Discovery and Data Mining. PAKDD 2017. Lecture Notes in Computer Science, vol 10234. Springer, Cham</blockquote>

<blockquote>23- Ballabio, D., Grisoni, F. and Todeschini, R. (2018). Multivariate comparison of classification performance measures. Chemometrics and Intelligent Laboratory Systems, 174, pp.33-44.</blockquote>

<blockquote>24- Cohen, Jacob. 1960. A coefficient of agreement for nominal scales. Educational And Psychological Measurement 20:37-46</blockquote>

<blockquote>25- Siegel, Sidney and N. John Castellan, Jr. 1988. Nonparametric Statistics for the Behavioral Sciences. McGraw Hill.</blockquote>

<blockquote>26- Cramér, Harald. 1946. Mathematical Methods of Statistics. Princeton: Princeton University Press, page 282 (Chapter 21. The two-dimensional case)</blockquote>

<blockquote>27- Matthews, B. W. (1975). "Comparison of the predicted and observed secondary structure of T4 phage lysozyme". Biochimica et Biophysica Acta (BBA) - Protein Structure. 405 (2): 442–451.</blockquote>

<blockquote>28- Swets JA. (1973). "The relative operating characteristic in Psychology". Science. 182 (14116): 990–1000.</blockquote> 

<blockquote>29- Jaccard, Paul (1901), "Étude comparative de la distribution florale dans une portion des Alpes et des Jura", Bulletin de la Société Vaudoise des Sciences Naturelles, 37: 547–579.</blockquote> 

<blockquote>30- Thomas M. Cover and Joy A. Thomas. 2006. Elements of Information Theory (Wiley Series in Telecommunications and Signal Processing). Wiley-Interscience, New York, NY, USA.</blockquote> 

<blockquote>31- Keeping, E.S. (1962) Introduction to Statistical Inference. D. Van Nostrand, Princeton, NJ.</blockquote>

<blockquote>32- Sindhwani V, Bhattacharge P, Rakshit S (2001) Information theoretic feature
crediting in multiclass Support Vector Machines. In: Grossman R, Kumar V,
editors, Proceedings First SIAM International Conference on Data Mining,
ICDM01. SIAM, pp. 1–18. </blockquote> 

<blockquote>33- Bekkar, Mohamed & Djema, Hassiba & Alitouche, T.A.. (2013). Evaluation measures for models assessment over imbalanced data sets. Journal of Information Engineering and Applications. 3. 27-38. </blockquote>

<blockquote>34- Youden W, (1950),« Index for rating diagnostic tests »; Cancer, 3 :32–35 </blockquote>


<blockquote>35- S. Brin, R. Motwani, J. D. Ullman, and S. Tsur. Dynamic itemset counting and implication rules for market basket data. In Proc. of the ACM SIGMOD Int'l Conf. on Management of Data (ACM SIGMOD '97), pages 265-276, 1997.</blockquote> 

<blockquote>36- Raschka, Sebastian (2018) MLxtend: Providing machine learning and data science utilities and extensions to Python's scientific computing stack. J Open Source Softw 3(24).</blockquote> 


## Cite

If you use PyCM in your research , please cite this JOSS paper :

<pre>
Haghighi, S., Jasemi, M., Hessabi, S. and Zolanvari, A. (2018). PyCM: Multiclass confusion matrix library in Python. Journal of Open Source Software, 3(25), p.729.
</pre>
<pre>

@article{Haghighi2018,
  doi = {10.21105/joss.00729},
  url = {https://doi.org/10.21105/joss.00729},
  year  = {2018},
  month = {may},
  publisher = {The Open Journal},
  volume = {3},
  number = {25},
  pages = {729},
  author = {Sepand Haghighi and Masoomeh Jasemi and Shaahin Hessabi and Alireza Zolanvari},
  title = {{PyCM}: Multiclass confusion matrix library in Python},
  journal = {Journal of Open Source Software}
}


</pre>

Download [PyCM.bib](http://www.pycm.ir/PYCM.bib)	


<table>
	<tr> 
		<td align="center">JOSS</td>
		<td align="center"><a href="https://doi.org/10.21105/joss.00729"><img src="http://joss.theoj.org/papers/10.21105/joss.00729/status.svg"></a></td>	
	</tr>
	<tr>
		<td align="center">Zenodo</td>
		<td align="center"><a href="https://doi.org/10.5281/zenodo.1157173"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.1157173.svg" alt="DOI"></a></td>
	</tr>
	<tr>
		<td align="center">Researchgate</td>
		<td align="center"><a href="https://www.researchgate.net/project/PYCM-python-confusion-matrix"><img src="https://img.shields.io/badge/Researchgate-PyCM-yellow.svg"></a></td>
	</tr>
</table>
				


## License

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fsepandhaghighi%2Fpycm.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fsepandhaghighi%2Fpycm?ref=badge_large)


## Donate to our project		

If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .

<a href="http://www.pycm.ir/donate.html" target="_blank"><img src="http://www.pycm.ir/images/Donate-Button.png" height="90px" width="270px" alt="PyCM Donation"></a>


