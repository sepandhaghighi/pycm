<div align="center">
<img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/logo.png">
<br/>
<br/>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>
<a href="/Document"><img src="https://img.shields.io/badge/doc-latest-orange.svg"></a>
<a href="https://codecov.io/gh/sepandhaghighi/pycm">
  <img src="https://codecov.io/gh/sepandhaghighi/pycm/branch/master/graph/badge.svg" />
</a>
<a href="https://badge.fury.io/py/pycm"><img src="https://badge.fury.io/py/pycm.svg" alt="PyPI version" height="18"></a>
<a href="https://anaconda.org/sepandhaghighi/pycm"><img src="https://anaconda.org/sepandhaghighi/pycm/badges/version.svg"></a>
<a href = "https://hub.docker.com/r/sepandhaghighi/pycm"><img alt="Docker Cloud Build Status" src="https://img.shields.io/docker/cloud/build/sepandhaghighi/pycm"></a>
</div>

----------
## Table of contents					
   * [Overview](https://github.com/sepandhaghighi/pycm#overview)
   * [Installation](https://github.com/sepandhaghighi/pycm#installation)
   * [Usage](https://github.com/sepandhaghighi/pycm#usage)
   * [Document](https://github.com/sepandhaghighi/pycm/tree/master/Document)
   * [Try PyCM in Your Browser](https://github.com/sepandhaghighi/pycm#try-pycm-in-your-browser)
   * [Issues & Bug Reports](https://github.com/sepandhaghighi/pycm#issues--bug-reports)
   * [Todo](https://github.com/sepandhaghighi/pycm/blob/master/TODO.md)
   * [Outputs](https://github.com/sepandhaghighi/pycm#outputs)
   * [Dependencies](https://github.com/sepandhaghighi/pycm#dependencies)
   * [Contribution](https://github.com/sepandhaghighi/pycm/blob/master/.github/CONTRIBUTING.md)
   * [References](https://github.com/sepandhaghighi/pycm#references)
   * [Cite](https://github.com/sepandhaghighi/pycm#cite)
   * [Support](https://github.com/sepandhaghighi/pycm#support)
   * [Authors](https://github.com/sepandhaghighi/pycm/blob/master/AUTHORS.md)
   * [License](https://github.com/sepandhaghighi/pycm#license)
   * [Donate](https://github.com/sepandhaghighi/pycm#donate-to-our-project)
   * [Changelog](https://github.com/sepandhaghighi/pycm/blob/master/CHANGELOG.md)
   * [Code of Conduct](https://github.com/sepandhaghighi/pycm/blob/master/.github/CODE_OF_CONDUCT.md)

## Overview

<p align="justify">	
PyCM is a multi-class confusion matrix library written in Python that supports both input data vectors and direct matrix, and a proper tool for post-classification model evaluation that supports most classes and overall statistics parameters.	
PyCM is the swiss-army knife of confusion matrices, targeted mainly at data scientists that need a broad array of metrics for predictive models and accurate evaluation of a large variety of classifiers.

</p>

<div align="center">
<img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/block_diagram.jpg">
<p>Fig1. ConfusionMatrix Block Diagram</p>
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

⚠️  PyCM 2.4 is the last version to support **Python 2.7** & **Python 3.4**

⚠️  Plotting capability requires **Matplotlib (>= 3.0.0)** or **Seaborn (>= 0.9.1)**   

### Source code
- Download [Version 3.0](https://github.com/sepandhaghighi/pycm/archive/v3.0.zip) or [Latest Source ](https://github.com/sepandhaghighi/pycm/archive/dev.zip)
- Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- Run `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install pycm==3.0` or `pip3 install pycm==3.0` (Need root access)

### Conda

- Check [Conda Managing Package](https://conda.io/)
- `conda install -c sepandhaghighi pycm` (Need root access)

### Easy install

- Run `easy_install --upgrade pycm` (Need root access)

### MATLAB

- Download and install [MATLAB](https://www.mathworks.com/products/matlab.html) (>=8.5, 64/32 bit)
- Download and install [Python3.x](https://www.python.org/downloads/) (>=3.5, 64/32 bit) 
	- [x] Select `Add to PATH` option
	- [x] Select `Install pip` option
- Run `pip install pycm` or `pip3 install pycm` (Need root access)
- Configure Python interpreter
```matlab
>> pyversion PYTHON_EXECUTABLE_FULL_PATH
```
- Visit [MATLAB Examples](https://github.com/sepandhaghighi/pycm/tree/master/MATLAB)	

### Docker	

- Run `docker pull sepandhaghighi/pycm` (Need root access)
- Configuration :
	- Ubuntu 16.04
	- Python 3.6


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
Predict 0       1       2       
Actual
0       3       0       0       

1       0       1       2       

2       2       1       3       





Overall Statistics : 

95% CI                                                            (0.30439,0.86228)
ACC Macro                                                         0.72222
ARI                                                               0.09206
AUNP                                                              0.66667
AUNU                                                              0.69444
Bangdiwala B                                                      0.37255
Bennett S                                                         0.375
CBA                                                               0.47778
CSI                                                               0.17778
Chi-Squared                                                       6.6
Chi-Squared DF                                                    4
Conditional Entropy                                               0.95915
Cramer V                                                          0.5244
Cross Entropy                                                     1.59352
F1 Macro                                                          0.56515
F1 Micro                                                          0.58333
FNR Macro                                                         0.38889
FNR Micro                                                         0.41667
FPR Macro                                                         0.22222
FPR Micro                                                         0.20833
Gwet AC1                                                          0.38931
Hamming Loss                                                      0.41667
Joint Entropy                                                     2.45915
KL Divergence                                                     0.09352
Kappa                                                             0.35484
Kappa 95% CI                                                      (-0.07708,0.78675)
Kappa No Prevalence                                               0.16667
Kappa Standard Error                                              0.22036
Kappa Unbiased                                                    0.34426
Krippendorff Alpha                                                0.37158
Lambda A                                                          0.16667
Lambda B                                                          0.42857
Mutual Information                                                0.52421
NIR                                                               0.5
Overall ACC                                                       0.58333
Overall CEN                                                       0.46381
Overall J                                                         (1.225,0.40833)
Overall MCC                                                       0.36667
Overall MCEN                                                      0.51894
Overall RACC                                                      0.35417
Overall RACCU                                                     0.36458
P-Value                                                           0.38721
PPV Macro                                                         0.56667
PPV Micro                                                         0.58333
Pearson C                                                         0.59568
Phi-Squared                                                       0.55
RCI                                                               0.34947
RR                                                                4.0
Reference Entropy                                                 1.5
Response Entropy                                                  1.48336
SOA1(Landis & Koch)                                               Fair
SOA2(Fleiss)                                                      Poor
SOA3(Altman)                                                      Fair
SOA4(Cicchetti)                                                   Poor
SOA5(Cramer)                                                      Relatively Strong
SOA6(Matthews)                                                    Weak
Scott PI                                                          0.34426
Standard Error                                                    0.14232
TNR Macro                                                         0.77778
TNR Micro                                                         0.79167
TPR Macro                                                         0.61111
TPR Micro                                                         0.58333
Zero-one Loss                                                     5

Class Statistics :

Classes                                                           0             1             2             
ACC(Accuracy)                                                     0.83333       0.75          0.58333       
AGF(Adjusted F-score)                                             0.9136        0.53995       0.5516        
AGM(Adjusted geometric mean)                                      0.83729       0.692         0.60712       
AM(Difference between automatic and manual classification)        2             -1            -1            
AUC(Area under the ROC curve)                                     0.88889       0.61111       0.58333       
AUCI(AUC value interpretation)                                    Very Good     Fair          Poor          
AUPR(Area under the PR curve)                                     0.8           0.41667       0.55          
BCD(Bray-Curtis dissimilarity)                                    0.08333       0.04167       0.04167       
BM(Informedness or bookmaker informedness)                        0.77778       0.22222       0.16667       
CEN(Confusion entropy)                                            0.25          0.49658       0.60442       
DOR(Diagnostic odds ratio)                                        None          4.0           2.0           
DP(Discriminant power)                                            None          0.33193       0.16597       
DPI(Discriminant power interpretation)                            None          Poor          Poor          
ERR(Error rate)                                                   0.16667       0.25          0.41667       
F0.5(F0.5 score)                                                  0.65217       0.45455       0.57692       
F1(F1 score - harmonic mean of precision and sensitivity)         0.75          0.4           0.54545       
F2(F2 score)                                                      0.88235       0.35714       0.51724       
FDR(False discovery rate)                                         0.4           0.5           0.4           
FN(False negative/miss/type 2 error)                              0             2             3             
FNR(Miss rate or false negative rate)                             0.0           0.66667       0.5           
FOR(False omission rate)                                          0.0           0.2           0.42857       
FP(False positive/type 1 error/false alarm)                       2             1             2             
FPR(Fall-out or false positive rate)                              0.22222       0.11111       0.33333       
G(G-measure geometric mean of precision and sensitivity)          0.7746        0.40825       0.54772       
GI(Gini index)                                                    0.77778       0.22222       0.16667       
GM(G-mean geometric mean of specificity and sensitivity)          0.88192       0.54433       0.57735       
IBA(Index of balanced accuracy)                                   0.95062       0.13169       0.27778       
ICSI(Individual classification success index)                     0.6           -0.16667      0.1           
IS(Information score)                                             1.26303       1.0           0.26303       
J(Jaccard index)                                                  0.6           0.25          0.375         
LS(Lift score)                                                    2.4           2.0           1.2           
MCC(Matthews correlation coefficient)                             0.68313       0.2582        0.16903       
MCCI(Matthews correlation coefficient interpretation)             Moderate      Negligible    Negligible    
MCEN(Modified confusion entropy)                                  0.26439       0.5           0.6875        
MK(Markedness)                                                    0.6           0.3           0.17143       
N(Condition negative)                                             9             9             6             
NLR(Negative likelihood ratio)                                    0.0           0.75          0.75          
NLRI(Negative likelihood ratio interpretation)                    Good          Negligible    Negligible    
NPV(Negative predictive value)                                    1.0           0.8           0.57143       
OC(Overlap coefficient)                                           1.0           0.5           0.6           
OOC(Otsuka-Ochiai coefficient)                                    0.7746        0.40825       0.54772       
OP(Optimized precision)                                           0.70833       0.29545       0.44048       
P(Condition positive or support)                                  3             3             6             
PLR(Positive likelihood ratio)                                    4.5           3.0           1.5           
PLRI(Positive likelihood ratio interpretation)                    Poor          Poor          Poor          
POP(Population)                                                   12            12            12            
PPV(Precision or positive predictive value)                       0.6           0.5           0.6           
PRE(Prevalence)                                                   0.25          0.25          0.5           
Q(Yule Q - coefficient of colligation)                            None          0.6           0.33333       
QI(Yule Q interpretation)                                         None          Moderate      Weak          
RACC(Random accuracy)                                             0.10417       0.04167       0.20833       
RACCU(Random accuracy unbiased)                                   0.11111       0.0434        0.21007       
TN(True negative/correct rejection)                               7             8             4             
TNR(Specificity or true negative rate)                            0.77778       0.88889       0.66667       
TON(Test outcome negative)                                        7             10            7             
TOP(Test outcome positive)                                        5             2             5             
TP(True positive/hit)                                             3             1             3             
TPR(Sensitivity, recall, hit rate, or true positive rate)         1.0           0.33333       0.5           
Y(Youden index)                                                   0.77778       0.22222       0.16667       
dInd(Distance index)                                              0.22222       0.67586       0.60093       
sInd(Similarity index)                                            0.84287       0.52209       0.57508

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
Predict      Class1       Class2       
Actual
Class1       1            2            

Class2       0            5            





Overall Statistics : 

95% CI                                                            (0.44994,1.05006)
ACC Macro                                                         0.75
ARI                                                               0.17241
AUNP                                                              0.66667
AUNU                                                              0.66667
Bangdiwala B                                                      0.68421
Bennett S                                                         0.5
CBA                                                               0.52381
CSI                                                               0.52381
Chi-Squared                                                       1.90476
Chi-Squared DF                                                    1
Conditional Entropy                                               0.34436
Cramer V                                                          0.48795
Cross Entropy                                                     1.2454
F1 Macro                                                          0.66667
F1 Micro                                                          0.75
FNR Macro                                                         0.33333
FNR Micro                                                         0.25
FPR Macro                                                         0.33333
FPR Micro                                                         0.25
Gwet AC1                                                          0.6
Hamming Loss                                                      0.25
Joint Entropy                                                     1.29879
KL Divergence                                                     0.29097
Kappa                                                             0.38462
Kappa 95% CI                                                      (-0.354,1.12323)
Kappa No Prevalence                                               0.5
Kappa Standard Error                                              0.37684
Kappa Unbiased                                                    0.33333
Krippendorff Alpha                                                0.375
Lambda A                                                          0.33333
Lambda B                                                          0.0
Mutual Information                                                0.1992
NIR                                                               0.625
Overall ACC                                                       0.75
Overall CEN                                                       0.44812
Overall J                                                         (1.04762,0.52381)
Overall MCC                                                       0.48795
Overall MCEN                                                      0.29904
Overall RACC                                                      0.59375
Overall RACCU                                                     0.625
P-Value                                                           0.36974
PPV Macro                                                         0.85714
PPV Micro                                                         0.75
Pearson C                                                         0.43853
Phi-Squared                                                       0.2381
RCI                                                               0.20871
RR                                                                4.0
Reference Entropy                                                 0.95443
Response Entropy                                                  0.54356
SOA1(Landis & Koch)                                               Fair
SOA2(Fleiss)                                                      Poor
SOA3(Altman)                                                      Fair
SOA4(Cicchetti)                                                   Poor
SOA5(Cramer)                                                      Relatively Strong
SOA6(Matthews)                                                    Weak
Scott PI                                                          0.33333
Standard Error                                                    0.15309
TNR Macro                                                         0.66667
TNR Micro                                                         0.75
TPR Macro                                                         0.66667
TPR Micro                                                         0.75
Zero-one Loss                                                     2

Class Statistics :

Classes                                                           Class1        Class2        
ACC(Accuracy)                                                     0.75          0.75          
AGF(Adjusted F-score)                                             0.53979       0.81325       
AGM(Adjusted geometric mean)                                      0.73991       0.5108        
AM(Difference between automatic and manual classification)        -2            2             
AUC(Area under the ROC curve)                                     0.66667       0.66667       
AUCI(AUC value interpretation)                                    Fair          Fair          
AUPR(Area under the PR curve)                                     0.66667       0.85714       
BCD(Bray-Curtis dissimilarity)                                    0.125         0.125         
BM(Informedness or bookmaker informedness)                        0.33333       0.33333       
CEN(Confusion entropy)                                            0.5           0.43083       
DOR(Diagnostic odds ratio)                                        None          None          
DP(Discriminant power)                                            None          None          
DPI(Discriminant power interpretation)                            None          None          
ERR(Error rate)                                                   0.25          0.25          
F0.5(F0.5 score)                                                  0.71429       0.75758       
F1(F1 score - harmonic mean of precision and sensitivity)         0.5           0.83333       
F2(F2 score)                                                      0.38462       0.92593       
FDR(False discovery rate)                                         0.0           0.28571       
FN(False negative/miss/type 2 error)                              2             0             
FNR(Miss rate or false negative rate)                             0.66667       0.0           
FOR(False omission rate)                                          0.28571       0.0           
FP(False positive/type 1 error/false alarm)                       0             2             
FPR(Fall-out or false positive rate)                              0.0           0.66667       
G(G-measure geometric mean of precision and sensitivity)          0.57735       0.84515       
GI(Gini index)                                                    0.33333       0.33333       
GM(G-mean geometric mean of specificity and sensitivity)          0.57735       0.57735       
IBA(Index of balanced accuracy)                                   0.11111       0.55556       
ICSI(Individual classification success index)                     0.33333       0.71429       
IS(Information score)                                             1.41504       0.19265       
J(Jaccard index)                                                  0.33333       0.71429       
LS(Lift score)                                                    2.66667       1.14286       
MCC(Matthews correlation coefficient)                             0.48795       0.48795       
MCCI(Matthews correlation coefficient interpretation)             Weak          Weak          
MCEN(Modified confusion entropy)                                  0.38998       0.51639       
MK(Markedness)                                                    0.71429       0.71429       
N(Condition negative)                                             5             3             
NLR(Negative likelihood ratio)                                    0.66667       0.0           
NLRI(Negative likelihood ratio interpretation)                    Negligible    Good          
NPV(Negative predictive value)                                    0.71429       1.0           
OC(Overlap coefficient)                                           1.0           1.0           
OOC(Otsuka-Ochiai coefficient)                                    0.57735       0.84515       
OP(Optimized precision)                                           0.25          0.25          
P(Condition positive or support)                                  3             5             
PLR(Positive likelihood ratio)                                    None          1.5           
PLRI(Positive likelihood ratio interpretation)                    None          Poor          
POP(Population)                                                   8             8             
PPV(Precision or positive predictive value)                       1.0           0.71429       
PRE(Prevalence)                                                   0.375         0.625         
Q(Yule Q - coefficient of colligation)                            None          None          
QI(Yule Q interpretation)                                         None          None          
RACC(Random accuracy)                                             0.04688       0.54688       
RACCU(Random accuracy unbiased)                                   0.0625        0.5625        
TN(True negative/correct rejection)                               5             1             
TNR(Specificity or true negative rate)                            1.0           0.33333       
TON(Test outcome negative)                                        7             1             
TOP(Test outcome positive)                                        1             7             
TP(True positive/hit)                                             1             5             
TPR(Sensitivity, recall, hit rate, or true positive rate)         0.33333       1.0           
Y(Youden index)                                                   0.33333       0.33333       
dInd(Distance index)                                              0.66667       0.66667       
sInd(Similarity index)                                            0.5286        0.5286
   
>>> cm2.stat(summary=True)
Overall Statistics : 

ACC Macro                                                         0.75
F1 Macro                                                          0.66667
FPR Macro                                                         0.33333
Kappa                                                             0.38462
Overall ACC                                                       0.75
PPV Macro                                                         0.85714
SOA1(Landis & Koch)                                               Fair
TPR Macro                                                         0.66667
Zero-one Loss                                                     2

Class Statistics :

Classes                                                           Class1        Class2        
ACC(Accuracy)                                                     0.75          0.75          
AUC(Area under the ROC curve)                                     0.66667       0.66667       
AUCI(AUC value interpretation)                                    Fair          Fair          
F1(F1 score - harmonic mean of precision and sensitivity)         0.5           0.83333       
FN(False negative/miss/type 2 error)                              2             0             
FP(False positive/type 1 error/false alarm)                       0             2             
FPR(Fall-out or false positive rate)                              0.0           0.66667       
N(Condition negative)                                             5             3             
P(Condition positive or support)                                  3             5             
POP(Population)                                                   8             8             
PPV(Precision or positive predictive value)                       1.0           0.71429       
TN(True negative/correct rejection)                               5             1             
TON(Test outcome negative)                                        7             1             
TOP(Test outcome positive)                                        1             7             
TP(True positive/hit)                                             1             5             
TPR(Sensitivity, recall, hit rate, or true positive rate)         0.33333       1.0 
                               
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

### Position		
`position` method is added in `version 2.8` in order to find the indexes of observations in `predict_vector` which made TP, TN, FP, FN.	

```pycon
>>> cm.position()
{0: {'FN': [], 'FP': [0, 7], 'TP': [1, 4, 9], 'TN': [2, 3, 5, 6, 8, 10, 11]}, 1: {'FN': [5, 10], 'FP': [3], 'TP': [6], 'TN': [0, 1, 2, 4, 7, 8, 9, 11]}, 2: {'FN': [0, 3, 7], 'FP': [5, 10], 'TP': [2, 8, 11], 'TN': [1, 4, 6, 9]}}
```

### To array
`to_array` method is added in `version 2.9` in order to returns the confusion matrix in the form of a NumPy array. This can be helpful to apply different operations over the confusion matrix for different purposes such as aggregation, normalization, and combination.

```pycon
>>> cm.to_array()
array([[3, 0, 0],
       [0, 1, 2],
       [2, 1, 3]])
>>> cm.to_array(normalized=True)
array([[1.     , 0.     , 0.     ],
       [0.     , 0.33333, 0.66667],
       [0.33333, 0.16667, 0.5    ]])
>>> cm.to_array(normalized=True,one_vs_all=True, class_name="L1")
array([[1.     , 0.     ],
       [0.22222, 0.77778]])
```

### Combine
`combine` method is added in `version 3.0` in order to merge two confusion matrices. This option will be useful in mini-batch learning.	

```pycon
>>> cm_combined = cm2.combine(cm3)
>>> cm_combined.print_matrix()
Predict      Class1       Class2       
Actual
Class1       2            4            

Class2       0            10           

```	

### Plot
`plot` method is added in `version 3.0` in order to plot a confusion matrix using Matplotlib or Seaborn.

```pycon
>>> cm.plot()
```
<img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/plot1.png">	

```pycon
>>> from matplotlib import pyplot as plt
>>> cm.plot(cmap=plt.cm.Greens,number_label=True,plot_lib="matplotlib")
```		

<img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/plot2.png">		

```pycon
>>> cm.plot(cmap=plt.cm.Reds,normalized=True,number_label=True,plot_lib="seaborn")
```		

<img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/plot3.png">

### Online help

`online_help` function is added in `version 1.1` in order to open each statistics definition in web browser


```pycon

>>> from pycm import online_help
>>> online_help("J")
>>> online_help("SOA1(Landis & Koch)")
>>> online_help(2)

```
* List of items are available by calling `online_help()` (without argument)		
* If PyCM website is not available, set `alt_link = True` (new in `version 2.4`)

### Parameter recommender

This option has been added in `version 1.9` to recommend the most related parameters considering the characteristics of the input dataset. 
The suggested parameters are selected according to some characteristics of the input such as being balance/imbalance and binary/multi-class.
All suggestions can be categorized into three main groups: imbalanced dataset, binary classification for a balanced dataset, and multi-class classification for a balanced dataset. 
The recommendation lists have been gathered according to the respective paper of each parameter and the capabilities which had been claimed by the paper.

```pycon
>>> cm.imbalance
False
>>> cm.binary
False
>>> cm.recommended_list
['MCC', 'TPR Micro', 'ACC', 'PPV Macro', 'BCD', 'Overall MCC', 'Hamming Loss', 'TPR Macro', 'Zero-one Loss', 'ERR', 'PPV Micro', 'Overall ACC']

```	

### Compare

In `version 2.0`, a method for comparing several confusion matrices is introduced. This option is a combination of several overall and class-based benchmarks. Each of the benchmarks evaluates the performance of the classification algorithm from good to poor and give them a numeric score. The score of good and poor performances are 1 and 0, respectively.

After that, two scores are calculated for each confusion matrices, overall and class-based. The overall score is the average of the score of six overall benchmarks which are Landis & Koch, Fleiss, Altman, Cicchetti, Cramer, and Matthews. In the same manner, the class-based score is the average of the score of six class-based benchmarks which are Positive Likelihood Ratio Interpretation, Negative Likelihood Ratio Interpretation, Discriminant Power Interpretation, AUC value Interpretation, Matthews Correlation Coefficient Interpretation and Yule's Q Interpretation. It should be noticed that if one of the benchmarks returns none for one of the classes, that benchmarks will be eliminated in total averaging. If the user sets weights for the classes, the averaging over the value of class-based benchmark scores will transform to a weighted average.

If the user sets the value of `by_class` boolean input `True`, the best confusion matrix is the one with the maximum class-based score. Otherwise, if a confusion matrix obtains the maximum of both overall and class-based scores, that will be reported as the best confusion matrix, but in any other case, the compared object doesn’t select the best confusion matrix.


```pycon
>>> cm2 = ConfusionMatrix(matrix={0:{0:2,1:50,2:6},1:{0:5,1:50,2:3},2:{0:1,1:7,2:50}})
>>> cm3 = ConfusionMatrix(matrix={0:{0:50,1:2,2:6},1:{0:50,1:5,2:3},2:{0:1,1:55,2:2}})
>>> cp = Compare({"cm2":cm2,"cm3":cm3})
>>> print(cp)
Best : cm2

Rank  Name   Class-Score    Overall-Score
1     cm2    9.05           2.55
2     cm3    6.05           1.98333

>>> cp.best
pycm.ConfusionMatrix(classes: [0, 1, 2])
>>> cp.sorted
['cm2', 'cm3']
>>> cp.best_name
'cm2'
```	

### Acceptable data types	

#### ConfusionMatrix

		
1. `actual_vector` : python `list` or numpy `array` of any stringable objects
2. `predict_vector` : python `list` or numpy `array` of any stringable objects
3. `matrix` : `dict`
4. `digit`: `int`	
5. `threshold` : `FunctionType (function or lambda)`	
6. `file` : `File object`
7. `sample_weight` : python `list` or numpy `array` of numbers
8. `transpose` : `bool`

* Run `help(ConfusionMatrix)` for `ConfusionMatrix` object details

#### Compare

1. `cm_dict` : python `dict` of `ConfusionMatrix` object (`str` : `ConfusionMatrix`)
2. `by_class` : `bool`
3. `weight` : python `dict` of class weights (`class_name` : `float`)
4. `digit`: `int`

* Run `help(Compare)` for `Compare` object details


For more information visit [here](https://github.com/sepandhaghighi/pycm/tree/master/Document "Document")

<div align="center">

<a href="https://asciinema.org/a/171863" target="_blank"><img src="https://asciinema.org/a/171863.png" /></a>
</div>

## Try PyCM in your browser!
PyCM can be used online in interactive Jupyter Notebooks via the Binder service! Try it out now! :

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sepandhaghighi/pycm/master)

* Check `Examples` in `Document` folder 

## Issues & bug reports			

Just fill an issue and describe it. We'll check it ASAP!							
or send an email to [info@pycm.ir](mailto:info@pycm.ir "info@pycm.ir"). 

* Please complete the issue template


## Outputs	

1. [HTML](http://www.pycm.ir/test.html)
2. [CSV](https://github.com/sepandhaghighi/pycm/blob/master/Otherfiles/test.csv)
3. [PyCM](https://github.com/sepandhaghighi/pycm/blob/master/Otherfiles/test.pycm)			
4. [OBJ](https://github.com/sepandhaghighi/pycm/blob/master/Otherfiles/test.obj)	
5. [COMP](https://github.com/sepandhaghighi/pycm/blob/master/Otherfiles/test.comp)


## Dependencies

<table>
	<tr> 
		<td align="center">master</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center"><a href="https://requires.io/github/sepandhaghighi/pycm/requirements/?branch=master"><img src="https://requires.io/github/sepandhaghighi/pycm/requirements.svg?branch=master" alt="Requirements Status" /></a></td>
		<td align="center"><a href="https://requires.io/github/sepandhaghighi/pycm/requirements/?branch=dev"><img src="https://requires.io/github/sepandhaghighi/pycm/requirements.svg?branch=dev" alt="Requirements Status" /></a></td>
	</tr>
</table>


## References			

<blockquote>1- J. R. Landis, G. G. Koch, “The measurement of observer agreement for categorical data. Biometrics,” in International Biometric Society,  pp. 159–174, 1977. </blockquote>

<blockquote>2- D. M. W. Powers, “Evaluation: from precision, recall and f-measure to roc, informedness, markedness & correlation,” in Journal of Machine Learning Technologies, pp.37-63, 2011.</blockquote>


<blockquote>3-  C. Sammut, G. Webb, “Encyclopedia of Machine Learning” in Springer, 2011.</blockquote>

<blockquote>4- J. L. Fleiss, “Measuring nominal scale agreement among many raters,” in Psychological Bulletin, pp. 378-382, 1971. </blockquote>

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

<blockquote>17- J.-M. Wei, X.-J. Yuan, Q.-H. Hu, and S.-Q. J. E. S. w. A. Wang, "A novel measure for evaluating classifiers," in Expert Systems with Applications, pp. 3799-3809, 2010.</blockquote>

<blockquote>18- I. Kononenko and I. J. M. L. Bratko, "Information-based evaluation criterion for classifier's performance," in Machine Learning, pp. 67-80, 1991.</blockquote>

<blockquote>19- R. Delgado and J. D. Núñez-González, "Enhancing Confusion Entropy as Measure for Evaluating Classifiers," in The 13th International Conference on Soft Computing Models in Industrial and Environmental Applications, pp. 79-89, 2018: Springer.</blockquote>

<blockquote>20- J. J. C. b. Gorodkin and chemistry, "Comparing two K-category assignments by a K-category correlation coefficient," in Computational Biology and chemistry, pp. 367-374, 2004.</blockquote>

<blockquote>21- C. O. Freitas, J. M. De Carvalho, J. Oliveira, S. B. Aires, and R. Sabourin, "Confusion matrix disagreement for multiple classifiers," in Iberoamerican Congress on Pattern Recognition, pp. 387-396, 2007.</blockquote>

<blockquote>22- P. Branco, L. Torgo, and R. P. Ribeiro, "Relevance-based evaluation metrics for multi-class imbalanced domains," in Pacific-Asia Conference on Knowledge Discovery and Data Mining, pp. 698-710, 2017. Springer.</blockquote>

<blockquote>23- D. Ballabio, F. Grisoni, R. J. C. Todeschini, and I. L. Systems, "Multivariate comparison of classification performance measures," in Chemometrics and Intelligent Laboratory Systems, pp. 33-44, 2018.</blockquote>

<blockquote>24- J. J. E. Cohen and p. measurement, "A coefficient of agreement for nominal scales," in Educational and Psychological Measurement, pp. 37-46, 1960.</blockquote>

<blockquote>25- S. Siegel, "Nonparametric statistics for the behavioral sciences," in 	New York : McGraw-Hill, 1956.</blockquote>

<blockquote>26- H. Cramér, "Mathematical methods of statistics (PMS-9),"in Princeton university press, 2016.</blockquote>

<blockquote>27- B. W. J. B. e. B. A.-P. S. Matthews, "Comparison of the predicted and observed secondary structure of T4 phage lysozyme," in Biochimica et Biophysica Acta (BBA) - Protein Structure, pp. 442-451, 1975.</blockquote>

<blockquote>28- J. A. J. S. Swets, "The relative operating characteristic in psychology: a technique for isolating effects of response bias finds wide use in the study of perception and cognition," in American Association for the Advancement of Science, pp. 990-1000, 1973.</blockquote> 

<blockquote>29- P. J. B. S. V. S. N. Jaccard, "Étude comparative de la distribution florale dans une portion des Alpes et des Jura," in Bulletin de la Société vaudoise des sciences naturelles, pp. 547-579, 1901.</blockquote> 

<blockquote>30- T. M. Cover and J. A. Thomas, "Elements of information theory," in John Wiley & Sons, 2012.</blockquote> 

<blockquote>31- E. S. Keeping, "Introduction to statistical inference," in Courier Corporation, 1995.</blockquote>

<blockquote>32- V. Sindhwani, P. Bhattacharya, and S. Rakshit, "Information theoretic feature crediting in multiclass support vector machines," in Proceedings of the 2001 SIAM International Conference on Data Mining, pp. 1-18, 2001.</blockquote> 

<blockquote>33- M. Bekkar, H. K. Djemaa, and T. A. J. J. I. E. A. Alitouche, "Evaluation measures for models assessment over imbalanced data sets," in Journal of Information Engineering and Applications, 2013.</blockquote>

<blockquote>34- W. J. J. C. Youden, "Index for rating diagnostic tests," in Cancer, pp. 32-35, 1950.</blockquote>

<blockquote>35- S. Brin, R. Motwani, J. D. Ullman, and S. J. A. S. R. Tsur, "Dynamic itemset counting and implication rules for market basket data," in Proceedings of the 1997 ACM SIGMOD international conference on Management of datavol, pp. 255-264, 1997.</blockquote> 

<blockquote>36- S. J. T. J. o. O. S. S. Raschka, "MLxtend: Providing machine learning and data science utilities and extensions to Python’s scientific computing stack," in Journal of Open Source Software, 2018.</blockquote> 

<blockquote>37- J. BRAy and J. CuRTIS, "An ordination of upland forest communities of southern Wisconsin.-ecological Monographs," in journal of Ecological Monographs, 1957.</blockquote>	

<blockquote>38- J. L. Fleiss, J. Cohen, and B. S. J. P. B. Everitt, "Large sample standard errors of kappa and weighted kappa," in Psychological Bulletin, p. 323, 1969.</blockquote> 	

<blockquote>39- M. Felkin, "Comparing classification results between n-ary and binary problems," in Quality Measures in Data Mining: Springer, pp. 277-301, 2007.</blockquote> 

<blockquote>40- R. Ranawana and V. Palade, "Optimized Precision-A new measure for classifier performance evaluation," in 2006 IEEE International Conference on Evolutionary Computation, pp. 2254-2261, 2006.</blockquote>	

<blockquote>41- V. García, R. A. Mollineda, and J. S. Sánchez, "Index of balanced accuracy: A performance measure for skewed class distributions," in Iberian Conference on Pattern Recognition and Image Analysis, pp. 441-448, 2009.</blockquote> 

<blockquote>42- P. Branco, L. Torgo, and R. P. J. A. C. S. Ribeiro, "A survey of predictive modeling on imbalanced domains," in Journal ACM Computing Surveys (CSUR), p. 31, 2016.</blockquote> 

<blockquote>43- K. Pearson, "Notes on Regression and Inheritance in the Case of Two Parents," in Proceedings of the Royal Society of London, p. 240-242, 1895.</blockquote> 

<blockquote>44- W. J. I. Conover, New York, "Practical Nonparametric Statistics," in John Wiley and Sons, 1999.</blockquote> 

<blockquote>45- Yule, G. U, "On the methods of measuring association between two attributes." in Journal of the Royal Statistical Society, pp. 579-652, 1912.</blockquote>

<blockquote>46- Batuwita, R. and Palade, V, "A new performance measure for class imbalance learning. application to bioinformatics problems," in Machine Learning and Applications, pp.545–550, 2009.</blockquote>

<blockquote>47- D. K. Lee, "Alternatives to P value: confidence interval and effect size," Korean journal of anesthesiology, vol. 69, no. 6, p. 555, 2016.</blockquote>

<blockquote>48- M. A. Raslich, R. J. Markert, and S. A. Stutes, "Selecting and interpreting diagnostic tests," Biochemia medica: Biochemia medica, vol. 17, no. 2, pp. 151-161, 2007.</blockquote>

<blockquote>49- D. E. Hinkle, W. Wiersma, and S. G. Jurs, "Applied statistics for the behavioral sciences," 1988.</blockquote>

<blockquote>50- A. Maratea, A. Petrosino, and M. Manzo, "Adjusted F-measure and kernel scaling for imbalanced data learning," Information Sciences, vol. 257, pp. 331-341, 2014.</blockquote>

<blockquote>51- L. Mosley, "A balanced approach to the multi-class imbalance problem," 2013.</blockquote>

<blockquote>52- M. Vijaymeena and K. Kavitha, "A survey on similarity measures in text mining," Machine Learning and Applications: An International Journal, vol. 3, no. 2, pp. 19-28, 2016.</blockquote>

<blockquote>53- Y. Otsuka, "The faunal character of the Japanese Pleistocene marine Mollusca, as evidence of climate having become colder during the Pleistocene in Japan," Biogeograph. Soc. Japan, vol. 6, pp. 165-170, 1936.</blockquote>

<blockquote>54- A. Tversky, "Features of similarity," Psychological review, vol. 84, no. 4, p. 327, 1977.</blockquote>

<blockquote>55- K. Boyd, K. H. Eng, and C. D. Page, "Area under the precision-recall curve: point estimates and confidence intervals," in Joint European conference on machine learning and knowledge discovery in databases, 2013, pp. 451-466: Springer.</blockquote>

<blockquote>56- J. Davis and M. Goadrich, "The relationship between Precision-Recall and ROC curves," in Proceedings of the 23rd international conference on Machine learning, 2006, pp. 233-240: ACM.</blockquote>

<blockquote>57- M. Kuhn, "Building predictive models in R using the caret package," Journal of statistical software, vol. 28, no. 5, pp. 1-26, 2008.</blockquote>

<blockquote>58- V. Labatut and H. Cherifi, "Accuracy measures for the comparison of classifiers," arXiv preprint, 2012.</blockquote>

<blockquote>59- S. Wallis, "Binomial confidence intervals and contingency tests: mathematical fundamentals and the evaluation of alternative methods," Journal of Quantitative Linguistics, vol. 20, no. 3, pp. 178-208, 2013.</blockquote>

<blockquote>60- D. Altman, D. Machin, T. Bryant, and M. Gardner, Statistics with confidence: confidence intervals and statistical guidelines. John Wiley & Sons, 2013.</blockquote>

<blockquote>61- J. A. Hanley and B. J. McNeil, "The meaning and use of the area under a receiver operating characteristic (ROC) curve," Radiology, vol. 143, no. 1, pp. 29-36, 1982.</blockquote>

<blockquote>62- E. B. Wilson, "Probable inference, the law of succession, and statistical inference," Journal of the American Statistical Association, vol. 22, no. 158, pp. 209-212, 1927.</blockquote>

<blockquote>63- A. Agresti and B. A. Coull, "Approximate is better than “exact” for interval estimation of binomial proportions," The American Statistician, vol. 52, no. 2, pp. 119-126, 1998.</blockquote>

<blockquote>64- C. S. Peirce, "The numerical measure of the success of predictions," Science, no. 93, pp. 453-454, 1884.</blockquote>

<blockquote>65- E. W. Steyerberg, B. Van Calster, and M. J. Pencina, "Performance measures for prediction models and markers: evaluation of predictions and classifications," Revista Española de Cardiología, vol. 64, no. 9, pp. 788-794, 2011.</blockquote>

<blockquote>66- A. J. Vickers and E. B. Elkin, "Decision curve analysis: a novel method for evaluating prediction models," Medical Decision Making, vol. 26, no. 6, pp. 565-574, 2006.</blockquote>

<blockquote>67- D. Knoke, G. W. Bohrnstedt, and A. P. Mee, Statistics for social data analysis. FE Peacock Publishers Itasca, IL, 2002</blockquote>

<blockquote>68- W. M. Rand, "Objective criteria for the evaluation of clustering methods," Journal of the American Statistical association, vol. 66, no. 336, pp. 846-850, 1971.</blockquote>

<blockquote>69- J. M. Santos and M. Embrechts, "On the use of the adjusted rand index as a metric for evaluating supervised classification," in International conference on artificial neural networks, 2009: Springer, pp. 175-184.</blockquote>

<blockquote>70- J. Cohen, "Weighted kappa: nominal scale agreement provision for scaled disagreement or partial credit," Psychological bulletin, vol. 70, no. 4, p. 213, 1968.</blockquote>

<blockquote>71- R. Bakeman and J. M. Gottman, Observing interaction: An introduction to sequential analysis. Cambridge university press, 1997.</blockquote>

<blockquote>72- S. Bangdiwala, "A graphical test for observer agreement," in 45th International Statistical Institute Meeting, 1985, vol. 1985, pp. 307-308.</blockquote>

<blockquote>73- K. Bangdiwala and H. Bryan, "Using SAS software graphical procedures for the observer agreement chart," in Proceedings of the SAS Users Group International Conference, 1987, vol. 12, pp. 1083-1088.</blockquote>

<blockquote>74- A. F. Hayes and K. Krippendorff, "Answering the call for a standard reliability measure for coding data," Communication methods and measures, vol. 1, no. 1, pp. 77-89, 2007.</blockquote>

<blockquote>75- M. Aickin, "Maximum likelihood estimation of agreement in the constant predictive probability model, and its relation to Cohen's kappa," Biometrics, pp. 293-302, 1990.</blockquote>


## Cite

If you use PyCM in your research, we would appreciate citations to the following paper :

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

## Support

- Website : [https://www.pycm.ir](https://www.pycm.ir)		
- Mailing List : [https://mail.python.org/mailman3/lists/pycm.python.org/](https://mail.python.org/mailman3/lists/pycm.python.org/)
- Email : [info@pycm.ir](mailto:info@pycm.ir "info@pycm.ir")		


## License

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fsepandhaghighi%2Fpycm.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fsepandhaghighi%2Fpycm?ref=badge_large)


## Donate to our project		

If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .

<a href="http://www.pycm.ir/donate.html" target="_blank"><img src="http://www.pycm.ir/images/Donate-Button.png" height="90px" width="270px" alt="PyCM Donation"></a>


