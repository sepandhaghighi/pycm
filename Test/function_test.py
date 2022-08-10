# -*- coding: utf-8 -*-
"""
>>> from pycm import *
>>> import os
>>> import json
>>> import numpy as np
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(y_actu, y_pred)
>>> LBL_MP = cm.label_map
>>> LBL_MP[0]
0
>>> LBL_MP[1]
1
>>> LBL_MP[2]
2
>>> cm.relabel({0:"L1",1:"L2",2:"L3"})
>>> LBL_MP = cm.label_map
>>> LBL_MP[0]
'L1'
>>> LBL_MP[1]
'L2'
>>> LBL_MP[2]
'L3'
>>> pycm_help()
<BLANKLINE>
PyCM is a multi-class confusion matrix library written in Python that
supports both input data vectors and direct matrix, and a proper tool for
post-classification model evaluation that supports most classes and overall
statistics parameters.
PyCM is the swiss-army knife of confusion matrices, targeted mainly at
data scientists that need a broad array of metrics for predictive models
and an accurate evaluation of large variety of classifiers.
<BLANKLINE>
If you use PyCM in your research, we would appreciate citations to the following paper :
<BLANKLINE>
https://doi.org/10.21105/joss.00729
<BLANKLINE>
<BLANKLINE>
Repo : https://github.com/sepandhaghighi/pycm
Webpage : https://www.pycm.io
>>> online_help(param=None)
Please choose one parameter :
<BLANKLINE>
Example : online_help("J") or online_help(2)
<BLANKLINE>
1-95% CI
2-ACC
3-ACC Macro
4-AGF
5-AGM
6-AM
7-ARI
8-AUC
9-AUCI
10-AUNP
11-AUNU
12-AUPR
13-BB
14-BCD
15-BM
16-Bangdiwala B
17-Bennett S
18-CBA
19-CEN
20-CSI
21-Chi-Squared
22-Chi-Squared DF
23-Conditional Entropy
24-Cramer V
25-Cross Entropy
26-DOR
27-DP
28-DPI
29-ERR
30-F0.5
31-F1
32-F1 Macro
33-F1 Micro
34-F2
35-FDR
36-FN
37-FNR
38-FNR Macro
39-FNR Micro
40-FOR
41-FP
42-FPR
43-FPR Macro
44-FPR Micro
45-G
46-GI
47-GM
48-Gwet AC1
49-HD
50-Hamming Loss
51-IBA
52-ICSI
53-IS
54-J
55-Joint Entropy
56-KL Divergence
57-Kappa
58-Kappa 95% CI
59-Kappa No Prevalence
60-Kappa Standard Error
61-Kappa Unbiased
62-Krippendorff Alpha
63-LS
64-Lambda A
65-Lambda B
66-MCC
67-MCCI
68-MCEN
69-MK
70-Mutual Information
71-N
72-NIR
73-NLR
74-NLRI
75-NPV
76-OC
77-OOC
78-OP
79-Overall ACC
80-Overall CEN
81-Overall J
82-Overall MCC
83-Overall MCEN
84-Overall RACC
85-Overall RACCU
86-P
87-P-Value
88-PLR
89-PLRI
90-POP
91-PPV
92-PPV Macro
93-PPV Micro
94-PRE
95-Pearson C
96-Phi-Squared
97-Q
98-QI
99-RACC
100-RACCU
101-RCI
102-RR
103-Reference Entropy
104-Response Entropy
105-SOA1(Landis & Koch)
106-SOA2(Fleiss)
107-SOA3(Altman)
108-SOA4(Cicchetti)
109-SOA5(Cramer)
110-SOA6(Matthews)
111-Scott PI
112-Standard Error
113-TN
114-TNR
115-TNR Macro
116-TNR Micro
117-TON
118-TOP
119-TP
120-TPR
121-TPR Macro
122-TPR Micro
123-Y
124-Zero-one Loss
125-dInd
126-sInd
>>> online_help("J")
...
>>> online_help("J",alt_link=True)
...
>>> online_help(4)
...
>>> from pycm.pycm_overall_func import *
>>> from pycm.pycm_class_func import *
>>> from pycm.pycm_ci import *
>>> from pycm.pycm_interpret import *
>>> from pycm.pycm_util import *
>>> inv_erf(-1)
'None'
>>> inv_erf(1)
'None'
>>> inv_erf(-2)
'None'
>>> inv_erf(2)
'None'
>>> inv_erf(0)
0
>>> inv_erf(-0.9999999999999749)
-5.389154023751963
>>> inv_erf(1.2490009027033011e-14)
1.1019786822020638e-14
>>> inv_erf(0.3)
0.27246271472675443
>>> inv_erf(0.8)
0.9061938024368231
>>> inv_erf(0.22)
0.19750838337227367
>>> complement(0.5)
0.5
>>> complement("None")
'None'
>>> rounder((1,2,"None"), digit=5)
'(1,2,None)'
>>> one_vs_all_func([1,2], {1:{1:0,2:0},2:{1:0,2:0}}, {1:0,2:0}, {1:0,2:0}, {1:0,2:0}, {1:0,2:0}, 3) == [[1, 2], {1: {1: 0, 2: 0}, 2: {1: 0, 2: 0}}]
True
>>> Q_calc(1,2,3,"None")
'None'
>>> AGM_calc(2,2,2,2,"None")
'None'
>>> ARI_calc([1,2],{1:{1:0,2:0},2:{1:0,2:0}},{1:0,2:0},{1:0,2:0},0)
'None'
>>> BCD_calc(2, "None")
'None'
>>> AM_calc(3, "None")
'None'
>>> RCI_calc(24,0)
'None'
>>> BB_calc(0,0,0)
'None'
>>> CEN_calc([1,2,3], {1:{1:0,2:0},2:{1:0,2:0}}, {1:2,2:3}, {1:2,2:3}, 2, modified=False)
'None'
>>> convex_combination([1,2,3], {1:{1:0,2:0},2:{1:0,2:0}}, {1:2,2:3}, {1:2,2:3}, 2, modified=False)
'None'
>>> overall_CEN_calc([1,2], {1:2,2:3},{1:2,2:3}, {1:2,2:3}, {1:2,2:"None"}, modified=False)
'None'
>>> NIR_calc({1:0,2:0}, 0)
'None'
>>> hamming_calc({1:0,2:0}, 0)
'None'
>>> zero_one_loss_calc({1:0,2:0}, "None")
'None'
>>> entropy_calc({1:0,2:0}, {1:0,2:0})
'None'
>>> kappa_no_prevalence_calc("None")
'None'
>>> cross_entropy_calc({1:0,2:0}, {1:0,2:0}, {1:0,2:0})
'None'
>>> joint_entropy_calc([1,2], {1:{1:0,2:0},2:{1:0,2:0}}, {1:0,2:0})
'None'
>>> conditional_entropy_calc([1,2],{1:{1:0,2:0},2:{1:0,2:0}}, {1:0,2:0}, {1:0,2:0})
'None'
>>> mutual_information_calc(2, "None")
'None'
>>> lambda_B_calc([1,2], {1:{1:0,2:0},2:{1:0,2:0}}, {1:0,2:0}, {1:0,2:0})
'None'
>>> lambda_A_calc([1,2], {1:{1:0,2:0},2:{1:0,2:0}}, {1:0,2:0}, {1:0,2:0})
'None'
>>> DF_calc(2)
'None'
>>> kappa_SE_calc(2, 1, 2)
'None'
>>> CI_calc(23, "None", CV=1.96)
('None', 'None')
>>> CI_calc_agresti("None",20,CV=1.96)
('None', 'None')
>>> CI_calc_wilson(200,0,CV=1.96)
('None', 'None')
>>> CI_calc_wilson(200,"None",CV=1.96)
('None', 'None')
>>> AUC_SE_calc(0.52, 0, 0)
'None'
>>> AUC_SE_calc("None", 40, 42)
'None'
>>> LR_SE_calc(0, 0, 0, 0)
'None'
>>> LR_SE_calc(0, 20, 2, 21)
'None'
>>> LR_CI_calc("None", 0.5, CV=1.96)
('None', 'None')
>>> PC_S_calc([])
'None'
>>> jaccard_index_calc(0, 0, 0)
'None'
>>> overall_jaccard_index_calc([])
'None'
>>> overall_accuracy_calc({1:0,2:0}, 0)
'None'
>>> overall_random_accuracy_calc({1:0,2:None})
'None'
>>> CBA_calc([1,2], {1:{1:0,2:0},2:{1:0,2:0}}, {1:0,2:0}, {1:0,2:0})
'None'
>>> RR_calc([], {1:0,2:0})
'None'
>>> overall_MCC_calc([1,2], {1:{1:0,2:0},2:{1:0,2:0}}, {1:0,2:0}, {1:0,2:0})
'None'
>>> CEN_misclassification_calc({1:{1:0,2:0},2:{1:0,2:0}},{1:0,2:0},{1:0,2:0},1,1,2)
'None'
>>> brier_score_calc([1,0], [0.8,0.3,0.2,0.4], [1,1,0,1], sample_weight=None, pos_class=None)
0.23249999999999998
>>> brier_score_calc([1,"0"], [0.8,0.3,0.2,0.4], [1,1,0,1], sample_weight=None, pos_class=None)
'None'
>>> vector_check([1,2,3,0.4])
False
>>> vector_check([1,2,3,-2])
False
>>> matrix_check({1:{1:0.5,2:0},2:{1:0,2:0}})
False
>>> matrix_check([])
False
>>> TTPN_calc(0,0)
'None'
>>> TTPN_calc(1,4)
0.2
>>> FXR_calc(None)
'None'
>>> FXR_calc(0.2)
0.8
>>> ACC_calc(0,0,0,0)
'None'
>>> ACC_calc(1,1,3,4)
0.2222222222222222
>>> MCC_calc(0,2,0,2)
'None'
>>> MCC_calc(1,2,3,4)
-0.408248290463863
>>> LR_calc(1,2)
0.5
>>> LR_calc(1,0)
'None'
>>> MK_BM_calc(2,"None")
'None'
>>> MK_BM_calc(1,2)
2
>>> PRE_calc(None,2)
'None'
>>> PRE_calc(1,5)
0.2
>>> PRE_calc(1,0)
'None'
>>> G_calc(None,2)
'None'
>>> G_calc(1,2)
1.4142135623730951
>>> RACC_calc(2,3,4)
0.375
>>> reliability_calc(1,None)
'None'
>>> reliability_calc(2,0.3)
1.7
>>> micro_calc({1:2,2:3},{1:1,2:4})
0.5
>>> micro_calc({1:2,2:3},None)
'None'
>>> macro_calc(None)
'None'
>>> macro_calc({1:2,2:3})
2.5
>>> F_calc(TP=0,FP=0,FN=0,beta=1)
'None'
>>> F_calc(TP=3,FP=2,FN=1,beta=5)
0.7428571428571429
>>> TI_calc("None",0,0,0,0)
'None'
>>> NB_calc(1,2,4,"None")
'None'
>>> ERR_calc(None)
'None'
>>> ERR_calc(0.1)
0.9
>>> cm.average("F0.5")
0.5612141481706698
>>> cm.average("DOR")
'None'
>>> cm.average("DOR", none_omit=True)
2.9999999999999987
>>> cm.weighted_average("PPV")
0.575
>>> cm.weighted_average("DOR",none_omit=True)
2.666666666666666
>>> cm.weighted_average("DOR")
'None'
>>> cm.weighted_average("PPV",weight=cm.P)
0.575
>>> cm.weighted_average("PPV",weight={'L1': 0, 'L3': 0, 'L2': 1})
0.5
>>> cm.weighted_average("PPV",weight={'L1': 0, 'L3': 1, 'L2': 1})
0.55
>>> cm.weighted_average("PPV",weight={'L1': 1, 'L3': 0, 'L2': 1})
0.55
>>> cm.aickin_alpha(max_iter=None)
'None'
>>> cm.positions
>>> POS = cm.position()
>>> POS == cm.positions
True
>>> POS['L1']['TP']
[1, 4, 9]
>>> POS['L1']['TN']
[2, 3, 5, 6, 8, 10, 11]
>>> POS['L1']['FP']
[0, 7]
>>> POS['L1']['FN']
[]
>>> POS['L2']['TP']
[6]
>>> POS['L2']['TN']
[0, 1, 2, 4, 7, 8, 9, 11]
>>> POS['L2']['FP']
[3]
>>> POS['L2']['FN']
[5, 10]
>>> POS['L3']['TP']
[2, 8, 11]
>>> POS['L3']['TN']
[1, 4, 6, 9]
>>> POS['L3']['FP']
[5, 10]
>>> POS['L3']['FN']
[0, 3, 7]
>>> y_actu = [0, 0, 1, 1, 0]
>>> y_pred = [0, 1, 1, 0, 0]
>>> cm2 = ConfusionMatrix(actual_vector=y_actu, predict_vector=y_pred)
>>> POS = cm2.position()
>>> POS[0]['TP']
[0, 4]
>>> POS[0]['TN']
[2]
>>> POS[0]['FP']
[3]
>>> POS[0]['FN']
[1]
>>> POS[1]['TP']
[2]
>>> POS[1]['TN']
[0, 4]
>>> POS[1]['FP']
[1]
>>> POS[1]['FN']
[3]
>>> POS == cm2.positions
True
>>> cm2.relabel({0:'L1',1:'L2'})
>>> cm2.positions
>>> LBL_MP = cm2.label_map
>>> LBL_MP[0]
'L1'
>>> LBL_MP[1]
'L2'
>>> POS = cm2.position()
>>> POS['L1']['TP']
[0, 4]
>>> POS['L1']['TN']
[2]
>>> POS['L1']['FP']
[3]
>>> POS['L1']['FN']
[1]
>>> POS['L2']['TP']
[2]
>>> POS['L2']['TN']
[0, 4]
>>> POS['L2']['FP']
[1]
>>> POS['L2']['FN']
[3]
>>> y_actu = np.array([0, 0, 1, 1, 0])
>>> y_pred = [0, 1, "1", 0, 0]
>>> cm2 = ConfusionMatrix(actual_vector=y_actu, predict_vector=y_pred)
>>> POS = cm2.position()
>>> POS["0"]['TP']
[0, 4]
>>> POS["0"]['TN']
[2]
>>> POS["0"]['FP']
[3]
>>> POS["0"]['FN']
[1]
>>> POS["1"]['TP']
[2]
>>> POS["1"]['TN']
[0, 4]
>>> POS["1"]['FP']
[1]
>>> POS["1"]['FN']
[3]
>>> cm.F_beta(4)["L1"]
0.9622641509433962
>>> cm.F_beta(4)["L2"]
0.34
>>> cm.F_beta(4)["L3"]
0.504950495049505
>>> cm.F_beta(None) == {'L3': 'None', 'L1': 'None', 'L2': 'None'}
True
>>> cm.IBA_alpha(None) == {'L3': 'None', 'L1': 'None', 'L2': 'None'}
True
>>> cm.relabel({"L1":"L4","L2":"L5","L3":"L6"})
>>> LBL_MP = cm.label_map
>>> LBL_MP[0]
'L4'
>>> LBL_MP[1]
'L5'
>>> LBL_MP[2]
'L6'
>>> del cm.classes
>>> del cm.TP
>>> cm.IBA_alpha(2)
{}
>>> cm.TI(2,3)
{}
>>> cm.F_beta(2)
{}
>>> cm.NB(3)
{}
>>> Q_analysis(None)
'None'
>>> Q_analysis("None")
'None'
>>> Q_analysis(1)
'Strong'
>>> Q_analysis(0)
'Negligible'
>>> Q_analysis(0.75)
'Strong'
>>> MCC_analysis(0.9)
'Very Strong'
>>> V_analysis(0.8)
'Very Strong'
>>> kappa_analysis_fleiss(0.75)
'Excellent'
>>> kappa_analysis_koch(-0.1)
'Poor'
>>> kappa_analysis_koch(0)
'Slight'
>>> kappa_analysis_koch(0.2)
'Fair'
>>> kappa_analysis_koch(0.4)
'Moderate'
>>> kappa_analysis_koch(0.6)
'Substantial'
>>> kappa_analysis_koch(0.8)
'Almost Perfect'
>>> kappa_analysis_koch(1.2)
'None'
>>> kappa_analysis_fleiss(0.4)
'Intermediate to Good'
>>> kappa_analysis_fleiss(0.75)
'Excellent'
>>> kappa_analysis_fleiss(1.2)
'Excellent'
>>> kappa_analysis_altman(-0.2)
'Poor'
>>> kappa_analysis_altman(0.2)
'Fair'
>>> kappa_analysis_altman(0.4)
'Moderate'
>>> kappa_analysis_altman(0.6)
'Good'
>>> kappa_analysis_altman(0.8)
'Very Good'
>>> kappa_analysis_altman(1.2)
'None'
>>> kappa_analysis_fleiss(0.2)
'Poor'
>>> kappa_analysis_cicchetti(0.3)
'Poor'
>>> kappa_analysis_cicchetti(0.5)
'Fair'
>>> kappa_analysis_cicchetti(0.65)
'Good'
>>> kappa_analysis_cicchetti(0.8)
'Excellent'
>>> kappa_analysis_cicchetti(1.2)
'None'
>>> PLR_analysis("None")
'None'
>>> PLR_analysis(1)
'Poor'
>>> PLR_analysis(3)
'Poor'
>>> PLR_analysis(7)
'Fair'
>>> PLR_analysis(11)
'Good'
>>> DP_analysis(0.2)
'Poor'
>>> DP_analysis(1.5)
'Limited'
>>> DP_analysis(2.5)
'Fair'
>>> DP_analysis(10)
'Good'
>>> AUC_analysis(0.5)
'Poor'
>>> AUC_analysis(0.65)
'Fair'
>>> AUC_analysis(0.75)
'Good'
>>> AUC_analysis(0.86)
'Very Good'
>>> AUC_analysis(0.97)
'Excellent'
>>> AUC_analysis(1.0)
'Excellent'
>>> PC_AC1_calc(1,1,1)
'None'
>>> PC_AC1_calc({1:123,2:2},{1:120,2:5},{1:125,2:125})
0.05443200000000002
>>> y_act=[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2]
>>> y_pre=[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,2,0,1,2,2,2,2]
>>> cm2=ConfusionMatrix(y_act,y_pre)
>>> chi_squared=chi_square_calc(cm2.classes,cm2.table,cm2.TOP,cm2.P,cm2.POP)
>>> chi_squared
15.525641025641026
>>> population = list(cm2.POP.values())[0]
>>> phi_squared=phi_square_calc(chi_squared,population)
>>> phi_squared
0.5750237416904084
>>> V=cramers_V_calc(phi_squared,cm2.classes)
>>> V
0.5362013342441477
>>> DF=DF_calc(cm2.classes)
>>> DF
4
>>> SE=SE_calc(cm2.Overall_ACC,population)
>>> SE
0.09072184232530289
>>> CI=CI_calc(cm2.Overall_ACC,SE)
>>> CI
(0.48885185570907297, 0.8444814776242603)
>>> response_entropy=entropy_calc(cm2.TOP,cm2.POP)
>>> response_entropy
1.486565953154142
>>> reference_entropy=entropy_calc(cm2.P,cm2.POP)
>>> reference_entropy
1.5304930567574824
>>> cross_entropy = cross_entropy_calc(cm2.TOP,cm2.P,cm2.POP)
>>> cross_entropy
1.5376219392005763
>>> join_entropy = joint_entropy_calc(cm2.classes,cm2.table,cm2.POP)
>>> join_entropy
2.619748965432189
>>> conditional_entropy = conditional_entropy_calc(cm2.classes,cm2.table,cm2.P,cm2.POP)
>>> conditional_entropy
1.089255908674706
>>> kl_divergence=kl_divergence_calc(cm2.P,cm2.TOP,cm2.POP)
>>> kl_divergence
0.007128882443093773
>>> lambda_B=lambda_B_calc(cm2.classes,cm2.table,cm2.TOP,population)
>>> lambda_B
0.35714285714285715
>>> lambda_A=lambda_A_calc(cm2.classes,cm2.table,cm2.P,population)
>>> lambda_A
0.4
>>> IS_calc(13,0,0,38)
1.5474877953024933
>>> weighted_kappa_calc(cm2.classes,cm2.table,cm2.P,cm2.TOP,cm2.POP,cm2.table)
-0.3883495145631068
>>> weighted_kappa_calc(cm2.classes,cm2.table,cm2.P,cm2.TOP,cm2.POP,{1:{1:2,2:2}})
'None'
>>> weighted_alpha_calc(cm2.classes,cm2.table,cm2.P,cm2.TOP,cm2.POP,cm2.table)
-0.5255636070853462
>>> weighted_alpha_calc(cm2.classes,cm2.table,cm2.P,cm2.TOP,cm2.POP,{1:{1:2,2:2}})
'None'
>>> kappa_no_prevalence_calc(cm2.Overall_ACC)
0.33333333333333326
>>> reliability_calc(cm2.Overall_RACC,cm2.Overall_ACC)
0.4740259740259741
>>> mutual_information_calc(cm2.ResponseEntropy,cm2.ConditionalEntropy)
0.39731004447943596
>>> cm3=ConfusionMatrix(matrix=cm2.table)
>>> cm3
pycm.ConfusionMatrix(classes: [0, 1, 2])
>>> cm3.CI95
(0.48885185570907297, 0.8444814776242603)
>>> cm3.Chi_Squared
15.525641025641026
>>> cm3.Phi_Squared
0.5750237416904084
>>> cm3.V
0.5362013342441477
>>> cm3.DF
4
>>> cm3.ResponseEntropy
1.486565953154142
>>> cm3.ReferenceEntropy
1.5304930567574824
>>> cm3.CrossEntropy
1.5376219392005763
>>> cm3.JointEntropy
2.619748965432189
>>> cm3.ConditionalEntropy
1.089255908674706
>>> cm3.KL
0.007128882443093773
>>> cm3.LambdaA
0.4
>>> cm3.LambdaB
0.35714285714285715
>>> cm4 = ConfusionMatrix(y_act,y_pre,classes=[1,2,0])
>>> cm4
pycm.ConfusionMatrix(classes: [1, 2, 0])
>>> cm4.classes
[1, 2, 0]
>>> cm4.to_array()
array([[5, 1, 3],
       [1, 4, 1],
       [3, 0, 9]])
>>> cm4 = ConfusionMatrix(y_act,y_pre,classes=[1,2])
>>> cm4
pycm.ConfusionMatrix(classes: [1, 2])
>>> cm4.classes
[1, 2]
>>> cm4.to_array()
array([[5, 1],
       [1, 4]])
>>> cm4 = ConfusionMatrix(["1",1,1,1],[1,2,1,1],classes=[1,2])
>>> cm4.to_array()
array([[3, 1],
       [0, 0]])
>>> cm4 = ConfusionMatrix([1,1,1,1],["1",2,1,1],classes=[1,2])
>>> cm4.to_array()
array([[3, 1],
       [0, 0]])
"""
