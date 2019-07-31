# -*- coding: utf-8 -*-
"""
>>> from pycm import *
>>> import os
>>> import json
>>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
>>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
>>> cm = ConfusionMatrix(y_actu, y_pred)
>>> cm.relabel({0:"L1",1:"L2",2:"L3"})
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
If you use PyCM in your research, please cite this paper :
<BLANKLINE>
https://doi.org/10.21105/joss.00729
<BLANKLINE>
<BLANKLINE>
Repo : https://github.com/sepandhaghighi/pycm
Webpage : https://www.pycm.ir
>>> rounder((1,2,"None"), digit=5)
'(1,2,None)'
>>> one_vs_all_func([1,2], {1:{1:0,2:0},2:{1:0,2:0}}, {1:0,2:0}, {1:0,2:0}, {1:0,2:0}, {1:0,2:0}, 3) == [[1, 2], {1: {1: 0, 2: 0}, 2: {1: 0, 2: 0}}]
True
>>> Q_calc(1,2,3,"None")
'None'
>>> AGM_calc(2,2,2,2,"None")
'None'
>>> BCD_calc(2, 2, "None")
'None'
>>> AM_calc(3, "None")
'None'
>>> RCI_calc(24,0)
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
>>> kappa_se_calc(2, 1, 2)
'None'
>>> CI_calc(23, "None", CV=1.96)
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
>>> ERR_calc(None)
'None'
>>> ERR_calc(0.1)
0.9
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
>>> del cm.classes
>>> del cm.TP
>>> cm.IBA_alpha(2)
{}
>>> cm.TI(2,3)
{}
>>> cm.F_beta(2)
{}
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
>>> PC_PI_calc(1,1,1)
'None'
>>> PC_PI_calc({1:12},{1:6},{1:45})
0.04000000000000001
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
>>> SE=se_calc(cm2.Overall_ACC,population)
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
>>> kappa_no_prevalence_calc(cm2.Overall_ACC)
0.33333333333333326
>>> reliability_calc(cm2.Overall_RACC,cm2.Overall_ACC)
0.4740259740259741
>>> mutual_information_calc(cm2.ResponseEntropy,cm2.ConditionalEntropy)
0.39731004447943596
>>> cm3=ConfusionMatrix(matrix=cm2.table)
>>> cm3
pycm.ConfusionMatrix(classes: [0, 1, 2])
>>> cm3.CI
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
7-AUC
8-AUCI
9-AUNP
10-AUNU
11-AUPR
12-BCD
13-BM
14-Bennett S
15-CBA
16-CEN
17-Chi-Squared
18-Chi-Squared DF
19-Conditional Entropy
20-Cramer V
21-Cross Entropy
22-DOR
23-DP
24-DPI
25-ERR
26-F0.5
27-F1
28-F1 Macro
29-F1 Micro
30-F2
31-FDR
32-FN
33-FNR
34-FOR
35-FP
36-FPR
37-G
38-GI
39-GM
40-Gwet AC1
41-Hamming Loss
42-IBA
43-IS
44-J
45-Joint Entropy
46-KL Divergence
47-Kappa
48-Kappa 95% CI
49-Kappa No Prevalence
50-Kappa Standard Error
51-Kappa Unbiased
52-LS
53-Lambda A
54-Lambda B
55-MCC
56-MCCI
57-MCEN
58-MK
59-Mutual Information
60-N
61-NIR
62-NLR
63-NLRI
64-NPV
65-OC
66-OOC
67-OP
68-Overall ACC
69-Overall CEN
70-Overall J
71-Overall MCC
72-Overall MCEN
73-Overall RACC
74-Overall RACCU
75-P
76-P-Value
77-PLR
78-PLRI
79-POP
80-PPV
81-PPV Macro
82-PPV Micro
83-PRE
84-Pearson C
85-Phi-Squared
86-Q
87-RACC
88-RACCU
89-RCI
90-RR
91-Reference Entropy
92-Response Entropy
93-SOA1(Landis & Koch)
94-SOA2(Fleiss)
95-SOA3(Altman)
96-SOA4(Cicchetti)
97-SOA5(Cramer)
98-SOA6(Matthews)
99-Scott PI
100-Standard Error
101-TN
102-TNR
103-TON
104-TOP
105-TP
106-TPR
107-TPR Macro
108-TPR Micro
109-Y
110-Zero-one Loss
111-dInd
112-sInd
>>> online_help("J")
...
>>> online_help("J",alt_link=True)
...
>>> online_help(4)
...
>>> NIR_calc({'Class2': 804, 'Class1': 196},1000) # Verified Case
0.804
>>> cm = ConfusionMatrix(matrix={0:{0:3,1:1},1:{0:4,1:2}})   # Verified Case
>>> cm.LS[1]
1.1111111111111112
>>> cm.LS[0]
1.0714285714285714
>>> cm = ConfusionMatrix(matrix={"Class1":{"Class1":183,"Class2":13},"Class2":{"Class1":141,"Class2":663}})  # Verified Case
>>> cm.PValue
0.000342386296143693
>>> cm = ConfusionMatrix(matrix={"Class1":{"Class1":4,"Class2":2},"Class2":{"Class1":2,"Class2":4}}) # Verified Case
>>> cm.Overall_CEN
0.861654166907052
>>> cm.Overall_MCEN
0.6666666666666666
>>> cm.IS["Class1"]
0.4150374992788437
>>> cm.IS["Class2"]
0.4150374992788437
>>> cm = ConfusionMatrix(matrix={1:{1:5,2:0,3:0},2:{1:0,2:10,3:0},3:{1:0,2:300,3:0}})  # Verified Case
>>> cm.Overall_CEN
0.022168905807495587
>>> cm.Overall_MCC
0.3012440235352457
>>> cm.CBA
0.3440860215053763
>>> cm = ConfusionMatrix(matrix={1:{1:1,2:3,3:0,4:0},2:{1:9,2:1,3:0,4:0},3:{1:0,2:0,3:100,4:0},4:{1:0,2:0,3:0,4:200}}) # Verified Case
>>> cm.RCI
0.9785616782831341
>>> cm = ConfusionMatrix(matrix={1:{1:1,2:0,3:3},2:{1:0,2:100,3:0},3:{1:0,2:0,3:200}}) # Verified Case
>>> cm.RCI
0.9264007150415143
>>> cm = ConfusionMatrix(matrix={1:{1:5,2:0,3:0},2:{1:0,2:10,3:0},3:{1:0,2:300,3:0}})
>>> cm.RCI
0.3675708571923818
>>> cm = ConfusionMatrix(matrix={1:{1:12806,2:26332},2:{1:5484,2:299777}},transpose=True) # Verified Case
>>> cm.AUC[1]
0.8097090079101759
>>> cm.GI[1]
0.6194180158203517
>>> cm.Overall_ACC
0.9076187793808925
>>> cm.DP[1]
0.7854399677022138
>>> cm.Y[1]
0.6194180158203517
>>> cm.BM[1]
0.6194180158203517
>>> cm = ConfusionMatrix(matrix={1:{1:13182,2:30516},2:{1:5108,2:295593}},transpose=True) # Verified Case
>>> cm.AUC[1]
0.8135728157964055
>>> cm.GI[1]
0.627145631592811
>>> cm.Overall_ACC
0.896561836706843
>>> cm.DP[1]
0.770700985610517
>>> cm.Y[1]
0.627145631592811
>>> cm.BM[1]
0.627145631592811
>>> cm = ConfusionMatrix(matrix={1:{1:60,2:9,3:1,4:0,5:0,6:0},2:{1:23,2:48,3:0,4:2,5:2,6:1},3:{1:11,2:5,3:1,4:0,5:0,6:0},4:{1:0,2:2,3:0,4:7,5:1,6:3},5:{1:2,2:1,3:0,4:0,5:4,6:2},6:{1:1,2:2,3:0,4:2,5:1,6:23}}) # Verified Case
>>> cm.AM[1]
27
>>> cm.BCD[1]
0.0630841121495327
>>> cm = ConfusionMatrix(matrix={1:{1:9,2:3,3:0},2:{1:3,2:5,3:1},3:{1:1,2:1,3:4}}) # Verified Case
>>> cm.CI
(0.48885185570907297, 0.8444814776242603)
>>> cm.SE
0.09072184232530289
>>> cm.Overall_RACC
0.36625514403292175
>>> cm.Kappa
0.4740259740259741
>>> cm.KappaNoPrevalence
0.33333333333333326
>>> cm.KappaUnbiased
0.4734561213434452
>>> cm.ReferenceEntropy
1.5304930567574824
>>> cm.ResponseEntropy
1.486565953154142
>>> cm.CrossEntropy
1.5376219392005763
>>> cm.ConditionalEntropy
1.089255908674706
>>> cm.MutualInformation
0.39731004447943596
>>> cm.KL
0.007128882443093773
>>> cm.Chi_Squared
15.525641025641026
>>> cm.Phi_Squared
0.5750237416904084
>>> cm.V
0.5362013342441477
>>> cm.LambdaA
0.4
>>> cm.LambdaB
0.35714285714285715
>>> cm.Overall_ACC
0.6666666666666666
>>> cm = ConfusionMatrix(matrix={1:{1:495,0:405},0:{0:8645,1:455}}) # Verified Case
>>> cm.ACC[1]
0.914
>>> cm.TNR[1]
0.95
>>> cm.TPR[1]
0.55
>>> cm.AUC[1]
0.75
>>> cm.AUPR[1]
0.5355263157894736
>>> cm.OP[1]
0.6473333333333334
>>> cm.IBA[1]
0.31350000000000006
>>> cm.IBA_alpha(0.5)[1]
0.41800000000000004
>>> cm.IBA_alpha(0.1)[1]
0.5016
>>> cm.GM[1]
0.722841614740048
>>> cm = ConfusionMatrix(matrix={1:{1:22,0:18},0:{1:2,0:14}}) # Verified Case
>>> cm.C
0.36170212765957444
>>> cm.Chi_Squared
8.429166666666667
>>> cm = ConfusionMatrix(matrix={0:{0:42,1:7},1:{1:114,0:203}}) # Verified Case
>>> cm.Q[0]
0.5422773393461104
>>> cm = ConfusionMatrix(matrix={1:{1:828,0:72},0:{0:8918,1:182}}) # Verified Case
>>> cm.AGM[1]
0.9640451296531609
>>> cm.GM[1]
0.9495261976375375
>>> cm = ConfusionMatrix(matrix={1:{1:882,0:18},0:{0:8372,1:728}}) # Verified Case
>>> cm.AGM[1]
0.935458742218606
>>> cm.GM[1]
0.9495261976375375
>>> cm = ConfusionMatrix([1,2,3,2,3,3,1,2,2],[2,2,1,2,1,3,2,3,2]) # Verified Case
>>> cm.F1_Macro
0.35555555555555557
>>> cm.F1_Micro
0.4444444444444444
>>> cm = ConfusionMatrix(matrix = {1:{1:5,0:1},0:{0:6,1:2}}) # Verified Case
>>> cm.AGF[1]
0.8197822947299411
>>> cm.F2[1]
0.8064516129032258
>>> cm.F05[0]
0.8333333333333334
>>> cm = ConfusionMatrix(matrix={1:{1:53,0:2},0:{1:5,0:44}})
>>> cm.OC[1]
0.9636363636363636
>>> cm.OOC[1]
0.9383838571303771
>>> cm = ConfusionMatrix(matrix={1:{1:63,0:1},0:{0:50,1:2}}) # Verified Case
>>> cm.TI(alpha=1,beta=1)[1]
0.9545454545454546
>>> cm.TI(alpha=0.5,beta=0.5)[1] == cm.F1[1]
True
>>> cm.TI(alpha=0.5,beta=0.5)[0] == cm.F1[0]
True
>>> cm.TI(alpha=2,beta=8)[1]
0.7777777777777778
>>> cm.TI(alpha=2,beta=8)[0]
0.8064516129032258
"""
