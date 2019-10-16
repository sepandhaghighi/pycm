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
If you use PyCM in your research, we would appreciate citations to the following paper :
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
17-CSI
18-Chi-Squared
19-Chi-Squared DF
20-Conditional Entropy
21-Cramer V
22-Cross Entropy
23-DOR
24-DP
25-DPI
26-ERR
27-F0.5
28-F1
29-F1 Macro
30-F1 Micro
31-F2
32-FDR
33-FN
34-FNR
35-FOR
36-FP
37-FPR
38-G
39-GI
40-GM
41-Gwet AC1
42-Hamming Loss
43-IBA
44-ICSI
45-IS
46-J
47-Joint Entropy
48-KL Divergence
49-Kappa
50-Kappa 95% CI
51-Kappa No Prevalence
52-Kappa Standard Error
53-Kappa Unbiased
54-LS
55-Lambda A
56-Lambda B
57-MCC
58-MCCI
59-MCEN
60-MK
61-Mutual Information
62-N
63-NIR
64-NLR
65-NLRI
66-NPV
67-OC
68-OOC
69-OP
70-Overall ACC
71-Overall CEN
72-Overall J
73-Overall MCC
74-Overall MCEN
75-Overall RACC
76-Overall RACCU
77-P
78-P-Value
79-PLR
80-PLRI
81-POP
82-PPV
83-PPV Macro
84-PPV Micro
85-PRE
86-Pearson C
87-Phi-Squared
88-Q
89-RACC
90-RACCU
91-RCI
92-RR
93-Reference Entropy
94-Response Entropy
95-SOA1(Landis & Koch)
96-SOA2(Fleiss)
97-SOA3(Altman)
98-SOA4(Cicchetti)
99-SOA5(Cramer)
100-SOA6(Matthews)
101-Scott PI
102-Standard Error
103-TN
104-TNR
105-TON
106-TOP
107-TP
108-TPR
109-TPR Macro
110-TPR Micro
111-Y
112-Zero-one Loss
113-dInd
114-sInd
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
>>> cm.CI95
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
>>> cm = ConfusionMatrix(matrix={1:{1:22,0:54},0:{1:1,0:57}},transpose=True) # Verified Case
>>> cm.TPR[1]
0.9565217391304348
>>> cm.CI("TPR",0.05)[1][1][0]
0.8731774862637585
>>> cm.CI("TPR",0.05)[1][1][1]
1.0398659919971112
>>> cm.CI("TNR",0.05)[1][1][0]
0.4205300089203393
>>> cm.CI("TNR",0.05)[1][1][1]
0.6064970181066877
>>> cm.CI("PPV",0.05)[1][1][0]
0.18751037940411688
>>> cm.CI("PPV",0.05)[1][1][1]
0.3914369890169358
>>> cm.CI("NPV",0.05)[1][1][0]
0.9492581037307116
>>> cm.CI("NPV",0.05)[1][1][1]
1.0162591376485988
>>> cm.CI("Overall ACC",0.05)[1] == cm.CI95
True
>>> cm.CI("Kappa",0.05)[1]==cm.Kappa_CI
True
>>> cm.CI("TPR",0.01)[1][1][1]
1.0660599000409237
>>> cm.CI("TPR",0.01)[1][1][0]
0.8469835782199459
>>> cm.CI("TPR",0.02)[1][1][0]
0.8576142227182464
>>> cm.CI("TPR",0.02)[1][1][1]
1.0554292555426232
>>> cm.CI("TPR",0.1)[1][1][0]
0.8865720983316171
>>> cm.CI("TPR",0.1)[1][1][1]
1.0264713799292524
>>> cm.PLR[1]
1.966183574879227
>>> cm.NLR[1]
0.08466819221967958
>>> cm.CI("PLR")[1][1][1]
2.425775129875753
>>> cm.CI("PLR")[1][1][0]
1.5936670314213608
>>> cm.CI("NLR")[1][1][0]
0.012345468067066089
>>> cm.CI("NLR")[1][1][1]
0.5806748464136811
>>> cm.CI("PLR",0.01)[1][1][1]
2.591323998732794
>>> cm.CI("PLR",0.01)[1][1][0]
1.4918542999699553
>>> cm.CI("TPR",alpha=0.05,one_sided=True)[1][1][1]
1.0264713799292524
>>> cm.CI("TPR",alpha=0.1,one_sided=True)[1][1][1]
1.0109506389617338
>>> cm.CI("TPR",alpha=0.01,one_sided=True)[1][1][1]
1.0554292555426232
>>> cm.CI("TPR",alpha=0.005,one_sided=True)[1][1][1]
1.0660599000409237
>>> cm.CI("TPR",alpha=0.001,one_sided=True)[1][1][1]
1.0879165051294297
>>> cm.CI("TPR",alpha=0.0005,one_sided=True)[1][1][1]
1.0964210207280702
>>> cm.CI("ACC",alpha=0.05,one_sided=False)[1][1][1]
0.6728424118161956
>>> cm.CI("Overall ACC")[1][1] == cm.CI("ACC",alpha=0.05,one_sided=False)[1][1][1]
True
>>> cm.CI("FPR",0.05)[1][1][1]
0.5794699910796607
>>> cm.CI("FPR",0.05)[1][1][0]
0.39350298189331234
>>> cm.CI("FNR",0.05)[1][1][1]
0.12682251373624154
>>> cm.CI("FNR",0.05)[1][1][0]
-0.039865991997111175
>>> cm.CI("AUC")[1][1][0]
0.6361359326673304
>>> cm.CI("AUC")[1][1][1]
0.8338993199766178
>>> cm.CI("PRE")[1][1][0]
0.10779717474937288
>>> cm.CI("PRE")[1][1][1]
0.23548640734017934
>>> cm.CI("PRE",binom_method="wilson")[1][1][0]
0.11718265287943842
>>> cm.CI("PRE",binom_method="wilson")[1][1][1]
0.2444033995169354
>>> cm.CI("PRE",binom_method="agresti-coull")[1][1][0]
0.11654591925873323
>>> cm.CI("PRE",binom_method="agresti-coull")[1][1][1]
0.2450401331376406
>>> cm.CI("Overall ACC",binom_method="agresti-coull")[1][1]
0.6692525441184717
>>> cm.CI("Overall ACC",binom_method="agresti-coull")[1][0]
0.5048603506825172
>>> cm.CI("Overall ACC",binom_method="wilson")[1][1]
0.6692157009292735
>>> cm.CI("Overall ACC",binom_method="wilson")[1][0]
0.5048971938717156
>>> SE = AUC_SE_calc(0.88915,279,527) # Verified Case
>>> SE
0.011116012490627622
>>> CI_calc(0.88915,SE)[0]
0.8673626155183699
>>> CI_calc(0.88915,SE)[1]
0.9109373844816301
"""
