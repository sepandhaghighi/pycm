# -*- coding: utf-8 -*-

def MatrixParams(actual_vector,estimate_vector):
    classes=list(set(actual_vector).intersection(set(estimate_vector)))
    map_dict={k:0 for k in classes}
    TP_dict=map_dict.copy()
    TN_dict=map_dict.copy()
    FP_dict=map_dict.copy()
    FN_dict=map_dict.copy()
    classes_result={k:map_dict.copy() for k in classes}
    for index,item in enumerate(actual_vector):
        if (item in classes) and (estimate_vector[index] in classes):
            classes_result[item][estimate_vector[index]]+=1
            if item==estimate_vector[index]:
                TP_dict[item]+=1
            else:
                FN_dict[item]+=1
                FP_dict[estimate_vector[index]]+=1
            for i in classes:
                if i != item and estimate_vector[index]!=i :
                    TN_dict[i] += 1
    return [classes_result,TP_dict,TN_dict,FP_dict,FN_dict]


        

def ClassStatistic(Item1,Item2):
    result=Item1.copy()
    for i in Item1.keys():
        result[i]=Item1[i]/(Item1[i]+Item2[i])
    return result
