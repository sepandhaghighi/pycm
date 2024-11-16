# -*- coding: utf-8 -*-
"""
>>> import numpy as np
>>> from math import isclose
>>> from pycm import *
>>> from pycm.overall_funcs import NIR_calc
>>> from pycm.ci import AUC_SE_calc, CI_calc
>>> ABS_TOL = 1e-12
>>> REL_TOL = 0
>>> assert isclose(NIR_calc({'Class2': 804, 'Class1': 196}, 1000), 0.804, abs_tol=ABS_TOL, rel_tol=REL_TOL) # Verified Case - (Caret package)
>>> cm = ConfusionMatrix([2, 0, 2, 2, 0, 1], [0, 0, 2, 2, 0, 2]) # Verified Case - (https: //bit.ly/38nfMha)
>>> cm.print_matrix()
Predict 0       1       2
Actual
0       2       0       0
<BLANKLINE>
1       0       0       1
<BLANKLINE>
2       1       0       2
<BLANKLINE>
<BLANKLINE>
>>> cm = ConfusionMatrix(matrix={0: {0: 3, 1: 1}, 1: {0: 4, 1: 2}})   # Verified Case - (https: //bit.ly/2DHQvjn)
>>> assert isclose(cm.LS[1], 1.1111111111111112, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.LS[0], 1.0714285714285714, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={"Class1": {"Class1": 183, "Class2": 13}, "Class2": {"Class1": 141, "Class2": 663}})  # Verified Case - (Caret package)
>>> assert isclose(cm.PValue, 0.000342386296143693, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={"Class1": {"Class1": 4, "Class2": 2}, "Class2": {"Class1": 2, "Class2": 4}}) # Verified Case - (Delgado, Nunez-Gonzalez, 2018)
>>> assert isclose(cm.Overall_CEN, 0.861654166907052, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.Overall_MCEN, 0.6666666666666666, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.IS["Class1"], 0.4150374992788437, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.IS["Class2"], 0.4150374992788437, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 5, 2: 0, 3: 0}, 2: {1: 0, 2: 10, 3: 0}, 3: {1: 0, 2: 300, 3: 0}})  # Verified Case - (Delgado, Nunez-Gonzalez, 2018)
>>> assert isclose(cm.Overall_CEN, 0.022168905807495587, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.Overall_MCC, 0.3012440235352457, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CBA, 0.3440860215053763, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 1, 2: 3, 3: 0, 4: 0}, 2: {1: 9, 2: 1, 3: 0, 4: 0}, 3: {1: 0, 2: 0, 3: 100, 4: 0}, 4: {1: 0, 2: 0, 3: 0, 4: 200}}) # Verified Case - (Branco et al., 2017)
>>> assert isclose(cm.RCI, 0.9785616782831341, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 1, 2: 0, 3: 3}, 2: {1: 0, 2: 100, 3: 0}, 3: {1: 0, 2: 0, 3: 200}}) # Verified Case - (Branco et al., 2017)
>>> assert isclose(cm.RCI, 0.9264007150415143, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 5, 2: 0, 3: 0}, 2: {1: 0, 2: 10, 3: 0}, 3: {1: 0, 2: 300, 3: 0}})  # Verified Case - (Branco et al., 2017)
>>> assert isclose(cm.RCI, 0.3675708571923818, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 12806, 2: 26332}, 2: {1: 5484, 2: 299777}}, transpose=True) # Verified Case - (Bekkar et al., 2013)
>>> assert isclose(cm.AUC[1], 0.8097090079101759, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.GI[1], 0.6194180158203517, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.Overall_ACC, 0.9076187793808925, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.DP[1], 0.7854399677022138, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.Y[1], 0.6194180158203517, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.BM[1], 0.6194180158203517, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 13182, 2: 30516}, 2: {1: 5108, 2: 295593}}, transpose=True) # Verified Case - (Bekkar et al., 2013)
>>> assert isclose(cm.AUC[1], 0.8135728157964055, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.GI[1], 0.627145631592811, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.Overall_ACC, 0.896561836706843, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.DP[1], 0.770700985610517, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.Y[1], 0.627145631592811, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.BM[1], 0.627145631592811, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 60, 2: 9, 3: 1, 4: 0, 5: 0, 6: 0}, 2: {1: 23, 2: 48, 3: 0, 4: 2, 5: 2, 6: 1}, 3: {1: 11, 2: 5, 3: 1, 4: 0, 5: 0, 6: 0}, 4: {1: 0, 2: 2, 3: 0, 4: 7, 5: 1, 6: 3}, 5: {1: 2, 2: 1, 3: 0, 4: 0, 5: 4, 6: 2}, 6: {1: 1, 2: 2, 3: 0, 4: 2, 5: 1, 6: 23}}) # Verified Case - (https: //bit.ly/2YdvM01)
>>> cm.AM[1]
27
>>> assert isclose(cm.BCD[1], 0.0630841121495327, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 9, 2: 3, 3: 0}, 2: {1: 3, 2: 5, 3: 1}, 3: {1: 1, 2: 1, 3: 4}}) # Verified Case -- (https: //bit.ly/2r80R9t)
>>> assert isclose(cm.CI95[0], 0.48885185570907297, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI95[1], 0.8444814776242603, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.SE, 0.09072184232530289, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.Overall_RACC, 0.36625514403292175, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.Kappa, 0.4740259740259741, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.KappaNoPrevalence, 0.33333333333333326, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.KappaUnbiased, 0.4734561213434452, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.ReferenceEntropy, 1.5304930567574824, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.ResponseEntropy, 1.486565953154142, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CrossEntropy, 1.5376219392005763, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.ConditionalEntropy, 1.089255908674706, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.MutualInformation, 0.39731004447943596, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.KL, 0.007128882443093773, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.Chi_Squared, 15.525641025641026, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.Phi_Squared, 0.5750237416904084, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.V, 0.5362013342441477, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.LambdaA, 0.4, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.LambdaB, 0.35714285714285715, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.Overall_ACC, 0.6666666666666666, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 495, 0: 405}, 0: {0: 8645, 1: 455}}) # Verified Case - (Garcia et al., 2009)
>>> assert isclose(cm.ACC[1], 0.914, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.TNR[1], 0.95, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.TPR[1], 0.55, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.AUC[1], 0.75, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.AUPR[1], 0.5355263157894736, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.OP[1], 0.6473333333333334, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.IBA[1], 0.31350000000000006, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.IBA_alpha(0.5)[1], 0.41800000000000004, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.IBA_alpha(0.1)[1], 0.5016, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.GM[1], 0.722841614740048, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 22, 0: 18}, 0: {1: 2, 0: 14}}) # Verified Case - (https: //bit.ly/2LiCZXB)
>>> assert isclose(cm.C, 0.36170212765957444, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.Chi_Squared, 8.429166666666667, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={0: {0: 42, 1: 7}, 1: {1: 114, 0: 203}}) # Verified Case - (https: //bit.ly/2LiCZXB)
>>> assert isclose(cm.Q[0], 0.5422773393461104, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={0: {0: 27, 1: 10}, 1: {0: 16, 1: 15}})  # Verified Case - (https: //bit.ly/2skyjKG)
>>> assert isclose(cm.Q[0], 0.4336283185840708, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm.QI[0]
'Weak'
>>> cm = ConfusionMatrix(matrix={1: {1: 828, 0: 72}, 0: {0: 8918, 1: 182}}) # Verified Case - (Batuwita, Palade, 2009)
>>> assert isclose(cm.AGM[1], 0.9640451296531609, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.GM[1], 0.9495261976375375, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 882, 0: 18}, 0: {0: 8372, 1: 728}}) # Verified Case - (Batuwita, Palade, 2009)
>>> assert isclose(cm.AGM[1], 0.935458742218606, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.GM[1], 0.9495261976375375, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix([1, 2, 3, 2, 3, 3, 1, 2, 2], [2, 2, 1, 2, 1, 3, 2, 3, 2])
>>> assert isclose(cm.F1_Macro, 0.35555555555555557, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.F1_Micro, 0.4444444444444444, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix = {1: {1: 5, 0: 1}, 0: {0: 6, 1: 2}})
>>> assert isclose(cm.AGF[1], 0.8197822947299411, abs_tol=ABS_TOL, rel_tol=REL_TOL)

>>> assert isclose(cm.F2[1], 0.8064516129032258, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.F05[0], 0.8333333333333334, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 53, 0: 2}, 0: {1: 5, 0: 44}})
>>> assert isclose(cm.OC[1], 0.9636363636363636, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.OOC[1], 0.9383838571303771, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 63, 0: 1}, 0: {0: 50, 1: 2}})
>>> assert isclose(cm.TI(alpha=1, beta=1)[1], 0.9545454545454546, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm.TI(alpha=0.5, beta=0.5)[1] == cm.F1[1]
True
>>> cm.TI(alpha=0.5, beta=0.5)[0] == cm.F1[0]
True
>>> assert isclose(cm.TI(alpha=2, beta=8)[1], 0.7777777777777778, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.TI(alpha=2, beta=8)[0], 0.8064516129032258, abs_tol=ABS_TOL, rel_tol=REL_TOL)

>>> cm = ConfusionMatrix(matrix={1: {1: 22, 0: 54}, 0: {1: 1, 0: 57}}, transpose=True) # Verified Case -- (https: //bit.ly/34KcVfB)
>>> assert isclose(cm.TPR[1], 0.9565217391304348, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("TPR", 0.05)[1][1][0], 0.8731774862637585, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("TPR", 0.05)[1][1][1], 1.0398659919971112, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("TNR", 0.05)[1][1][0], 0.4205300089203393, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("TNR", 0.05)[1][1][1], 0.6064970181066877, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("PPV", 0.05)[1][1][0], 0.18751037940411688, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("PPV", 0.05)[1][1][1], 0.3914369890169358, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("NPV", 0.05)[1][1][0], 0.9492581037307116, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("NPV", 0.05)[1][1][1], 1.0162591376485988, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm.CI("Overall ACC", 0.05)[1] == cm.CI95
True
>>> cm.CI("Kappa", 0.05)[1]==cm.Kappa_CI
True
>>> assert isclose(cm.CI("TPR", 0.01)[1][1][1], 1.0660599000409237, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("TPR", 0.01)[1][1][0], 0.8469835782199459, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("TPR", 0.02)[1][1][0], 0.8576142227182464, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("TPR", 0.02)[1][1][1], 1.0554292555426232, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("TPR", 0.1)[1][1][0], 0.8865720983316171, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("TPR", 0.1)[1][1][1], 1.0264713799292524, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.PLR[1], 1.966183574879227, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.NLR[1], 0.08466819221967958, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("PLR")[1][1][1], 2.425775129875753, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("PLR")[1][1][0], 1.5936670314213608, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("NLR")[1][1][0], 0.012345468067066089, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("NLR")[1][1][1], 0.5806748464136811, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("PLR", 0.01)[1][1][1], 2.591323998732794, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("PLR", 0.01)[1][1][0], 1.4918542999699553, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("TPR", alpha=0.05, one_sided=True)[1][1][1], 1.0264713799292524, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("TPR", alpha=0.1, one_sided=True)[1][1][1], 1.0109506389617338, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("TPR", alpha=0.01, one_sided=True)[1][1][1], 1.0554292555426232, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("TPR", alpha=0.005, one_sided=True)[1][1][1], 1.0660599000409237, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("TPR", alpha=0.001, one_sided=True)[1][1][1], 1.0879165051294297, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("TPR", alpha=0.0005, one_sided=True)[1][1][1], 1.0964210207280702, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("ACC", alpha=0.05, one_sided=False)[1][1][1], 0.6728424118161956, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm.CI("Overall ACC")[1][1] == cm.CI("ACC", alpha=0.05, one_sided=False)[1][1][1]
True
>>> assert isclose(cm.CI("FPR", 0.05)[1][1][1], 0.5794699910796607, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("FPR", 0.05)[1][1][0], 0.39350298189331234, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("FNR", 0.05)[1][1][1], 0.12682251373624154, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("FNR", 0.05)[1][1][0], -0.039865991997111175, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("AUC")[1][1][0], 0.6361359326673304, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("AUC")[1][1][1], 0.8338993199766178, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("PRE")[1][1][0], 0.10779717474937288, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("PRE")[1][1][1], 0.23548640734017934, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("PRE", binom_method="wilson")[1][1][0], 0.11718265287943842, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("PRE", binom_method="wilson")[1][1][1], 0.2444033995169354, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("PRE", binom_method="agresti-coull")[1][1][0], 0.11654591925873323, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("PRE", binom_method="agresti-coull")[1][1][1], 0.2450401331376406, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("Overall ACC", binom_method="agresti-coull")[1][1], 0.6692525441184717, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("Overall ACC", binom_method="agresti-coull")[1][0], 0.5048603506825172, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("Overall ACC", binom_method="wilson")[1][1], 0.6692157009292735, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.CI("Overall ACC", binom_method="wilson")[1][0], 0.5048971938717156, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> SE = AUC_SE_calc(0.88915, 279, 527) # Verified Case -- (https: //bit.ly/2qblMrE)
>>> assert isclose(SE, 0.011116012490627622, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(CI_calc(0.88915, SE)[0], 0.8673626155183699, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(CI_calc(0.88915, SE)[1], 0.9109373844816301, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 135, 0: 48}, 0: {0: 2014, 1: 1067}}) # Verified Case -- (Steyerberg et al., 2011, p. 792)
>>> cm.TP[1]
135
>>> cm.FP[1]
1067
>>> cm.POP[1]
3264
>>> assert isclose(cm.NB(w=0.059)[1], 0.022073223039215686, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 3, 2: 0, 3: 1}, 2: {1: 1, 2: 2, 3: 1}, 3: {1: 0, 2: 2, 3: 2}})  # Verified Case -- (https: //bit.ly/2ur7Rj4)
>>> assert isclose(cm.ARI, 0.08333333333333333, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix([0, 0, 1, 1], [0, 0, 1, 1]) # Verified Case -- (https: //bit.ly/30PNzvL)
>>> assert isclose(cm.ARI, 1.0, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix([0, 0, 1, 2], [0, 0, 1, 1]) # Verified Case -- (https: //bit.ly/30PNzvL)
>>> assert isclose(cm.ARI, 0.5714285714285715, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix([0, 1, 2, 0, 1, 2], [0, 2, 1, 0, 0, 1]) # Verified Case -- (https: //bit.ly/3egZBEG)
>>> assert isclose(cm.weighted_average("F1"), 0.26666666666666666, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix([0, 1, 2, 2, 2], [0, 0, 2, 2, 1]) # Verified Case -- (https: //bit.ly/2yidCBo)
>>> assert isclose(cm.average("PPV"), 0.5, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.average("TPR"), 0.5555555555555555, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.average("F1"), 0.4888888888888889, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.weighted_average("PPV"), 0.7, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.weighted_average("TPR"), 0.6, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.weighted_average("F1"), 0.6133333333333334, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={"often": {"often": 16, "seldom": 6, "never": 2}, "seldom": {"often": 4, "seldom": 10, "never": 1}, "never": {"often": 3, "seldom": 0, "never": 8}}) # Verified Case -- (https: //bit.ly/3btZm7z)
>>> weighted_kappa = cm.weighted_kappa(weight={"often": {"often": 0, "seldom": 1, "never": 2}, "seldom": {"often": 1, "seldom": 0, "never": 1}, "never": {"often": 2, "seldom": 1, "never": 0}})
>>> assert isclose(weighted_kappa, 0.5009505703422054, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> weighted_kappa = cm.weighted_kappa(weight={"often": {"often": 0, "seldom": 1, "never": 1}, "seldom": {"often": 1, "seldom": 0, "never": 1}, "never": {"often": 1, "seldom": 1, "never": 0}})
>>> assert isclose(weighted_kappa, 0.49590422180214233, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 60, 2: 10}, 2: {1: 10, 2: 20}}) # Verified Case -- (Warrens, Raadt, 2019)
>>> assert isclose(cm.B, 0.6896551724137931, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 10, 2: 10, 3: 0}, 2: {1: 10, 2: 10, 3: 0}, 3: {1: 0, 2: 0, 3: 60}}) # Verified Case -- (Warrens, Raadt, 2019)
>>> assert isclose(cm.B, 0.8636363636363636, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 13, 2: 0, 3: 0}, 2: {1: 0, 2: 20, 3: 7}, 3: {1: 0, 2: 4, 3: 56}}) # Verified Case -- (https: //bit.ly/3fWUuKF)
>>> assert isclose(cm.Alpha, 0.7972584977308513, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> weighted_alpha = cm.weighted_alpha(weight={1: {1: 0, 2: 1, 3: 1}, 2: {1: 1, 2: 0, 3: 1}, 3: {1: 1, 2: 1, 3: 0}})
>>> assert isclose(weighted_alpha, 0.7972584977308516, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.Kappa, 0.7964094021839719, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.PI, 0.7962396962119107, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm.AC1, 0.8493305482313461, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 55, 2: 10, 3: 2}, 2: {1: 6, 2: 4, 3: 10}, 3: {1: 2, 2: 5, 3: 6}}) # Verified Case -- (Gwet, Kilem L. Handbook of inter-rater reliability, 2014)
>>> assert isclose(cm.aickin_alpha(), 0.40455288947232665, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm = ConfusionMatrix(matrix={1: {1: 60, 0: 40}, 0: {0: 80, 1: 20}}) # Verified Case -- (https: //bit.ly/3ooCi0t)
>>> assert isclose(cm.sensitivity_index()[1], 1.094968336708714, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> y_true = np.array([0, 1, 1, 0])
>>> y_true_categorical = np.array(["spam", "ham", "ham", "spam"])
>>> y_prob = np.array([0.1, 0.9, 0.8, 0.3])
>>> cm1 = ConfusionMatrix(y_true, y_prob, threshold=lambda x: 1) # Verified Case -- (https: //bit.ly/3n8Uo7R)
>>> assert isclose(cm1.brier_score(), 0.03749999999999999, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.brier_score(pos_class=1), 0.03749999999999999, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm2 = ConfusionMatrix(y_true, 1-y_prob, threshold=lambda x: 1) # Verified Case -- (https: //bit.ly/3n8Uo7R)
>>> assert isclose(cm2.brier_score(pos_class=0), 0.0375, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm3 = ConfusionMatrix(y_true_categorical, y_prob, threshold=lambda x: "ham") # Verified Case -- (https: //bit.ly/3n8Uo7R)
>>> assert isclose(cm3.brier_score(pos_class="ham"), 0.03749999999999999, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm4 = ConfusionMatrix(y_true, y_prob, sample_weight=[2, 2, 3, 3], threshold=lambda x: 1)
>>> assert isclose(cm4.brier_score(), 0.043, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm5 = ConfusionMatrix(y_true, np.array(y_prob) > 0.5, threshold=lambda x: 1) # Verified Case -- (https: //bit.ly/3n8Uo7R)
>>> assert isclose(cm5.brier_score(), 0.0, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> y_true = np.array([0, 1, 1, 0])
>>> y_true_categorical = np.array(["spam", "ham", "ham", "spam"])
>>> y_prob = np.array([0.1, 0.9, 0.8, 0.35])
>>> cm1 = ConfusionMatrix(y_true, y_prob, threshold=lambda x: 1) # Verified Case -- (https://bit.ly/420uyVW)
>>> assert isclose(cm1.log_loss(), 0.21616187468057912, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.log_loss(pos_class=1), 0.21616187468057912, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm2 = ConfusionMatrix(y_true, 1-y_prob, threshold=lambda x: 1) # Verified Case -- (https://bit.ly/420uyVW)
>>> assert isclose(cm2.log_loss(pos_class=0), 0.21616187468057912, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm3 = ConfusionMatrix(y_true_categorical, y_prob, threshold=lambda x: "ham") # Verified Case -- (https://bit.ly/420uyVW)
>>> assert isclose(cm3.log_loss(pos_class="ham"), 0.21616187468057912, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm3.log_loss(pos_class="ham", normalize=False), 0.8646474987223165, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm4 = ConfusionMatrix(y_true, y_prob, sample_weight=[2, 2, 3, 3], threshold=lambda x: 1) # Verified Case -- (https://bit.ly/420uyVW)
>>> assert isclose(cm4.log_loss(), 0.2383221464851297, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm4.log_loss(normalize=False), 2.383221464851297, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> y1 = [1, 1, 0, 0, 0, 1]
>>> y2 = [1, 0, 1, 1, 0, 1]
>>> cm1 = ConfusionMatrix(y1, y2) # Verified Case -- (https: //bit.ly/3OWrZ00)
>>> cm1.HD[1]
3
>>> cm1.HD[0]
3
>>> y1 = [1, 1, 0, 1, 0, 0, 1, 1, 1, 1]
>>> y2 = [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
>>> cm2 = ConfusionMatrix(y1, y2) # Verified Case -- (https: //bit.ly/3zVWUoV)
>>> cm2.HD[1]
5
>>> cm2.HD[0]
5
>>> cm1 = ConfusionMatrix(matrix = {1: {1: 2, 0: 2}, 0: {0: 778, 1: 2}})  # Verified Case -- (https: //bit.ly/3BVdNBp)
>>> assert isclose(cm1.BB[1], 0.5, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> cm2 = ConfusionMatrix(matrix = {1: {1: 2, 0: 3}, 0: {0: 775, 1: 4}})  # Verified Case -- (https: //bit.ly/3BVdNBp)
>>> assert isclose(cm2.BB[1], 0.3333333333333333, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> crv = Curve(actual_vector = np.array([1, 1, 2, 2]), probs = np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1])  # Verified Case -- (https: //bit.ly/3MIMk9z)
>>> crv.thresholds
[0.1, 0.2, 0.35, 0.4, 0.6, 0.65, 0.8, 0.9]
>>> crv.data[2]["TPR"]
[1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.0]
>>> crv.data[2]["FPR"]
[1.0, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0]
>>> crv = ROCCurve(actual_vector = np.array([1, 1, 2, 2]), probs = np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1]) # Verified Case -- (https: //bit.ly/2Hqg0Ix)
>>> crv.thresholds
[0.1, 0.2, 0.35, 0.4, 0.6, 0.65, 0.8, 0.9]
>>> crv.data[2]["TPR"]
[1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.0, 0]
>>> crv.data[2]["FPR"]
[1.0, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0]
>>> abs(crv.area()[2] - 0.75) < 0.001
True
>>> abs(crv.area(method="midpoint")[1]-0.75) < 0.001
True
>>> abs(crv.area(method="midpoint")[2]-0.75) < 0.001
True
>>> crv = PRCurve(actual_vector = np.array([1, 1, 2, 2]), probs = np.array([[0.1, 0.9], [0.4, 0.6], [0.35, 0.65], [0.8, 0.2]]), classes=[2, 1]) # Verified Case -- (https: //bit.ly/2PqUeKx)
>>> crv.data[2]["TPR"]
[1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 0.5]
>>> crv.data[2]["PPV"]
[0.5, 0.6666666666666666, 0.6666666666666666, 0.5, 1.0, 1.0, 1.0]
>>> abs(crv.area()[2] - 0.2916) < 0.001      # Verified Case -- (https: //bit.ly/2Hqg0Ix)
True
>>> abs(crv.area(method="midpoint")[2] - 0.2916) < 0.001
True
>>> cm1 = ConfusionMatrix(matrix = {1: {1: 2, 0: 2}, 0: {0: 778, 1: 2}})  # Verified Case -- (https: //bit.ly/3vVMWRT)
>>> cm2 = ConfusionMatrix(matrix = {1: {1: 2, 0: 3}, 0: {0: 775, 1: 4}})  # Verified Case -- (https: //bit.ly/3vVMWRT)
>>> assert isclose(cm1.distance(metric=DistanceType.AMPLE)[1], 0.49743589743589745, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.AMPLE)[1], 0.32947729220222793, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.Anderberg)[1], 0.0, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.Anderberg)[1], 0.0, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.AndresMarzoDelta)[1], 0.9897959183673469, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.AndresMarzoDelta)[1], 0.9822344346552608, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaroniUrbaniBuserI)[1], 0.9119837740878104, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaroniUrbaniBuserI)[1], 0.8552823175014205, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaroniUrbaniBuserII)[1], 0.8239675481756209, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaroniUrbaniBuserII)[1], 0.7105646350028408, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BatageljBren)[1], 0.002570694087403599, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BatageljBren)[1], 0.007741935483870968, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaulieuI)[1], 0.75, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaulieuI)[1], 0.8666666666666667, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaulieuII)[1], 0.24871959237343852, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaulieuII)[1], 0.13213719608444902, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaulieuIII)[1], 0.4949500208246564, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaulieuIII)[1], 0.4949955747605165, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaulieuIV)[1], -5249.96272285802, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaulieuIV)[1], -5209.561726488335, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaulieuV)[1], 0.7142857142857143, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaulieuV)[1], 0.8, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaulieuVI)[1], 0.5714285714285714, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaulieuVI)[1], 0.7, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaulieuVII)[1], 0.005050505050505051, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaulieuVII)[1], 0.008838383838383838, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaulieuVIII)[1], 0.0, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaulieuVIII)[1], 1.6269262807163682e-06, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaulieuIX)[1], 0.007633587786259542, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaulieuIX)[1], 0.012706480304955527, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaulieuX)[1], 0.007633587786259542, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaulieuX)[1], 0.013959390862944163, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaulieuXI)[1], 0.005115089514066497, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaulieuXI)[1], 0.008951406649616368, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaulieuXII)[1], 0.8, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaulieuXII)[1], 0.875, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaulieuXIII)[1], 0.2857142857142857, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaulieuXIII)[1], 0.4117647058823529, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaulieuXIV)[1], 0.75, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaulieuXIV)[1], 0.8333333333333334, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BaulieuXV)[1], 0.75, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BaulieuXV)[1], 0.8461538461538461, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BeniniI)[1], 0.49743589743589745, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BeniniI)[1], 0.3953727506426735, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.BeniniII)[1], 0.49743589743589745, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.BeniniII)[1], 0.3953727506426735, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.Canberra)[1], 0.5, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.Canberra)[1], 0.6363636363636364, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.Clement)[1], 0.5025379382522239, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.Clement)[1], 0.33840586363079933, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.ConsonniTodeschiniI)[1], 0.9992336018090547, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.ConsonniTodeschiniI)[1], 0.998656222829757, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.ConsonniTodeschiniII)[1], 0.7585487129939101, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.ConsonniTodeschiniII)[1], 0.6880377723094788, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.ConsonniTodeschiniIII)[1], 0.16481614417697044, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.ConsonniTodeschiniIII)[1], 0.16481614417697044, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.ConsonniTodeschiniIV)[1], 0.5645750340535797, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.ConsonniTodeschiniIV)[1], 0.47712125471966244, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.ConsonniTodeschiniV)[1], 0.48072545510682463, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.ConsonniTodeschiniV)[1], 0.4003930264973547, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.Dennis)[1], 13.857142857142858, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.Dennis)[1], 10.028539207654113, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.Digby)[1], 0.9774244829419212, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.Digby)[1], 0.9491281473458171, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.Dispersion)[1], 0.002524989587671803, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.Dispersion)[1], 0.002502212619741774, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.Doolittle)[1], 0.24744247205785666, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.Doolittle)[1], 0.13009912077202224, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.Eyraud)[1], -1.438198553583169e-06, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.Eyraud)[1], -1.5399964580081465e-06, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.FagerMcGowan)[1], 0.25, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.FagerMcGowan)[1], 0.16102422643817918, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.Faith)[1], 0.4987244897959184, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.Faith)[1], 0.4968112244897959, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.FleissLevinPaik)[1], 0.9974358974358974, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.FleissLevinPaik)[1], 0.9955041746949261, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.ForbesI)[1], 98.0, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.ForbesI)[1], 52.266666666666666, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.ForbesII)[1], 0.49743589743589745, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.ForbesII)[1], 0.3953727506426735, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.Fossum)[1], 110.25, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.Fossum)[1], 58.8, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.GilbertWells)[1], 20.176174477346354, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.GilbertWells)[1], 16.717742356979358, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.Goodall)[1], 0.9544884026871964, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.Goodall)[1], 0.9397552079794624, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.GoodmanKruskalLambda)[1], 0.0, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.GoodmanKruskalLambda)[1], 0.0, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.GoodmanKruskalLambdaR)[1], 0.0, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.GoodmanKruskalLambdaR)[1], -0.2727272727272727, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.GuttmanLambdaA)[1], 0.0, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.GuttmanLambdaA)[1], 0.0, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.GuttmanLambdaB)[1], 0.0, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.GuttmanLambdaB)[1], 0.0, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.Hamann)[1], 0.9897959183673469, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.Hamann)[1], 0.9821428571428571, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.HarrisLahey)[1], 0.3367085964820711, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.HarrisLahey)[1], 0.22761577457069784, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.HawkinsDotson)[1], 0.6641091219096334, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.HawkinsDotson)[1], 0.606635407786303, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.KendallTau)[1], 0.0025282143508744493, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.KendallTau)[1], 0.00250866630176975, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.KentFosterI)[1], -0.19999999999999996, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.KentFosterI)[1], -0.23529411764705888, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.KentFosterII)[1], -0.0012804097311239404, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.KentFosterII)[1], -0.002196997436837158, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.KoppenI)[1], 0.9993589743589744, abs_tol=ABS_TOL, rel_tol=REL_TOL) # normalizer: None
>>> assert isclose(cm2.distance(metric=DistanceType.KoppenI)[1], 0.9991825772172593, abs_tol=ABS_TOL, rel_tol=REL_TOL) # normalizer: None
>>> assert isclose(cm1.distance(metric=DistanceType.KoppenII)[1], 4.0, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.KoppenII)[1], 5.5, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.KuderRichardson)[1], 0.6643835616438356, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.KuderRichardson)[1], 0.5285677463699631, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.KuhnsI)[1], 0.005049979175343606, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.KuhnsI)[1], 0.005004425239483548, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.KuhnsII)[1], 0.49489795918367346, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.KuhnsII)[1], 0.32695578231292516, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.KuhnsIII)[1], 0.3307757885763001, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.KuhnsIII)[1], 0.21873141468207793, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.KuhnsIV)[1], 0.49489795918367346, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.KuhnsIV)[1], 0.3923469387755102, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.KuhnsV)[1], 0.497435897435897, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.KuhnsV)[1], 0.329477292202228, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.KuhnsVI)[1], 0.497435897435897, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.KuhnsVI)[1], 0.394865211810013, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm1.distance(metric=DistanceType.KuhnsVII)[1], 0.49489795918367346, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> assert isclose(cm2.distance(metric=DistanceType.KuhnsVII)[1], 0.3581621145590755, abs_tol=ABS_TOL, rel_tol=REL_TOL)
>>> mlcm = MultiLabelCM(actual_vector=[{"cat", "bird"}, {"dog"}], predict_vector=[{"cat"}, {"dog", "bird"}], classes=["cat", "dog", "bird"]) # Verified Case -- (http://bitly.ws/GNq2)
>>> mlcm.actual_vector_multihot
[[1, 0, 1], [0, 1, 0]]
>>> mlcm.predict_vector_multihot
[[1, 0, 0], [0, 1, 1]]
>>> mlcm.get_cm_by_class("cat").print_matrix()
Predict 0       1
Actual
0       1       0
<BLANKLINE>
1       0       1
<BLANKLINE>
<BLANKLINE>
>>> mlcm.get_cm_by_class("dog").print_matrix()
Predict 0       1
Actual
0       1       0
<BLANKLINE>
1       0       1
<BLANKLINE>
<BLANKLINE>
>>> mlcm.get_cm_by_class("bird").print_matrix()
Predict 0       1
Actual
0       0       1
<BLANKLINE>
1       1       0
<BLANKLINE>
<BLANKLINE>
>>> mlcm.get_cm_by_sample(0).print_matrix()
Predict 0       1
Actual
0       1       0
<BLANKLINE>
1       1       1
<BLANKLINE>
<BLANKLINE>
>>> mlcm.get_cm_by_sample(1).print_matrix()
Predict 0       1
Actual
0       1       1
<BLANKLINE>
1       0       1
<BLANKLINE>
<BLANKLINE>
"""
