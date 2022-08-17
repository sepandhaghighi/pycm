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
<a href="https://colab.research.google.com/github/sepandhaghighi/pycm/blob/master">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Document"/>
</a>
<a href="https://discord.com/invite/zqpU2b3J3f">
  <img src="https://img.shields.io/discord/901883546162065408.svg" alt="Discord Channel">
</a>
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
   * [Acknowledgments](https://github.com/sepandhaghighi/pycm#acknowledgments)
   * [References](https://github.com/sepandhaghighi/pycm#references)
   * [Cite](https://github.com/sepandhaghighi/pycm#cite)
   * [Authors](https://github.com/sepandhaghighi/pycm/blob/master/AUTHORS.md)
   * [License](https://github.com/sepandhaghighi/pycm/blob/master/LICENSE)
   * [Show Your Support](https://github.com/sepandhaghighi/pycm#show-your-support)
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
		<td align="center"><a href="http://pepy.tech/project/pycm"><img src="http://pepy.tech/badge/pycm"></a></td>
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
		<td align="center">CI</td>
		<td align="center"><img src="https://github.com/sepandhaghighi/pycm/workflows/CI/badge.svg?branch=master"></td>
		<td align="center"><img src="https://github.com/sepandhaghighi/pycm/workflows/CI/badge.svg?branch=dev"></td>
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
- Download [Version 3.6](https://github.com/sepandhaghighi/pycm/archive/v3.6.zip) or [Latest Source ](https://github.com/sepandhaghighi/pycm/archive/dev.zip)
- Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- Run `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install pycm==3.6` or `pip3 install pycm==3.6` (Need root access)

### Conda

- Check [Conda Managing Package](https://conda.io/)
- Update Conda using `conda update conda` (Need root access)
- Run `conda install -c sepandhaghighi pycm` (Need root access)

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


## Usage

		
### From vector
```pycon
>>> from pycm import *
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(actual_vector=y_actu, predict_vector=y_pred)
>>> cm.classes
[0, 1, 2]
>>> cm.table
{0: {0: 3, 1: 0, 2: 0}, 1: {0: 0, 1: 1, 2: 2}, 2: {0: 2, 1: 1, 2: 3}}
>>> cm.print_matrix()
Predict 0       1       2       
Actual
0       3       0       0       

1       0       1       2       

2       2       1       3   

>>> cm.print_normalized_matrix()
Predict       0             1             2             
Actual
0             1.0           0.0           0.0           

1             0.0           0.33333       0.66667       

2             0.33333       0.16667       0.5          

>>> cm.stat(summary=True)
Overall Statistics : 

ACC Macro                                                         0.72222
F1 Macro                                                          0.56515
FPR Macro                                                         0.22222
Kappa                                                             0.35484
Overall ACC                                                       0.58333
PPV Macro                                                         0.56667
SOA1(Landis & Koch)                                               Fair
TPR Macro                                                         0.61111
Zero-one Loss                                                     5

Class Statistics :

Classes                                                           0             1             2             
ACC(Accuracy)                                                     0.83333       0.75          0.58333       
AUC(Area under the ROC curve)                                     0.88889       0.61111       0.58333       
AUCI(AUC value interpretation)                                    Very Good     Fair          Poor          
F1(F1 score - harmonic mean of precision and sensitivity)         0.75          0.4           0.54545       
FN(False negative/miss/type 2 error)                              0             2             3             
FP(False positive/type 1 error/false alarm)                       2             1             2             
FPR(Fall-out or false positive rate)                              0.22222       0.11111       0.33333       
N(Condition negative)                                             9             9             6             
P(Condition positive or support)                                  3             3             6             
POP(Population)                                                   12            12            12            
PPV(Precision or positive predictive value)                       0.6           0.5           0.6           
TN(True negative/correct rejection)                               7             8             4             
TON(Test outcome negative)                                        7             10            7             
TOP(Test outcome positive)                                        5             2             5             
TP(True positive/hit)                                             3             1             3             
TPR(Sensitivity, recall, hit rate, or true positive rate)         1.0           0.33333       0.5 

```
### Direct CM
```pycon
>>> from pycm import *
>>> cm2 = ConfusionMatrix(matrix={"Class1": {"Class1": 1, "Class2":2}, "Class2": {"Class1": 0, "Class2": 5}})
>>> cm2
pycm.ConfusionMatrix(classes: ['Class1', 'Class2'])
>>> cm2.classes
['Class1', 'Class2']
>>> cm2.print_matrix()
Predict      Class1       Class2       
Actual
Class1       1            2            

Class2       0            5            

>>> cm2.print_normalized_matrix()
Predict       Class1        Class2        
Actual
Class1        0.33333       0.66667       

Class2        0.0           1.0 

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
     
```
* `matrix()` and `normalized_matrix()` renamed to `print_matrix()` and `print_normalized_matrix()` in `version 1.5`			

### Activation threshold
`threshold` is added in `version 0.9` for real value prediction.			
						
For more information visit [Example3](http://www.pycm.io/doc/Example3.html "Example3")

### Load from file			
`file` is added in `version 0.9.5` in order to load saved confusion matrix with `.obj` format generated by `save_obj` method.

For more information visit [Example4](http://www.pycm.io/doc/Example4.html "Example4")

### Sample weights
`sample_weight` is added in `version 1.2`

For more information visit [Example5](http://www.pycm.io/doc/Example5.html "Example5")

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

`is_imbalanced` parameter has been added in `version 3.3`, so the user can indicate whether the concerned dataset is imbalanced or not. As long as the user does not provide any information in this regard, the automatic detection algorithm will be used.

```pycon
>>> cm = ConfusionMatrix(y_actu, y_pred, is_imbalanced = True)
>>> cm.imbalance
True
>>> cm = ConfusionMatrix(y_actu, y_pred, is_imbalanced = False)
>>> cm.imbalance
False
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

Rank  Name   Class-Score       Overall-Score
1     cm2    0.50278           0.425
2     cm3    0.33611           0.33056

>>> cp.best
pycm.ConfusionMatrix(classes: [0, 1, 2])
>>> cp.sorted
['cm2', 'cm3']
>>> cp.best_name
'cm2'
```	

### Acceptable data types	

**ConfusionMatrix**

		
1. `actual_vector` : python `list` or numpy `array` of any stringable objects
2. `predict_vector` : python `list` or numpy `array` of any stringable objects
3. `matrix` : `dict`
4. `digit`: `int`	
5. `threshold` : `FunctionType (function or lambda)`	
6. `file` : `File object`
7. `sample_weight` : python `list` or numpy `array` of numbers
8. `transpose` : `bool`
9. `classes` : python `list`
10. `is_imbalanced` : `bool`

* Run `help(ConfusionMatrix)` for `ConfusionMatrix` object details

**Compare**

1. `cm_dict` : python `dict` of `ConfusionMatrix` object (`str` : `ConfusionMatrix`)
2. `by_class` : `bool`
3. `class_weight` : python `dict` of class weights (`class_name` : `float`)
4. `class_benchmark_weight`: python `dict` of class benchmark weights (`class_benchmark_name` : `float`) 
5. `overall_benchmark_weight`: python `dict` of overall benchmark weights (`overall_benchmark_name` : `float`) 
6. `digit`: `int`

* Run `help(Compare)` for `Compare` object details


For more information visit [here](https://github.com/sepandhaghighi/pycm/tree/master/Document "Document")

<div align="center">

<a href="https://asciinema.org/a/171863" target="_blank"><img src="https://asciinema.org/a/171863.png" /></a>
</div>

## Try PyCM in your browser!
PyCM can be used online in interactive Jupyter Notebooks via the Binder or Colab services! Try it out now! :

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sepandhaghighi/pycm/master)

[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sepandhaghighi/pycm/blob/master)

* Check `Examples` in `Document` folder 

## Issues & bug reports			

1. Fill an issue and describe it. We'll check it ASAP! 
    - Please complete the issue template
2. Discord : [https://discord.com/invite/zqpU2b3J3f](https://discord.com/invite/zqpU2b3J3f)
3. Website : [https://www.pycm.io](https://www.pycm.io)		
4. Mailing List : [https://mail.python.org/mailman3/lists/pycm.python.org/](https://mail.python.org/mailman3/lists/pycm.python.org/)
5. Email : [info@pycm.io](mailto:info@pycm.io "info@pycm.io")		


## Outputs	

1. [HTML](http://www.pycm.io/test.html)
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

## Acknowledgments

[NLnet foundation](https://nlnet.nl) has supported the PyCM project from version **3.6** to **4.0** through the [NGI Assure](https://nlnet.nl/assure) Fund. This fund is set up by [NLnet foundation](https://nlnet.nl) with funding from the European Commission's [Next Generation Internet program](https://ngi.eu), administered by DG Communications Networks, Content, and Technology under grant agreement [**No 957073**](https://nlnet.nl/project/PyCM/).

<a href="https://nlnet.nl"><img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/NlNet.svg" height="50px" alt="NLnet foundation"></a> &nbsp;  <a href="https://nlnet.nl/assure"><img src="https://github.com/sepandhaghighi/pycm/raw/master/Otherfiles/NGIAssure.svg" height="50px" alt="NGI Assure"></a>

## References			

<blockquote>1- J. R. Landis and G. G. Koch, "The measurement of observer agreement for categorical data," <i>biometrics</i>, pp. 159-174, 1977.</blockquote>

<blockquote>2- D. M. Powers, "Evaluation: from precision, recall and F-measure to ROC, informedness, markedness and correlation," <i>arXiv preprint arXiv:2010.16061</i>, 2020.</blockquote>

<blockquote>3- C. Sammut and G. I. Webb, <i>Encyclopedia of machine learning</i>. Springer Science & Business Media, 2011.</blockquote>

<blockquote>4- J. L. Fleiss, "Measuring nominal scale agreement among many raters," <i>Psychological bulletin</i>, vol. 76, no. 5, p. 378, 1971.</blockquote>

<blockquote>5- D. G. Altman, <i>Practical statistics for medical research</i>. CRC press, 1990.</blockquote>

<blockquote>6- K. L. Gwet, "Computing inter-rater reliability and its variance in the presence of high agreement," <i>British Journal of Mathematical and Statistical Psychology</i>, vol. 61, no. 1, pp. 29-48, 2008.</blockquote>

<blockquote>7- W. A. Scott, "Reliability of content analysis: The case of nominal scale coding," <i>Public opinion quarterly</i>, pp. 321-325, 1955.</blockquote>

<blockquote>8- E. M. Bennett, R. Alpert, and A. Goldstein, "Communications through limited-response questioning," <i>Public Opinion Quarterly</i>, vol. 18, no. 3, pp. 303-308, 1954.</blockquote>

<blockquote>9- D. V. Cicchetti, "Guidelines, criteria, and rules of thumb for evaluating normed and standardized assessment instruments in psychology," <i>Psychological assessment</i>, vol. 6, no. 4, p. 284, 1994.</blockquote>

<blockquote>10- R. B. Davies, "Algorithm AS 155: The distribution of a linear combination of χ2 random variables," <i>Applied Statistics</i>, pp. 323-333, 1980.</blockquote>

<blockquote>11- S. Kullback and R. A. Leibler, "On information and sufficiency," <i>The annals of mathematical statistics</i>, vol. 22, no. 1, pp. 79-86, 1951.</blockquote>

<blockquote>12- L. A. Goodman and W. H. Kruskal, "Measures of association for cross classifications, IV: Simplification of asymptotic variances," <i>Journal of the American Statistical Association</i>, vol. 67, no. 338, pp. 415-421, 1972.</blockquote>

<blockquote>13- L. A. Goodman and W. H. Kruskal, "Measures of association for cross classifications III: Approximate sampling theory," <i>Journal of the American Statistical Association</i>, vol. 58, no. 302, pp. 310-364, 1963.</blockquote>

<blockquote>14- T. Byrt, J. Bishop, and J. B. Carlin, "Bias, prevalence and kappa," <i>Journal of clinical epidemiology</i>, vol. 46, no. 5, pp. 423-429, 1993.</blockquote>

<blockquote>15- M. Shepperd, D. Bowes, and T. Hall, "Researcher bias: The use of machine learning in software defect prediction," <i>IEEE Transactions on Software Engineering</i>, vol. 40, no. 6, pp. 603-616, 2014.</blockquote>

<blockquote>16- X. Deng, Q. Liu, Y. Deng, and S. Mahadevan, "An improved method to construct basic probability assignment based on the confusion matrix for classification problem," <i>Information Sciences</i>, vol. 340, pp. 250-261, 2016.</blockquote>

<blockquote>17- J.-M. Wei, X.-J. Yuan, Q.-H. Hu, and S.-Q. Wang, "A novel measure for evaluating classifiers," <i>Expert Systems with Applications</i>, vol. 37, no. 5, pp. 3799-3809, 2010.</blockquote>

<blockquote>18- I. Kononenko and I. Bratko, "Information-based evaluation criterion for classifier's performance," <i>Machine learning</i>, vol. 6, no. 1, pp. 67-80, 1991.</blockquote>

<blockquote>19- R. Delgado and J. D. Núnez-González, "Enhancing confusion entropy as measure for evaluating classifiers," in <i>The 13th International Conference on Soft Computing Models in Industrial and Environmental Applications</i>, 2018: Springer, pp. 79-89.</blockquote>

<blockquote>20- J. Gorodkin, "Comparing two K-category assignments by a K-category correlation coefficient," <i>Computational biology and chemistry</i>, vol.28, no. 5-6, pp. 367-374, 2004.</blockquote>

<blockquote>21- C. O. Freitas, J. M. De Carvalho, J. Oliveira, S. B. Aires, and R. Sabourin, "Confusion matrix disagreement for multiple classifiers," in <i>Iberoamerican Congress on Pattern Recognition</i>, 2007: Springer, pp. 387-396.</blockquote>

<blockquote>22- P. Branco, L. Torgo, and R. P. Ribeiro, "Relevance-based evaluation metrics for multi-class imbalanced domains," in <i>Pacific-Asia Conference on Knowledge Discovery and Data Mining</i>, 2017: Springer, pp. 698-710.</blockquote>

<blockquote>23- D. Ballabio, F. Grisoni, and R. Todeschini, "Multivariate comparison of classification performance measures," <i>Chemometrics and Intelligent Laboratory Systems</i>, vol. 174, pp. 33-44, 2018.</blockquote>

<blockquote>24- J. Cohen, "A coefficient of agreement for nominal scales," <i>Educational and psychological measurement</i>, vol. 20, no. 1, pp. 37-46, 1960.</blockquote>

<blockquote>25- S. Siegel, "Nonparametric statistics for the behavioral sciences," 1956.</blockquote>

<blockquote>26- H. Cramér, <i>Mathematical methods of statistics</i>. Princeton university press, 1999.</blockquote>

<blockquote>27- B. W. Matthews, "Comparison of the predicted and observed secondary structure of T4 phage lysozyme," <i>Biochimica et Biophysica Acta (BBA)-Protein Structure</i>, vol. 405, no. 2, pp. 442-451, 1975.</blockquote>

<blockquote>28- J. A. Swets, "The relative operating characteristic in psychology: a technique for isolating effects of response bias finds wide use in the study of perception and cognition," <i>Science</i>, vol. 182, no. 4116, pp. 990-1000, 1973.</blockquote>

<blockquote>29- P. Jaccard, "Étude comparative de la distribution florale dans une portion des Alpes et des Jura," <i>Bull Soc Vaudoise Sci Nat</i>, vol. 37, pp. 547-579, 1901.</blockquote>

<blockquote>30- T. M. Cover and J. A. Thomas, <i>Elements of Information Theory</i>. John Wiley & Sons, 2012.</blockquote>

<blockquote>31- E. S. Keeping, <i>Introduction to statistical inference</i>. Courier Corporation, 1995.</blockquote>

<blockquote>32- V. Sindhwani, P. Bhattacharya, and S. Rakshit, "Information theoretic feature crediting in multiclass support vector machines," in <i>Proceedings of the 2001 SIAM International Conference on Data Mining</i>, 2001: SIAM, pp. 1-18.</blockquote>

<blockquote>33- M. Bekkar, H. K. Djemaa, and T. A. Alitouche, "Evaluation measures for models assessment over imbalanced data sets," <i>J Inf Eng Appl</i>, vol. 3, no. 10, 2013.</blockquote>

<blockquote>34- W. J. Youden, "Index for rating diagnostic tests," <i>Cancer</i>, vol. 3, no. 1, pp. 32-35, 1950.</blockquote>

<blockquote>35- S. Brin, R. Motwani, J. D. Ullman, and S. Tsur, "Dynamic itemset counting and implication rules for market basket data," in <i>Proceedings of the 1997 ACM SIGMOD international conference on Management of data</i>, 1997, pp. 255-264.</blockquote>

<blockquote>36- S. Raschka, "MLxtend: Providing machine learning and data science utilities and extensions to Python's scientific computing stack," <i>Journal of open source software</i>, vol. 3, no. 24, p. 638, 2018.</blockquote>

<blockquote>37- J. R. Bray and J. T. Curtis, "An ordination of the upland forest communities of southern Wisconsin," Ecological monographs, vol. 27, no. 4, pp. 325-349, 1957.</blockquote>

<blockquote>38- J. L. Fleiss, J. Cohen, and B. S. Everitt, "Large sample standard errors of kappa and weighted kappa," <i>Psychological bulletin</i>, vol. 72, no. 5, p. 323, 1969.</blockquote>

<blockquote>39- M. Felkin, "Comparing classification results between n-ary and binary problems," in <i>Quality Measures in Data Mining</i>: Springer, 2007, pp. 277-301.</blockquote>

<blockquote>40- R. Ranawana and V. Palade, "Optimized precision-a new measure for classifier performance evaluation," in <i>2006 IEEE International Conference on Evolutionary Computation</i>, 2006: IEEE, pp. 2254-2261.</blockquote>

<blockquote>41- V. García, R. A. Mollineda, and J. S. Sánchez, "Index of balanced accuracy: A performance measure for skewed class distributions," in <i>Iberian conference on pattern recognition and image analysis</i>, 2009: Springer, pp. 441-448.</blockquote>

<blockquote>42- P. Branco, L. Torgo, and R. P. Ribeiro, "A survey of predictive modeling on imbalanced domains," <i>ACM Computing Surveys (CSUR)</i>, vol. 49, no. 2, pp. 1-50, 2016.</blockquote>

<blockquote>43- K. Pearson, "Notes on Regression and Inheritance in the Case of Two Parents," in <i>Proceedings of the Royal Society of London</i>, p. 240-242, 1895.</blockquote>

<blockquote>44- W. J. Conover, <i>Practical nonparametric statistics</i>. John Wiley & Sons, 1998.</blockquote>

<blockquote>45- G. U. Yule, "On the methods of measuring association between two attributes," <i>Journal of the Royal Statistical Society</i>, vol. 75, no. 6, pp. 579-652, 1912.</blockquote>

<blockquote>46- R. Batuwita and V. Palade, "A new performance measure for class imbalance learning. application to bioinformatics problems," in <i>2009 International Conference on Machine Learning and Applications</i>, 2009: IEEE, pp. 545-550.</blockquote>

<blockquote>47- D. K. Lee, "Alternatives to P value: confidence interval and effect size," <i>Korean journal of anesthesiology</i>, vol. 69, no. 6, p. 555, 2016.</blockquote>

<blockquote>48- M. A. Raslich, R. J. Markert, and S. A. Stutes, "Selecting and interpreting diagnostic tests," <i>Biochemia Medica</i>, vol. 17, no. 2, pp. 151-161, 2007.</blockquote>

<blockquote>49- D. E. Hinkle, W. Wiersma, and S. G. Jurs, <i>Applied statistics for the behavioral sciences</i>. Houghton Mifflin College Division, 2003.</blockquote>

<blockquote>50- A. Maratea, A. Petrosino, and M. Manzo, "Adjusted F-measure and kernel scaling for imbalanced data learning," <i>Information Sciences</i>, vol. 257, pp. 331-341, 2014.</blockquote>

<blockquote>51- L. Mosley, "A balanced approach to the multi-class imbalance problem," 2013.</blockquote>

<blockquote>52- M. Vijaymeena and K. Kavitha, "A survey on similarity measures in text mining," <i>Machine Learning and Applications: An International Journal</i>, vol. 3, no. 2, pp. 19-28, 2016.</blockquote>

<blockquote>53- Y. Otsuka, "The faunal character of the Japanese Pleistocene marine Mollusca, as evidence of climate having become colder during the Pleistocene in Japan," <i>Biogeograph Soc Japan</i>, vol. 6, no. 16, pp. 165-170, 1936.</blockquote>

<blockquote>54- A. Tversky, "Features of similarity," <i>Psychological review</i>, vol. 84, no. 4, p. 327, 1977.</blockquote>

<blockquote>55- K. Boyd, K. H. Eng, and C. D. Page, "Area under the precision-recall curve: point estimates and confidence intervals," in <i>Joint European conference on machine learning and knowledge discovery in databases</i>, 2013: Springer, pp. 451-466.</blockquote>

<blockquote>56- J. Davis and M. Goadrich, "The relationship between Precision-Recall and ROC curves," in <i>Proceedings of the 23rd international conference on Machine learning</i>, 2006, pp. 233-240.</blockquote>

<blockquote>57- M. Kuhn, "Building predictive models in R using the caret package," <i>J Stat Softw</i>, vol. 28, no. 5, pp. 1-26, 2008.</blockquote>

<blockquote>58- V. Labatut and H. Cherifi, "Accuracy measures for the comparison of classifiers," <i>arXiv preprint arXiv:1207.3790</i>, 2012.</blockquote>

<blockquote>59- S. Wallis, "Binomial confidence intervals and contingency tests: mathematical fundamentals and the evaluation of alternative methods," <i>Journal of Quantitative Linguistics</i>, vol. 20, no. 3, pp. 178-208, 2013.</blockquote>

<blockquote>60- D. Altman, D. Machin, T. Bryant, and M. Gardner, <i>Statistics with confidence: confidence intervals and statistical guidelines</i>. John Wiley & Sons, 2013.</blockquote>

<blockquote>61- J. A. Hanley and B. J. McNeil, "The meaning and use of the area under a receiver operating characteristic (ROC) curve," <i>Radiology</i>, vol. 143, no. 1, pp. 29-36, 1982.</blockquote>

<blockquote>62- E. B. Wilson, "Probable inference, the law of succession, and statistical inference," <i>Journal of the American Statistical Association</i>, vol. 22, no. 158, pp. 209-212, 1927.</blockquote>

<blockquote>63- A. Agresti and B. A. Coull, "Approximate is better than “exact” for interval estimation of binomial proportions," <i>The American Statistician</i>, vol. 52, no. 2, pp. 119-126, 1998.</blockquote>

<blockquote>64- C. S. Peirce, "The numerical measure of the success of predictions," <i>Science</i>, no. 93, pp. 453-454, 1884.</blockquote>

<blockquote>65- E. W. Steyerberg, B. Van Calster, and M. J. Pencina, "Performance measures for prediction models and markers: evaluation of predictions and classifications," <i>Revista Española de Cardiología (English Edition)</i>, vol. 64, no. 9, pp. 788-794, 2011.</blockquote>

<blockquote>66- A. J. Vickers and E. B. Elkin, "Decision curve analysis: a novel method for evaluating prediction models," <i>Medical Decision Making</i>, vol. 26, no. 6, pp. 565-574, 2006.</blockquote>

<blockquote>67- G. W. Bohrnstedt and D. Knoke,"Statistics for social data analysis," 1982.</blockquote>

<blockquote>68- W. M. Rand, "Objective criteria for the evaluation of clustering methods," <i>Journal of the American Statistical association</i>, vol. 66, no. 336, pp. 846-850, 1971.</blockquote>

<blockquote>69- J. M. Santos and M. Embrechts, "On the use of the adjusted rand index as a metric for evaluating supervised classification," in <i>International conference on artificial neural networks</i>, 2009: Springer, pp. 175-184.</blockquote>

<blockquote>70- J. Cohen, "Weighted kappa: nominal scale agreement provision for scaled disagreement or partial credit," <i>Psychological bulletin</i>, vol. 70, no. 4, p. 213, 1968.</blockquote>

<blockquote>71- R. Bakeman and J. M. Gottman, <i>Observing interaction: An introduction to sequential analysis</i>. Cambridge university press, 1997.</blockquote>

<blockquote>72- S. Bangdiwala, "A graphical test for observer agreement," in <i>45th International Statistical Institute Meeting</i>, 1985, vol. 1985, p. 307.</blockquote>

<blockquote>73- K. Bangdiwala and H. Bryan, "Using SAS software graphical procedures for the observer agreement chart," in <i>Proceedings of the SAS Users Group International Conference</i>, 1987, vol. 12, pp. 1083-1088.</blockquote>

<blockquote>74- A. F. Hayes and K. Krippendorff, "Answering the call for a standard reliability measure for coding data," <i>Communication methods and measures</i>, vol. 1, no. 1, pp. 77-89, 2007.</blockquote>

<blockquote>75- M. Aickin, "Maximum likelihood estimation of agreement in the constant predictive probability model, and its relation to Cohen's kappa," <i>Biometrics</i>, pp. 293-302, 1990.</blockquote>

<blockquote>76- N. A. Macmillan and C. D. Creelman, <i>Detectiontheory: A user's guide</i>. Psychology press, 2004.</blockquote>

<blockquote>77- D. J. Hand, P. Christen, and N. Kirielle, "F*: an interpretable transformation of the F-measure," <i>Machine Learning</i>, vol. 110, no. 3, pp. 451-456, 2021.</blockquote>

<blockquote>78- G. W. Brier, "Verification of forecasts expressed in terms of probability," <i>Monthly weather review</i>, vol. 78, no. 1, pp. 1-3, 1950.</blockquote>

<blockquote>79- L. Buitinck et al., "API design for machine learning software: experiences from the scikit-learn project," <i>arXiv preprint arXiv:1309.0238</i>, 2013.</blockquote>

<blockquote>80- R. W. Hamming, "Error detecting and error correcting codes," The Bell system technical journal, vol. 29, no. 2, pp. 147-160, 1950.</blockquote>

<blockquote>81- S. S. Choi, S. H. Cha, and C. C. Tappert, "A survey of binary similarity and distance measures," Journal of systemics, cybernetics and informatics, vol. 8, no. 1, pp. 43-48, 2010.</blockquote>

<blockquote>82- J. Braun-Blanquet, "Plant sociology. The study of plant communities," Plant sociology. The study of plant communities. First ed., 1932.</blockquote>

<blockquote>83- C. C. Little, "Abydos Documentation," 2020.</blockquote>


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

Download [PyCM.bib](http://www.pycm.io/PYCM.bib)	


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

## Show your support

### Star this repo

Give a ⭐️ if this project helped you!


### Donate to our project

If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .

<a href="http://www.pycm.io/donate.html" target="_blank"><img src="http://www.pycm.io/images/Donate-Button.png" height="90px" width="270px" alt="PyCM Donation"></a>


