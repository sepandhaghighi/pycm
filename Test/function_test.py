# -*- coding: utf-8 -*-
"""
>>> from math import isclose
>>> from pycm import *
>>> from pycm.distance import DISTANCE_MAPPER
>>> import os
>>> import json
>>> import numpy as np
>>> ABS_TOL = 1e-12
>>> REL_TOL = 0
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
>>> cm.relabel({0: "L1", 1: "L2", 2: "L3"})
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
76-NPV Macro
77-NPV Micro
78-OC
79-OOC
80-OP
81-Overall ACC
82-Overall CEN
83-Overall J
84-Overall MCC
85-Overall MCEN
86-Overall RACC
87-Overall RACCU
88-P
89-P-Value
90-PLR
91-PLRI
92-POP
93-PPV
94-PPV Macro
95-PPV Micro
96-PR
97-PRE
98-Pearson C
99-Phi-Squared
100-Q
101-QI
102-RACC
103-RACCU
104-RCI
105-RR
106-Reference Entropy
107-Response Entropy
108-SOA1(Landis & Koch)
109-SOA2(Fleiss)
110-SOA3(Altman)
111-SOA4(Cicchetti)
112-SOA5(Cramer)
113-SOA6(Matthews)
114-SOA7(Lambda A)
115-SOA8(Lambda B)
116-SOA9(Krippendorff Alpha)
117-SOA10(Pearson C)
118-Scott PI
119-Standard Error
120-TN
121-TNR
122-TNR Macro
123-TNR Micro
124-TON
125-TOP
126-TOPR
127-TP
128-TPR
129-TPR Macro
130-TPR Micro
131-Y
132-Zero-one Loss
133-dInd
134-sInd
>>> online_help("J")
...
>>> online_help("J", alt_link=True)
...
>>> online_help(4)
...
>>> from pycm.output import *
>>> from pycm.overall_funcs import *
>>> from pycm.class_funcs import *
>>> from pycm.ci import *
>>> from pycm.interpret import *
>>> from pycm.utils import *
>>> color_check("red")
[255, 0, 0]
>>> color_check((255,2,2))
[255, 2, 2]
>>> color_check(None)
[0, 0, 0]
>>> color_check("wrong_color")
[0, 0, 0]
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
>>> assert isclose(inv_erf(-0.9999999999999749), -5.389154023751963, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(inv_erf(1.2490009027033011e-14), 1.1019786822020638e-14, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(inv_erf(0.3), 0.27246271472675443, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(inv_erf(0.8), 0.9061938024368231, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(inv_erf(0.22), 0.19750838337227367, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(complement(0.5), 0.5, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> complement("None")
'None'
>>> rounder((1, 2, "None"), digit=5)
'(1,2,None)'
>>> one_vs_all_func([1, 2], {1: {1: 0, 2: 0}, 2: {1: 0, 2: 0}}, {1: 0, 2: 0}, {1: 0, 2: 0}, {1: 0, 2: 0}, {1: 0, 2: 0}, 3) == ([1, 2], {1: {1: 0, 2: 0}, 2: {1: 0, 2: 0}})
True
>>> Q_calc(1, 2, 3, "None")
'None'
>>> AGM_calc(2, 2, 2, 2, "None")
'None'
>>> ARI_calc([1, 2], {1: {1: 0, 2: 0}, 2: {1: 0, 2: 0}}, {1: 0, 2: 0}, {1: 0, 2: 0}, 0)
'None'
>>> BCD_calc(2, "None")
'None'
>>> AM_calc(3, "None")
'None'
>>> RCI_calc(24, 0)
'None'
>>> BB_calc(0, 0, 0)
'None'
>>> CEN_calc([1, 2, 3], {1: {1: 0, 2: 0}, 2: {1: 0, 2: 0}}, {1: 2, 2: 3}, {1: 2, 2: 3}, 2, modified=False)
'None'
>>> convex_combination([1, 2, 3], {1: {1: 0, 2: 0}, 2: {1: 0, 2: 0}}, {1: 2, 2: 3}, {1: 2, 2: 3}, 2, modified=False)
'None'
>>> overall_CEN_calc([1, 2], {1: 2, 2: 3}, {1: 2, 2: 3}, {1: 2, 2: 3}, {1: 2, 2: "None"}, modified=False)
'None'
>>> NIR_calc({1: 0, 2: 0}, 0)
'None'
>>> hamming_calc({1: 0, 2: 0}, 0)
'None'
>>> zero_one_loss_calc({1: 0, 2: 0}, "None")
'None'
>>> entropy_calc({1: 0, 2: 0}, {1: 0, 2: 0})
'None'
>>> kappa_no_prevalence_calc("None")
'None'
>>> cross_entropy_calc({1: 0, 2: 0}, {1: 0, 2: 0}, {1: 0, 2: 0})
'None'
>>> joint_entropy_calc([1, 2], {1: {1: 0, 2: 0}, 2: {1: 0, 2: 0}}, {1: 0, 2: 0})
'None'
>>> conditional_entropy_calc([1, 2], {1: {1: 0, 2: 0}, 2: {1: 0, 2: 0}}, {1: 0, 2: 0}, {1: 0, 2: 0})
'None'
>>> mutual_information_calc(2, "None")
'None'
>>> lambda_B_calc([1, 2], {1: {1: 0, 2: 0}, 2: {1: 0, 2: 0}}, {1: 0, 2: 0}, {1: 0, 2: 0})
'None'
>>> lambda_A_calc([1, 2], {1: {1: 0, 2: 0}, 2: {1: 0, 2: 0}}, {1: 0, 2: 0}, {1: 0, 2: 0})
'None'
>>> DF_calc(2)
'None'
>>> kappa_SE_calc(2, 1, 2)
'None'
>>> CI_calc(23, "None", CV=1.96)
('None', 'None')
>>> CI_calc_agresti("None", 20, CV=1.96)
('None', 'None')
>>> CI_calc_wilson(200, 0, CV=1.96)
('None', 'None')
>>> CI_calc_wilson(200, "None", CV=1.96)
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
>>> overall_accuracy_calc({1: 0, 2: 0}, 0)
'None'
>>> overall_random_accuracy_calc({1: 0, 2: None})
'None'
>>> CBA_calc([1, 2], {1: {1: 0, 2: 0}, 2: {1: 0, 2: 0}}, {1: 0, 2: 0}, {1: 0, 2: 0})
'None'
>>> RR_calc([], {1: 0, 2: 0})
'None'
>>> overall_MCC_calc([1, 2], {1: {1: 0, 2: 0}, 2: {1: 0, 2: 0}}, {1: 0, 2: 0}, {1: 0, 2: 0})
'None'
>>> CEN_misclassification_calc({1: {1: 0, 2: 0}, 2: {1: 0, 2: 0}}, {1: 0, 2: 0}, {1: 0, 2: 0}, 1, 1, 2)
'None'
>>> assert isclose(brier_score_calc([1, 0], [0.8, 0.3, 0.2, 0.4], [1, 1, 0, 1], sample_weight=None, pos_class=None), 0.23249999999999998, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(log_loss_calc([1, 0], [0.8, 0.3, 0.2, 0.4], [1, 1, 0, 1], sample_weight=None, pos_class=None), 0.6416376597071276, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> brier_score_calc([1, "0"], [0.8, 0.3, 0.2, 0.4], [1, 1, 0, 1], sample_weight=None, pos_class=None)
'None'
>>> log_loss_calc([1, "0"], [0.8, 0.3, 0.2, 0.4], [1, 1, 0, 1], sample_weight=None, pos_class=None)
'None'
>>> vector_check([1, 2, 3, 0.4])
False
>>> vector_check([1, 2, 3,-2])
False
>>> matrix_check({1: {1: 0.5, 2: 0}, 2: {1: 0, 2: 0}})
False
>>> matrix_check([])
False
>>> TTPN_calc(0, 0)
'None'
>>> assert isclose(TTPN_calc(1, 4), 0.2, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> FXR_calc(None)
'None'
>>> assert isclose(FXR_calc(0.2), 0.8, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> ACC_calc(0, 0, 0, 0)
'None'
>>> assert isclose(ACC_calc(1, 1, 3, 4), 0.2222222222222222, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> MCC_calc(0, 2, 0, 2)
'None'
>>> assert isclose(MCC_calc(1, 2, 3, 4), -0.408248290463863, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(LR_calc(1, 2), 0.5, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> LR_calc(1, 0)
'None'
>>> MK_BM_calc(2, "None")
'None'
>>> MK_BM_calc(1, 2)
2
>>> proportion_calc(None, 2)
'None'
>>> assert isclose(proportion_calc(1, 5), 0.2, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> proportion_calc(1, 0)
'None'
>>> G_calc(None, 2)
'None'
>>> assert isclose(G_calc(1, 2), 1.4142135623730951, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(RACC_calc(2, 3, 4), 0.375, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> reliability_calc(1, None)
'None'
>>> assert isclose(reliability_calc(2, 0.3), 1.7, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(micro_calc({1: 2, 2: 3}, {1: 1, 2: 4}), 0.5, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> micro_calc({1: 2, 2: 3}, None)
'None'
>>> macro_calc(None)
'None'
>>> assert isclose(macro_calc({1: 2, 2: 3}), 2.5, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> F_calc(TP=0, FP=0, FN=0, beta=1)
'None'
>>> assert isclose(F_calc(TP=3, FP=2, FN=1, beta=5), 0.7428571428571429, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> TI_calc("None", 0, 0, 0, 0)
'None'
>>> NB_calc(1, 2, 4, "None")
'None'
>>> ERR_calc(None)
'None'
>>> assert isclose(ERR_calc(0.1), 0.9, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.average("F0.5"), 0.5612141481706698, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm.average("DOR")
'None'
>>> assert isclose(cm.average("DOR", none_omit=True), 2.9999999999999987, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.weighted_average("PPV"), 0.575, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.weighted_average("DOR", none_omit=True), 2.666666666666666, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm.weighted_average("DOR")
'None'
>>> assert isclose(cm.weighted_average("PPV", weight=cm.P), 0.575, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.weighted_average("PPV", weight={'L1': 0, 'L3': 0, 'L2': 1}), 0.5, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.weighted_average("PPV", weight={'L1': 0, 'L3': 1, 'L2': 1}), 0.55, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.weighted_average("PPV", weight={'L1': 1, 'L3': 0, 'L2': 1}), 0.55, abs_tol=ABS_TOL, rel_tol=REL_TOL)
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
>>> POS = cm.position()
>>> POS == cm.positions
True
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
>>> cm2.relabel({0: 'L1', 1: 'L2'})
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
>>> assert isclose(cm.F_beta(4)["L1"], 0.9622641509433962, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.F_beta(4)["L2"], 0.34, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.F_beta(4)["L3"], 0.504950495049505, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm.F_beta(None) == {'L3': 'None', 'L1': 'None', 'L2': 'None'}
True
>>> cm.IBA_alpha(None) == {'L3': 'None', 'L1': 'None', 'L2': 'None'}
True
>>> cm.relabel({"L1": "L4", "L2": "L5", "L3": "L6"})
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
>>> cm.TI(2, 3)
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
>>> lambda_analysis(0)
'None'
>>> lambda_analysis(0.1)
'Very Weak'
>>> lambda_analysis(0.3)
'Weak'
>>> lambda_analysis(0.5)
'Moderate'
>>> lambda_analysis(0.7)
'Strong'
>>> lambda_analysis(0.9)
'Very Strong'
>>> lambda_analysis(1)
'Perfect'
>>> alpha_analysis(0)
'Low'
>>> alpha_analysis(0.667)
'Tentative'
>>> alpha_analysis(0.8)
'High'
>>> pearson_C_analysis(0)
'None'
>>> pearson_C_analysis(0.05)
'Not Appreciable'
>>> pearson_C_analysis(0.1)
'Weak'
>>> pearson_C_analysis(0.2)
'Medium'
>>> pearson_C_analysis(0.3)
'Strong'
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
>>> PC_AC1_calc(1, 1, 1)
'None'
>>> assert isclose(PC_AC1_calc({1: 123, 2: 2}, {1: 120, 2: 5}, {1: 125, 2: 125}), 0.05443200000000002, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> y_act=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
>>> y_pre=[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 2, 0, 1, 2, 2, 2, 2]
>>> cm2=ConfusionMatrix(y_act, y_pre)
>>> chi_squared=chi_square_calc(cm2.classes, cm2.table, cm2.TOP, cm2.P, cm2.POP)
>>> assert isclose(chi_squared, 15.525641025641026, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> population = list(cm2.POP.values())[0]
>>> phi_squared=phi_square_calc(chi_squared, population)
>>> assert isclose(phi_squared, 0.5750237416904084, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> V=cramers_V_calc(phi_squared, cm2.classes)
>>> assert isclose(V, 0.5362013342441477, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> DF=DF_calc(cm2.classes)
>>> DF
4
>>> SE=SE_calc(cm2.Overall_ACC, population)
>>> assert isclose(SE, 0.09072184232530289, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> CI=CI_calc(cm2.Overall_ACC, SE)
>>> assert isclose(CI[0], 0.48885185570907297, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(CI[1], 0.8444814776242603, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> response_entropy=entropy_calc(cm2.TOP, cm2.POP)
>>> assert isclose(response_entropy, 1.486565953154142, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> reference_entropy=entropy_calc(cm2.P, cm2.POP)
>>> assert isclose(reference_entropy, 1.5304930567574824, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cross_entropy = cross_entropy_calc(cm2.TOP, cm2.P, cm2.POP)
>>> assert isclose(cross_entropy, 1.5376219392005763, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> join_entropy = joint_entropy_calc(cm2.classes, cm2.table, cm2.POP)
>>> assert isclose(join_entropy, 2.619748965432189, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> conditional_entropy = conditional_entropy_calc(cm2.classes, cm2.table, cm2.P, cm2.POP)
>>> assert isclose(conditional_entropy, 1.089255908674706, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> kl_divergence=kl_divergence_calc(cm2.P, cm2.TOP, cm2.POP)
>>> assert isclose(kl_divergence, 0.007128882443093773, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> lambda_B=lambda_B_calc(cm2.classes, cm2.table, cm2.TOP, population)
>>> assert isclose(lambda_B, 0.35714285714285715, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> lambda_A=lambda_A_calc(cm2.classes, cm2.table, cm2.P, population)
>>> assert isclose(lambda_A, 0.4, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(IS_calc(13, 0, 0, 38), 1.5474877953024933, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(weighted_kappa_calc(cm2.classes, cm2.table, cm2.P, cm2.TOP, cm2.POP, cm2.table), -0.3883495145631068, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> weighted_kappa_calc(cm2.classes, cm2.table, cm2.P, cm2.TOP, cm2.POP, {1: {1: 2, 2: 2}})
'None'
>>> assert isclose(weighted_alpha_calc(cm2.classes, cm2.table, cm2.P, cm2.TOP, cm2.POP, cm2.table), -0.5255636070853462, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> weighted_alpha_calc(cm2.classes, cm2.table, cm2.P, cm2.TOP, cm2.POP, {1: {1: 2, 2: 2}})
'None'
>>> assert isclose(kappa_no_prevalence_calc(cm2.Overall_ACC), 0.33333333333333326, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(reliability_calc(cm2.Overall_RACC, cm2.Overall_ACC), 0.4740259740259741, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(mutual_information_calc(cm2.ResponseEntropy, cm2.ConditionalEntropy), 0.39731004447943596, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm3=ConfusionMatrix(matrix=cm2.table)
>>> cm3
pycm.ConfusionMatrix(classes: [0, 1, 2])
>>> assert isclose(cm3.CI95[0], 0.48885185570907297, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm3.CI95[1], 0.8444814776242603, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm3.Chi_Squared, 15.525641025641026, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm3.Phi_Squared, 0.5750237416904084, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm3.V, 0.5362013342441477, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm3.DF
4
>>> assert isclose(cm3.ResponseEntropy, 1.486565953154142, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm3.ReferenceEntropy, 1.5304930567574824, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm3.CrossEntropy, 1.5376219392005763, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm3.JointEntropy, 2.619748965432189, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm3.ConditionalEntropy, 1.089255908674706, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm3.KL, 0.007128882443093773, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm3.LambdaA, 0.4, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm3.LambdaB, 0.35714285714285715, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm4 = ConfusionMatrix(y_act, y_pre, classes=[1, 2, 0])
>>> cm4
pycm.ConfusionMatrix(classes: [1, 2, 0])
>>> cm4.classes
[1, 2, 0]
>>> cm4.to_array()
array([[5, 1, 3],
       [1, 4, 1],
       [3, 0, 9]])
>>> cm4 = ConfusionMatrix(y_act, y_pre, classes=[1, 2])
>>> cm4
pycm.ConfusionMatrix(classes: [1, 2])
>>> cm4.classes
[1, 2]
>>> cm4.to_array()
array([[5, 1],
       [1, 4]])
>>> cm4 = ConfusionMatrix(["1", 1, 1, 1], [1, 2, 1, 1], classes=[1, 2])
>>> cm4.to_array()
array([[3, 1],
       [0, 0]])
>>> cm4 = ConfusionMatrix([1, 1, 1, 1], ["1", 2, 1, 1], classes=[1, 2])
>>> cm4.to_array()
array([[3, 1],
       [0, 0]])
>>> result = []
>>> for item in DISTANCE_MAPPER.values():
...     result.append(item(TP=2, TN=2, FP=1, FN="2"))
>>> all(list(map(lambda x: x=="None", result)))
True
"""
