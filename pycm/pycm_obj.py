# -*- coding: utf-8 -*-

from .pycm_func import *
from .pycm_output import *
import os
import json
import types
import numpy


class pycmVectorError(Exception):
    pass


class pycmMatrixError(Exception):
    pass


class ConfusionMatrix():
    '''
    Main Class Of ConfusionMatrix
    >>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
    >>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
    >>> cm = ConfusionMatrix(y_actu, y_pred)
    >>> cm.classes
    [0, 1, 2]
    >>> cm.table
    {0: {0: 3, 1: 0, 2: 0}, 1: {0: 0, 1: 1, 2: 2}, 2: {0: 2, 1: 1, 2: 3}}
    >>> cm2 = ConfusionMatrix(matrix={"Class1": {"Class1": 1, "Class2":2},"Class2": {"Class1": 0, "Class2": 5}})
    >>> cm2
    pycm.ConfusionMatrix(classes: ['Class1', 'Class2'])
    '''

    def __init__(
            self,
            actual_vector=None,
            predict_vector=None,
            matrix=None,
            digit=5, threshold=None, file=None,
            sample_weight=None, transpose=False):
        '''
        :param actual_vector: Actual Vector
        :type actual_vector: python list or numpy array of any stringable objects
        :param predict_vector: Predicted Vector
        :type predict_vector: python list or numpy array of any stringable objects
        :param matrix: direct matrix
        :type matrix: dictionary
        :type matrix: dict
        :param digit: precision digit (default value : 5)
        :type digit : int
        :param threshold : activation threshold function
        :type threshold : FunctionType (function or lambda)
        :param file : saved confusion matrix file object
        :type file : (io.IOBase & file)
        :param sample_weight : sample weights list
        :type sample_weight : list
        :param transpose : transpose flag
        :type transpose : bool
        '''
        self.actual_vector = actual_vector
        self.predict_vector = predict_vector
        self.digit = digit
        self.weights = None
        if isinstance(transpose, bool):
            self.transpose = transpose
        else:
            self.transpose = False
        if isfile(file):
            obj_data = json.load(file)
            if obj_data["Actual-Vector"] is not None and obj_data[
                    "Predict-Vector"] is not None:
                try:
                    loaded_weights = obj_data["Sample-Weight"]
                except Exception:
                    loaded_weights = None
                matrix_param = matrix_params_calc(obj_data[
                    "Actual-Vector"],
                    obj_data[
                    "Predict-Vector"], loaded_weights)
                self.actual_vector = obj_data["Actual-Vector"]
                self.predict_vector = obj_data["Predict-Vector"]
                self.weights = loaded_weights
            else:
                try:
                    loaded_transpose = obj_data["Transpose"]
                except Exception:
                    loaded_transpose = False
                self.transpose = loaded_transpose
                loaded_matrix = dict(obj_data["Matrix"])
                for i in loaded_matrix.keys():
                    loaded_matrix[i] = dict(loaded_matrix[i])
                matrix_param = matrix_params_from_table(loaded_matrix)
            self.digit = obj_data["Digit"]
        elif isinstance(matrix, dict):
            if matrix_check(matrix):
                if class_check(list(matrix.keys())) == False:
                    raise pycmMatrixError(
                        "Input Matrix Classes Must Be Same Type")
                else:
                    matrix_param = matrix_params_from_table(matrix, transpose)
            else:
                raise pycmMatrixError("Input Confusion Matrix Format Error")
        else:
            if isinstance(threshold, types.FunctionType):
                predict_vector = list(map(threshold, predict_vector))
                self.predict_vector = predict_vector
            if not isinstance(actual_vector, (list, numpy.ndarray)) or not\
                    isinstance(predict_vector, (list, numpy.ndarray)):
                raise pycmVectorError("Input Vectors Must Be List")
            if len(actual_vector) != len(predict_vector):
                raise pycmVectorError("Input Vectors Must Be The Same Length")
            if len(actual_vector) == 0 or len(predict_vector) == 0:
                raise pycmVectorError("Input Vectors Are Empty")
            [actual_vector, predict_vector] = vector_filter(
                actual_vector, predict_vector)
            matrix_param = matrix_params_calc(
                actual_vector, predict_vector, sample_weight)
            if isinstance(sample_weight, list):
                self.weights = sample_weight
            if isinstance(sample_weight, numpy.ndarray):
                self.weights = sample_weight.tolist()
        if len(matrix_param[0]) < 2:
            raise pycmVectorError("Number Of Classes < 2")
        self.classes = matrix_param[0]
        self.table = matrix_param[1]
        self.matrix = self.table
        self.normalized_table = normalized_table_calc(self.classes, self.table)
        self.normalized_matrix = self.normalized_table
        self.TP = matrix_param[2]
        self.TN = matrix_param[3]
        self.FP = matrix_param[4]
        self.FN = matrix_param[5]
        statistic_result = class_statistics(
            TP=matrix_param[2],
            TN=matrix_param[3],
            FP=matrix_param[4],
            FN=matrix_param[5],
            classes=matrix_param[0],
            table=matrix_param[1])
        self.class_stat = statistic_result
        self.overall_stat = overall_statistics(
            RACC=statistic_result["RACC"],
            RACCU=statistic_result["RACCU"],
            TPR=statistic_result["TPR"],
            PPV=statistic_result["PPV"],
            TP=statistic_result["TP"],
            FN=statistic_result["FN"],
            FP=statistic_result["FP"],
            POP=statistic_result["POP"],
            P=statistic_result["P"],
            TOP=statistic_result["TOP"],
            jaccard_list=statistic_result["J"],
            classes=self.classes,
            table=self.table,
            CEN_dict=statistic_result["CEN"],
            MCEN_dict=statistic_result["MCEN"],
            AUC_dict=statistic_result["AUC"])
        __class_stat_init__(self)
        __overall_stat_init__(self)

    def print_matrix(self, one_vs_all=False, class_name=None):
        '''
        This method print confusion matrix
        :param one_vs_all : One-Vs-All mode flag
        :type one_vs_all : bool
        :param class_name : target class name for One-Vs-All mode
        :type class_name : any valid type
        :return: None
        '''
        classes = self.classes
        table = self.table
        if one_vs_all:
            [classes, table] = one_vs_all_func(
                classes, table, self.TP, self.TN, self.FP, self.FN, class_name)
        print(table_print(classes, table))

    def print_normalized_matrix(self, one_vs_all=False, class_name=None):
        '''
        This method print normalized confusion matrix
        :param one_vs_all : One-Vs-All mode flag
        :type one_vs_all : bool
        :param class_name : target class name for One-Vs-All mode
        :type class_name : any valid type
        :return: None
        '''
        classes = self.classes
        table = self.table
        if one_vs_all:
            [classes, table] = one_vs_all_func(
                classes, table, self.TP, self.TN, self.FP, self.FN, class_name)
        table = normalized_table_calc(classes, table)
        print(table_print(classes, table))

    def stat(self, overall_param=None, class_param=None):
        '''
        This method print statistical measures table
        :param overall_param : Overall parameters list for print, Example : ["Kappa","Scott PI]
        :type overall_param : list
        :param class_param : Class parameters list for print, Example : ["TPR","TNR","AUC"]
        :type class_param : list
        :return: None
        '''
        print(
            stat_print(
                self.classes,
                self.class_stat,
                self.overall_stat,
                self.digit, overall_param, class_param))

    def __str__(self):
        '''
        ConfusionMatrix object string representation method
        :return: representation as str (matrix + params)
        '''
        result = table_print(self.classes, self.table)
        result += "\n" * 4
        result += stat_print(self.classes, self.class_stat,
                             self.overall_stat, self.digit)
        return result

    def save_stat(
            self,
            name,
            address=True,
            overall_param=None,
            class_param=None):
        '''
        This method save ConfusionMatrix in .pycm (flat file format)
        :param name: filename
        :type name : str
        :param address: Flag for address return
        :type address : bool
        :param overall_param : Overall parameters list for save, Example : ["Kappa","Scott PI]
        :type overall_param : list
        :param class_param : Class parameters list for save, Example : ["TPR","TNR","AUC"]
        :type class_param : list
        :return: Saving Status as dict {"Status":bool , "Message":str}
        '''
        try:
            message = None
            file = open(name + ".pycm", "w")
            matrix = "Matrix : \n\n" + table_print(self.classes,
                                                   self.table) + "\n\n"
            normalized_matrix = "Normalized Matrix : \n\n" + \
                                table_print(self.classes,
                                            self.normalized_table) + "\n\n"
            one_vs_all = "\nOne-Vs-All : \n\n"
            for class_name in self.classes:
                one_vs_all += str(class_name) + "-Vs-All : \n\n"
                [classes, table] = one_vs_all_func(self.classes, self.table,
                                                   self.TP, self.TN, self.FP,
                                                   self.FN, class_name)
                one_vs_all += table_print(classes, table) + "\n\n"
            stat = stat_print(
                self.classes,
                self.class_stat,
                self.overall_stat,
                self.digit, overall_param, class_param)
            file.write(matrix + normalized_matrix + stat + one_vs_all)
            file.close()
            if address:
                message = os.path.join(os.getcwd(), name + ".pycm")
            return {"Status": True, "Message": message}
        except Exception as e:
            return {"Status": False, "Message": str(e)}

    def save_html(
            self,
            name,
            address=True,
            overall_param=None,
            class_param=None):
        '''
        This method save ConfusionMatrix in HTML file
        :param name: filename
        :type name : str
        :param address: Flag for address return
        :type address : bool
        :param overall_param : Overall parameters list for save, Example : ["Kappa","Scott PI]
        :type overall_param : list
        :param class_param : Class parameters list for save, Example : ["TPR","TNR","AUC"]
        :type class_param : list
        :return: Saving Status as dict {"Status":bool , "Message":str}
        '''
        try:
            message = None
            html_file = open(name + ".html", "w")
            html_maker(
                html_file,
                name,
                self.classes,
                self.table,
                self.overall_stat,
                self.class_stat,
                self.digit, overall_param, class_param)
            html_file.close()
            if address:
                message = os.path.join(os.getcwd(), name + ".html")
            return {"Status": True, "Message": message}
        except Exception as e:
            return {"Status": False, "Message": str(e)}

    def save_csv(self, name, address=True, class_param=None):
        '''
        This method save ConfusionMatrix in CSV file
        :param name: filename
        :type name : str
        :param address: Flag for address return
        :type address : bool
        :param class_param : Class parameters list for save, Example : ["TPR","TNR","AUC"]
        :type class_param : list
        :return: Saving Status as dict {"Status":bool , "Message":str}
        '''
        try:
            message = None
            csv_file = open(name + ".csv", "w")
            csv_data = csv_print(
                self.classes,
                self.class_stat,
                self.digit,
                class_param)
            csv_file.write(csv_data)
            if address:
                message = os.path.join(os.getcwd(), name + ".csv")
            return {"Status": True, "Message": message}
        except Exception as e:
            return {"Status": False, "Message": str(e)}

    def save_obj(self, name, address=True):
        '''
        This method save ConfusionMatrix in .obj file
        :param name: filename
        :type name : str
        :param address: Flag for address return
        :type address : bool
        :return: Saving Status as dict {"Status":bool , "Message":str}
        '''
        try:
            message = None
            obj_file = open(name + ".obj", "w")
            actual_vector_temp = self.actual_vector
            predict_vector_temp = self.predict_vector
            matrix_temp = {k: self.table[k].copy() for k in self.classes}
            matrix_items = []
            for i in self.classes:
                matrix_items.append((i, list(matrix_temp[i].items())))
            if isinstance(actual_vector_temp, numpy.ndarray):
                actual_vector_temp = actual_vector_temp.tolist()
            if isinstance(predict_vector_temp, numpy.ndarray):
                predict_vector_temp = predict_vector_temp.tolist()
            json.dump({"Actual-Vector": actual_vector_temp,
                       "Predict-Vector": predict_vector_temp,
                       "Matrix": matrix_items,
                       "Digit": self.digit,
                       "Sample-Weight": self.weights,
                       "Transpose": self.transpose}, obj_file)
            if address:
                message = os.path.join(os.getcwd(), name + ".obj")
            return {"Status": True, "Message": message}
        except Exception as e:
            return {"Status": False, "Message": str(e)}

    def F_beta(self, Beta):
        '''
        This method calculate FBeta Score
        :param Beta: Beta parameter
        :type Beta : float
        :return: FBeta Score for classes as dict
        '''
        try:
            F_Dict = {}
            for i in self.TP.keys():
                F_Dict[i] = F_calc(
                    TP=self.TP[i],
                    FP=self.FP[i],
                    FN=self.FN[i],
                    Beta=Beta)
            return F_Dict
        except Exception:
            return {}

    def __repr__(self):
        '''
        ConfusionMatrix object representation method
        :return: representation as str
        '''
        return "pycm.ConfusionMatrix(classes: " + str(self.classes) + ")"

    def __len__(self):
        return len(self.classes)

    def relabel(self, mapping):
        '''
        This method rename ConfusionMatrix classes
        :param mapping: mapping dictionary
        :type mapping : dict
        :return: None
        '''
        if not isinstance(mapping, dict):
            raise pycmMatrixError("Mapping Format Error")
        if self.classes != list(mapping.keys()):
            raise pycmMatrixError("Mapping Classnames Error")
        for row in self.classes:
            temp_dict = {}
            temp_dict_normalized = {}
            for col in self.classes:
                temp_dict[mapping[col]] = self.table[row][col]
                temp_dict_normalized[mapping[col]
                                     ] = self.normalized_table[row][col]
            self.table[mapping[row]] = temp_dict
            self.normalized_table[mapping[row]] = temp_dict_normalized
        self.matrix = self.table
        self.normalized_matrix = self.normalized_table
        for param in self.class_stat.keys():
            temp_dict = {}
            for classname in self.classes:
                temp_dict[mapping[classname]
                          ] = self.class_stat[param][classname]
            self.class_stat[param] = temp_dict
        self.classes = list(mapping.values())
        self.TP = self.class_stat["TP"]
        self.TN = self.class_stat["TN"]
        self.FP = self.class_stat["FP"]
        self.FN = self.class_stat["FN"]
        __class_stat_init__(self)


def __class_stat_init__(CM):
    '''
    This function init individual class stat
    :param CM: ConfusionMatrix
    :type CM : pycm.ConfusionMatrix object
    :return: None
    '''
    CM.TPR = CM.class_stat["TPR"]
    CM.TNR = CM.class_stat["TNR"]
    CM.PPV = CM.class_stat["PPV"]
    CM.NPV = CM.class_stat["NPV"]
    CM.FNR = CM.class_stat["FNR"]
    CM.FPR = CM.class_stat["FPR"]
    CM.FDR = CM.class_stat["FDR"]
    CM.FOR = CM.class_stat["FOR"]
    CM.ACC = CM.class_stat["ACC"]
    CM.F1 = CM.class_stat["F1"]
    CM.MCC = CM.class_stat["MCC"]
    CM.BM = CM.class_stat["BM"]
    CM.MK = CM.class_stat["MK"]
    CM.DOR = CM.class_stat["DOR"]
    CM.PLR = CM.class_stat["PLR"]
    CM.NLR = CM.class_stat["NLR"]
    CM.POP = CM.class_stat["POP"]
    CM.P = CM.class_stat["P"]
    CM.N = CM.class_stat["N"]
    CM.TOP = CM.class_stat["TOP"]
    CM.TON = CM.class_stat["TON"]
    CM.PRE = CM.class_stat["PRE"]
    CM.G = CM.class_stat["G"]
    CM.RACC = CM.class_stat["RACC"]
    CM.RACCU = CM.class_stat["RACCU"]
    CM.F2 = CM.class_stat["F2"]
    CM.F05 = CM.class_stat["F0.5"]
    CM.ERR = CM.class_stat["ERR"]
    CM.J = CM.class_stat["J"]
    CM.IS = CM.class_stat["IS"]
    CM.CEN = CM.class_stat["CEN"]
    CM.MCEN = CM.class_stat["MCEN"]
    CM.AUC = CM.class_stat["AUC"]
    CM.dInd = CM.class_stat["dInd"]
    CM.sInd = CM.class_stat["sInd"]
    CM.DP = CM.class_stat["DP"]
    CM.Y = CM.class_stat["Y"]
    CM.PLRI = CM.class_stat["PLRI"]
    CM.DPI = CM.class_stat["DPI"]
    CM.AUCI = CM.class_stat["AUCI"]


def __overall_stat_init__(CM):
    '''
    This function init individual overall stat
    :param CM: ConfusionMatrix
    :type CM : pycm.ConfusionMatrix object
    :return: None
    '''
    CM.Overall_J = CM.overall_stat["Overall J"]
    CM.SOA1 = CM.overall_stat["SOA1(Landis & Koch)"]
    CM.SOA2 = CM.overall_stat["SOA2(Fleiss)"]
    CM.SOA3 = CM.overall_stat["SOA3(Altman)"]
    CM.SOA4 = CM.overall_stat["SOA4(Cicchetti)"]
    CM.Kappa = CM.overall_stat["Kappa"]
    CM.Overall_ACC = CM.overall_stat["Overall ACC"]
    CM.TPR_Macro = CM.overall_stat["TPR Macro"]
    CM.PPV_Macro = CM.overall_stat["PPV Macro"]
    CM.TPR_Micro = CM.overall_stat["TPR Micro"]
    CM.PPV_Micro = CM.overall_stat["PPV Micro"]
    CM.Overall_RACC = CM.overall_stat["Overall RACC"]
    CM.Overall_RACCU = CM.overall_stat["Overall RACCU"]
    CM.PI = CM.overall_stat["Scott PI"]
    CM.AC1 = CM.overall_stat["Gwet AC1"]
    CM.S = CM.overall_stat["Bennett S"]
    CM.Kappa_SE = CM.overall_stat["Kappa Standard Error"]
    CM.Kappa_CI = CM.overall_stat["Kappa 95% CI"]
    CM.Chi_Squared = CM.overall_stat["Chi-Squared"]
    CM.Phi_Squared = CM.overall_stat["Phi-Squared"]
    CM.KappaUnbiased = CM.overall_stat["Kappa Unbiased"]
    CM.KappaNoPrevalence = CM.overall_stat["Kappa No Prevalence"]
    CM.V = CM.overall_stat["Cramer V"]
    CM.DF = CM.overall_stat["Chi-Squared DF"]
    CM.CI = CM.overall_stat["95% CI"]
    CM.SE = CM.overall_stat["Standard Error"]
    CM.ReferenceEntropy = CM.overall_stat["Reference Entropy"]
    CM.ResponseEntropy = CM.overall_stat["Response Entropy"]
    CM.CrossEntropy = CM.overall_stat["Cross Entropy"]
    CM.JointEntropy = CM.overall_stat["Joint Entropy"]
    CM.ConditionalEntropy = CM.overall_stat["Conditional Entropy"]
    CM.MutualInformation = CM.overall_stat["Mutual Information"]
    CM.KL = CM.overall_stat["KL Divergence"]
    CM.LambdaB = CM.overall_stat["Lambda B"]
    CM.LambdaA = CM.overall_stat["Lambda A"]
    CM.HammingLoss = CM.overall_stat["Hamming Loss"]
    CM.ZeroOneLoss = CM.overall_stat["Zero-one Loss"]
    CM.NIR = CM.overall_stat["NIR"]
    CM.PValue = CM.overall_stat["P-Value"]
    CM.Overall_CEN = CM.overall_stat["Overall CEN"]
    CM.Overall_MCEN = CM.overall_stat["Overall MCEN"]
    CM.Overall_MCC = CM.overall_stat["Overall MCC"]
    CM.RR = CM.overall_stat["RR"]
    CM.CBA = CM.overall_stat["CBA"]
    CM.AUNU = CM.overall_stat["AUNU"]
    CM.AUNP = CM.overall_stat["AUNP"]
    CM.RCI = CM.overall_stat["RCI"]
