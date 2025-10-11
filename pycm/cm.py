# -*- coding: utf-8 -*-
"""ConfusionMatrix module."""
from __future__ import division
from typing import Union, List, Dict, Any, Tuple, Callable, Generator, Optional
from .errors import pycmVectorError, pycmMatrixError, pycmCIError, pycmAverageError, pycmPlotError
from .handlers import __class_stat_init__, __overall_stat_init__
from .handlers import __obj_assign_handler__, __obj_file_handler__, __obj_matrix_handler__, __obj_vector_handler__, __obj_array_handler__
from .handlers import __imbalancement_handler__
from .class_funcs import F_calc, IBA_calc, TI_calc, NB_calc, sensitivity_index_calc
from .overall_funcs import weighted_kappa_calc, weighted_alpha_calc, alpha2_calc, brier_score_calc, log_loss_calc
from .distance import DistanceType, DISTANCE_MAPPER
from .output import *
from .utils import *
from .params import *
from .ci import __CI_overall_handler__, __CI_class_handler__
import os
import json
import numpy
import time
from warnings import warn


class ConfusionMatrix():
    """
    Confusion matrix class.

    >>> y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
    >>> y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
    >>> cm = ConfusionMatrix(y_actu, y_pred)
    >>> cm.classes
    [0, 1, 2]
    >>> cm.table
    {0: {0: 3, 1: 0, 2: 0}, 1: {0: 0, 1: 1, 2: 2}, 2: {0: 2, 1: 1, 2: 3}}
    >>> cm2 = ConfusionMatrix(matrix={"Class1": {"Class1": 1, "Class2": 2}, "Class2": {"Class1": 0, "Class2": 5}})
    >>> cm2
    pycm.ConfusionMatrix(classes: ['Class1', 'Class2'])
    """

    def __init__(
            self,
            actual_vector: Optional[Union[List[Any], numpy.ndarray]] = None,
            predict_vector: Optional[Union[List[Any], numpy.ndarray]] = None,
            matrix: Optional[Union[Dict[str, Dict[str, int]], List[List[int]], numpy.ndarray]] = None,
            digit: int = 5,
            threshold: Optional[Callable] = None,
            file: Optional[TextIOWrapper] = None,
            sample_weight: Optional[Union[List[float], numpy.ndarray]] = None,
            transpose: bool = False,
            classes: Optional[List[Any]] = None,
            is_imbalanced: Optional[bool] = None,
            metrics_off: bool = False) -> None:
        """
        Init method.

        :param actual_vector: actual vector
        :param predict_vector: vector of predictions
        :param matrix: the confusion matrix
        :param digit: scale (number of fraction digits)(default value: 5)
        :param threshold: activation threshold function
        :param file: saved confusion matrix file object
        :param sample_weight: sample weights list
        :param transpose: transpose flag
        :param classes: ordered labels of classes
        :param is_imbalanced: imbalance dataset flag
        :param metrics_off: metrics off flag
        """
        self.timings = {
            "matrix_creation": 0.0,
            "class_statistics": 0.0,
            "overall_statistics": 0.0,
            "total": 0.0
        }
        matrix_creation_start = time.perf_counter()
        self.actual_vector = actual_vector
        self.predict_vector = predict_vector
        self.metrics_off = metrics_off
        self.prob_vector = None
        self.digit = digit
        self.weights = None
        self.classes = None
        self.imbalance = None
        if isinstance(transpose, bool):
            self.transpose = transpose
        else:
            self.transpose = False
        if isfile(file):
            matrix_param = __obj_file_handler__(self, file)
        elif isinstance(matrix, dict):
            matrix_param = __obj_matrix_handler__(
                matrix, classes, self.transpose)
        elif isinstance(matrix, (list, numpy.ndarray)):
            matrix_param = __obj_array_handler__(
                matrix, classes, self.transpose)
        else:
            matrix_param = __obj_vector_handler__(
                self, actual_vector, predict_vector, threshold, sample_weight, classes)
        __obj_assign_handler__(self, matrix_param)
        matrix_creation_end = time.perf_counter()
        self.timings["matrix_creation"] = matrix_creation_end - matrix_creation_start
        if not metrics_off:
            class_statistics_start = time.perf_counter()
            __class_stat_init__(self)
            class_statistics_end = time.perf_counter()
            self.timings["class_statistics"] = class_statistics_end - class_statistics_start
            overall_statistics_start = time.perf_counter()
            __overall_stat_init__(self)
            overall_statistics_end = time.perf_counter()
            self.timings["overall_statistics"] = overall_statistics_end - overall_statistics_start
            __imbalancement_handler__(self, is_imbalanced)
        self.binary = binary_check(self.classes)
        self.recommended_list = statistic_recommend(
            self.classes, self.imbalance)
        self.sparse_matrix = None
        self.sparse_normalized_matrix = None
        self.positions = None
        self.label_map = {x: x for x in self.classes}
        self.timings["total"] = sum(self.timings.values())

    def print_matrix(self,
                     one_vs_all: bool = False,
                     class_name: Any = None,
                     sparse: bool = False) -> None:
        """
        Print confusion matrix.

        :param one_vs_all: one-vs-all mode flag
        :param class_name: target class name for one-vs-all mode
        :param sparse: sparse mode printing flag
        """
        classes = self.classes
        table = self.table
        if one_vs_all:
            [classes, table] = one_vs_all_func(
                classes, table, self.TP, self.TN, self.FP, self.FN, class_name)
        if sparse is True:
            if self.sparse_matrix is None:
                self.sparse_matrix = sparse_matrix_calc(classes, table)
            print(sparse_table_print(self.sparse_matrix))
        else:
            print(table_print(classes, table))
        if len(classes) >= CLASS_NUMBER_THRESHOLD:
            warn(CLASS_NUMBER_WARNING, RuntimeWarning)

    def print_normalized_matrix(
            self,
            one_vs_all: bool = False,
            class_name: Any = None,
            sparse: bool = False) -> None:
        """
        Print normalized confusion matrix.

        :param one_vs_all: one-vs-all mode flag
        :param class_name: target class name for one-vs-all mode
        :param sparse: sparse mode printing flag
        """
        classes = self.classes
        table = self.table
        normalized_table = self.normalized_table
        if one_vs_all:
            [classes, table] = one_vs_all_func(
                classes, table, self.TP, self.TN, self.FP, self.FN, class_name)
            normalized_table = normalized_table_calc(classes, table)
        if sparse is True:
            if self.sparse_normalized_matrix is None:
                self.sparse_normalized_matrix = sparse_matrix_calc(
                    classes, normalized_table)
            print(sparse_table_print(self.sparse_normalized_matrix))
        else:
            print(table_print(classes, normalized_table))
        if len(classes) >= CLASS_NUMBER_THRESHOLD:
            warn(CLASS_NUMBER_WARNING, RuntimeWarning)

    def print_timings(self) -> None:
        """Print timings report."""
        result = TIMINGS_TEMPLATE.format(matrix_creation=self.timings["matrix_creation"],
                                         class_statistics=self.timings["class_statistics"],
                                         overall_statistics=self.timings["overall_statistics"],
                                         total=self.timings["total"])
        print(result)

    @metrics_off_check
    def stat(
            self,
            overall_param: Optional[List[str]] = None,
            class_param: Optional[List[str]] = None,
            class_name: Optional[List[Any]] = None,
            summary: bool = False) -> None:
        """
        Print statistical measures table.

        :param overall_param: overall parameters list for print, Example: ["Kappa", "Scott PI"]
        :param class_param: class parameters list for print, Example: ["TPR", "TNR", "AUC"]
        :param class_name: class name (a subset of confusion matrix classes), Example: [1, 2, 3]
        :param summary: summary mode flag
        """
        classes = class_filter(self.classes, class_name)
        class_list = class_param
        overall_list = overall_param
        if summary:
            class_list = SUMMARY_CLASS
            overall_list = SUMMARY_OVERALL
        print(
            stat_print(
                classes,
                self.class_stat,
                self.overall_stat,
                self.digit, overall_list, class_list))
        if len(classes) >= CLASS_NUMBER_THRESHOLD:
            warn(CLASS_NUMBER_WARNING, RuntimeWarning)

    def __str__(self) -> str:
        """Confusion matrix object string representation method."""
        result = table_print(self.classes, self.table)
        result += "\n" * 4
        result += stat_print(self.classes, self.class_stat,
                             self.overall_stat, self.digit)
        if len(self.classes) >= CLASS_NUMBER_THRESHOLD:
            warn(CLASS_NUMBER_WARNING, RuntimeWarning)
        return result

    def __iter__(self) -> Generator[Tuple[Any, Dict[Any, int]], None, None]:
        """Iterate through confusion matrix."""
        for key in self.matrix:
            yield key, self.matrix[key]

    def __contains__(self, class_name: Any) -> bool:
        """
        Check if the confusion matrix contains the given class name.

        :param class_name: given class name
        """
        return class_name in self.classes

    def __getitem__(self, class_name: Any) -> Dict[Any, int]:
        """
        Return the element(s) in the matrix corresponding to the given class name.

        :param class_name: given class name
        """
        return self.matrix[class_name]

    def save_stat(
            self,
            name: str,
            address: bool = True,
            overall_param: Optional[List[str]] = None,
            class_param: Optional[List[str]] = None,
            class_name: Optional[List[Any]] = None,
            summary: bool = False,
            sparse: bool = False) -> Dict[str, Union[bool, str]]:
        """
        Save the ConfusionMatrix object in .pycm (flat file format) and return the result as a dictionary.

        :param name: filename
        :param address: flag for address return
        :param overall_param: overall parameters list for save, Example: ["Kappa", "Scott PI"]
        :param class_param: class parameters list for save, Example: ["TPR", "TNR", "AUC"]
        :param class_name: class name (subset of classes names), Example: [1, 2, 3]
        :param summary: summary mode flag
        :param sparse: sparse mode printing flag
        """
        try:
            message = None
            class_list = class_param
            overall_list = overall_param
            warning_message = ""
            if summary:
                class_list = SUMMARY_CLASS
                overall_list = SUMMARY_OVERALL
            classes = self.classes
            table = self.table
            file = open(name + ".pycm", "w", encoding="utf-8")
            if sparse is True:
                if self.sparse_matrix is None:
                    self.sparse_matrix = sparse_matrix_calc(classes, table)
                matrix = "Matrix : \n\n" + \
                    sparse_table_print(self.sparse_matrix) + "\n\n"
                if self.sparse_normalized_matrix is None:
                    self.sparse_normalized_matrix = sparse_matrix_calc(
                        classes, self.normalized_table)
                normalized_matrix = "Normalized Matrix : \n\n" + \
                    sparse_table_print(self.sparse_normalized_matrix) + "\n\n"
            else:
                matrix = "Matrix : \n\n" + table_print(self.classes,
                                                       self.table) + "\n\n"
                normalized_matrix = "Normalized Matrix : \n\n" + \
                                    table_print(self.classes,
                                                self.normalized_table) + "\n\n"
            one_vs_all = "\nOne-Vs-All : \n\n"
            for c in self.classes:
                one_vs_all += str(c) + "-Vs-All : \n\n"
                [classes, table] = one_vs_all_func(self.classes, self.table,
                                                   self.TP, self.TN, self.FP,
                                                   self.FN, c)
                one_vs_all += table_print(classes, table) + "\n\n"
            classes = class_filter(self.classes, class_name)
            stat = stat_print(
                classes,
                self.class_stat,
                self.overall_stat,
                self.digit, overall_list, class_list)
            if len(self.classes) >= CLASS_NUMBER_THRESHOLD:
                warning_message = "\n" + "Warning : " + CLASS_NUMBER_WARNING + "\n"
            file.write(
                matrix +
                normalized_matrix +
                stat +
                one_vs_all +
                warning_message)
            file.close()
            if address:
                message = os.path.join(
                    os.getcwd(), name + ".pycm")  # pragma: no cover
            return {"Status": True, "Message": message}
        except Exception as e:
            return {"Status": False, "Message": str(e)}

    def save_html(
            self,
            name: str,
            address: bool = True,
            overall_param: Optional[List[str]] = None,
            class_param: Optional[List[str]] = None,
            class_name: Optional[List[Any]] = None,
            color: Tuple[int, int, int] = (0, 0, 0),
            normalize: bool = False,
            summary: bool = False,
            alt_link: bool = False,
            shortener: bool = True) -> Dict[str, Union[bool, str]]:
        """
        Save ConfusionMatrix in HTML file and return the result as a dictionary.

        :param name: filename
        :param address: flag for address return
        :param overall_param: overall parameters list for save, Example: ["Kappa", "Scott PI"]
        :param class_param: class parameters list for save, Example: ["TPR", "TNR", "AUC"]
        :param class_name: class name (subset of classes names), Example: [1, 2, 3]
        :param color: matrix color in RGB as (R, G, B)
        :param normalize: save normalize matrix flag
        :param summary: summary mode flag
        :param alt_link: alternative link for document flag
        :param shortener: class name shortener flag
        """
        try:
            class_list = class_param
            overall_list = overall_param
            if summary:
                class_list = SUMMARY_CLASS
                overall_list = SUMMARY_OVERALL
            message = None
            table = self.table
            if normalize:
                table = self.normalized_table
            html_file = open(name + ".html", "w", encoding="utf-8")
            html_file.write(HTML_INIT_TEMPLATE.format(description=OG_DESCRIPTION, image_url=OG_IMAGE_URL))
            html_file.write(html_dataset_type(self.binary, self.imbalance))
            html_file.write(
                html_table(
                    self.classes,
                    table,
                    color,
                    normalize,
                    shortener))
            html_file.write(
                html_overall_stat(
                    self.overall_stat,
                    self.digit,
                    overall_list,
                    self.recommended_list,
                    alt_link))
            class_stat_classes = class_filter(self.classes, class_name)
            html_file.write(
                html_class_stat(
                    class_stat_classes,
                    self.class_stat,
                    self.digit,
                    class_list,
                    self.recommended_list,
                    alt_link))
            html_file.write(HTML_END_TEMPLATE.format(version=PYCM_VERSION))
            html_file.close()
            if address:
                message = os.path.join(
                    os.getcwd(), name + ".html")  # pragma: no cover
            return {"Status": True, "Message": message}
        except Exception as e:
            return {"Status": False, "Message": str(e)}

    def save_csv(
            self,
            name: str,
            address: bool = True,
            class_param: Optional[List[str]] = None,
            class_name: Optional[List[Any]] = None,
            matrix_save: bool = True,
            normalize: bool = False,
            summary: bool = False,
            header: bool = False) -> Dict[str, Union[bool, str]]:
        """
        Save ConfusionMatrix in csv file and return the result as a dictionary.

        :param name: filename
        :param address: flag for address return
        :param class_param: class parameters list for save, Example: ["TPR", "TNR", "AUC"]
        :param class_name: class name (subset of classes names), Example: [1, 2, 3]
        :param matrix_save: save matrix flag
        :param normalize: save normalize matrix flag
        :param summary: summary mode flag
        :param header: add headers to csv file
        """
        try:
            class_list = class_param
            if summary:
                class_list = SUMMARY_CLASS
            message = None
            classes = class_filter(self.classes, class_name)
            csv_file = open(name + ".csv", "w", encoding="utf-8")
            csv_data = csv_print(
                classes,
                self.class_stat,
                self.digit,
                class_list)
            csv_file.write(csv_data)
            if matrix_save:
                matrix = self.table
                if normalize:
                    matrix = self.normalized_table
                csv_matrix_file = open(
                    name + "_matrix" + ".csv", "w", encoding="utf-8")
                csv_matrix_data = csv_matrix_print(
                    self.classes, matrix, header=header)
                csv_matrix_file.write(csv_matrix_data)
            if address:
                message = os.path.join(
                    os.getcwd(), name + ".csv")  # pragma: no cover
            return {"Status": True, "Message": message}
        except Exception as e:
            return {"Status": False, "Message": str(e)}

    def save_obj(
            self,
            name: str,
            address: bool = True,
            save_stat: bool = False,
            save_vector: bool = True) -> Dict[str, Union[bool, str]]:
        """
        Save ConfusionMatrix object in .obj file and return the result as a dictionary.

        :param name: filename
        :param address: flag for address return
        :param save_stat: save statistics flag
        :param save_vector: save vectors flag
        """
        try:
            message = None
            obj_file = open(name + ".obj", "w")
            actual_vector_temp = self.actual_vector
            predict_vector_temp = self.predict_vector
            prob_vector_temp = self.prob_vector
            weights_vector_temp = self.weights
            matrix_temp = {k: self.table[k].copy() for k in self.classes}
            matrix_items = []
            for i in self.classes:
                matrix_items.append((i, list(matrix_temp[i].items())))
            actual_vector_temp, predict_vector_temp, prob_vector_temp, weights_vector_temp = map(
                vector_serializer, [
                    actual_vector_temp, predict_vector_temp, prob_vector_temp, weights_vector_temp])
            dump_dict = {"Actual-Vector": actual_vector_temp,
                         "Predict-Vector": predict_vector_temp,
                         "Prob-Vector": prob_vector_temp,
                         "Matrix": matrix_items,
                         "Digit": self.digit,
                         "Sample-Weight": weights_vector_temp,
                         "Transpose": self.transpose,
                         "Imbalanced": self.imbalance}
            if save_stat:
                dump_dict["Class-Stat"] = self.class_stat
                dump_dict["Overall-Stat"] = self.overall_stat
            if not save_vector:
                dump_dict["Actual-Vector"] = None
                dump_dict["Predict-Vector"] = None
                dump_dict["Prob-Vector"] = None
                dump_dict["Sample-Weight"] = None
            json.dump(dump_dict, obj_file)
            if address:
                message = os.path.join(
                    os.getcwd(), name + ".obj")  # pragma: no cover
            return {"Status": True, "Message": message}
        except Exception as e:
            return {"Status": False, "Message": str(e)}

    def F_beta(self, beta: float) -> Dict[str, float]:
        """
        Calculate FBeta score for all classes.

        :param beta: beta parameter
        """
        try:
            F_dict = {}
            for i in self.TP:
                F_dict[i] = F_calc(
                    TP=self.TP[i],
                    FP=self.FP[i],
                    FN=self.FN[i],
                    beta=beta)
            return F_dict
        except Exception:
            return {}

    @metrics_off_check
    def sensitivity_index(self) -> Dict[str, float]:
        """Calculate sensitivity index for all classes."""
        sensitivity_index_dict = {}
        for i in self.classes:
            sensitivity_index_dict[i] = sensitivity_index_calc(
                self.TPR[i], self.FPR[i])
        return sensitivity_index_dict

    @metrics_off_check
    def IBA_alpha(self, alpha: float) -> Dict[str, float]:
        """
        Calculate IBA_alpha score for all classes.

        :param alpha: alpha parameter
        """
        try:
            IBA_dict = {}
            for i in self.classes:
                IBA_dict[i] = IBA_calc(self.TPR[i], self.TNR[i], alpha=alpha)
            return IBA_dict
        except Exception:
            return {}

    def TI(self, alpha: float, beta: float) -> Dict[str, float]:
        """
        Calculate Tversky index.

        :param alpha: alpha coefficient
        :param beta: beta coefficient
        """
        try:
            TI_dict = {}
            for i in self.classes:
                TI_dict[i] = TI_calc(
                    self.TP[i], self.FP[i], self.FN[i], alpha, beta)
            return TI_dict
        except Exception:
            return {}

    @metrics_off_check
    def NB(self, w: float = 1.0) -> Dict[str, float]:
        """
        Calculate Net benefit for all classes.

        :param w: weight
        """
        try:
            NB_dict = {}
            for i in self.classes:
                NB_dict[i] = NB_calc(self.TP[i], self.FP[i], self.POP[i], w)
            return NB_dict
        except Exception:
            return {}

    def distance(self, metric: DistanceType) -> Dict[str, float]:
        """
        Calculate distance/similarity for all classes.

        :param metric: metric
        """
        distance_dict = {}
        if not isinstance(metric, DistanceType):
            raise pycmMatrixError(DISTANCE_METRIC_TYPE_ERROR)
        for i in self.classes:
            distance_dict[i] = DISTANCE_MAPPER[metric](
                TP=self.TP[i], FP=self.FP[i], FN=self.FN[i], TN=self.TN[i])
        return distance_dict

    def dissimilarity_matrix(self) -> Dict[str, Dict[str, int]]:
        """Calculate dissimilarity matrix."""
        result = {class_name: dict(zip(self.classes, [0] * len(self.classes))) for class_name in self.classes}
        matrix_array = self.to_array()
        for class_index_1, class_name_1 in enumerate(self.classes):
            for class_index_2, class_name_2 in enumerate(self.classes):
                dist = int(sum(abs(matrix_array[class_index_1] - matrix_array[class_index_2])))
                result[class_name_1][class_name_2] = dist
        return result

    @metrics_off_check
    def CI(
            self,
            param: str,
            alpha: float = 0.05,
            one_sided: bool = False,
            binom_method: str = "normal-approx") -> Dict[str, Tuple[float, float]]:
        """
        Calculate CI.

        :param param: input parameter
        :param alpha: type I error
        :param one_sided: one-sided mode flag
        :param binom_method: binomial confidence intervals method
        """
        if isinstance(param, str):
            method = "normal-approx"
            if isinstance(binom_method, str):
                method = binom_method.lower()
            if one_sided:
                if alpha in ALPHA_ONE_SIDE_TABLE:
                    CV = ALPHA_ONE_SIDE_TABLE[alpha]
                else:
                    CV = ALPHA_ONE_SIDE_TABLE[0.05]
                    warn(CI_ALPHA_ONE_SIDE_WARNING, RuntimeWarning)
            else:
                if alpha in ALPHA_TWO_SIDE_TABLE:
                    CV = ALPHA_TWO_SIDE_TABLE[alpha]
                else:
                    CV = ALPHA_TWO_SIDE_TABLE[0.05]
                    warn(CI_ALPHA_TWO_SIDE_WARNING, RuntimeWarning)
            param_u = param.upper()
            if param_u in CI_CLASS_LIST:
                return __CI_class_handler__(self, param_u, CV, method)
            if param in CI_OVERALL_LIST:
                return __CI_overall_handler__(self, param, CV, method)
            raise pycmCIError(CI_SUPPORT_ERROR)
        raise pycmCIError(CI_FORMAT_ERROR)

    def __repr__(self) -> str:
        """Confusion matrix object representation method."""
        return "pycm.ConfusionMatrix(classes: " + str(self.classes) + ")"

    def __len__(self) -> int:
        """Confusion matrix object length method."""
        return len(self.classes)

    def __eq__(self, other: Any) -> bool:
        """
        Confusion matrix equal method.

        :param other: the other confusion matrix
        """
        if isinstance(other, ConfusionMatrix):
            return self.table == other.table
        return False

    def __ne__(self, other: Any) -> bool:
        """
        Confusion matrix not equal method.

        :param other: the other confusion matrix
        """
        return not self.__eq__(other)

    def __copy__(self) -> "ConfusionMatrix":
        """Create a copy of the confusion matrix."""
        _class = self.__class__
        result = _class.__new__(_class)
        result.__dict__.update(self.__dict__)
        return result

    def copy(self) -> "ConfusionMatrix":
        """Create a copy of the confusion matrix."""
        return self.__copy__()

    def relabel(self, mapping: Dict[Any, Any], sort: bool = False) -> None:
        """
        Rename the confusion matrix classes.

        :param mapping: mapping dictionary
        :param sort: flag for sorting new classes
        """
        if not isinstance(mapping, dict):
            raise pycmMatrixError(MAPPING_FORMAT_ERROR)
        if set(self.classes) != set(mapping):
            raise pycmMatrixError(MAPPING_CLASS_NAME_ERROR)
        if len(self.classes) != len(set(mapping.values())):
            raise pycmMatrixError(MAPPING_CLASS_NAME_ERROR)
        table_temp = {}
        normalized_table_temp = {}
        for row in self.classes:
            temp_dict = {}
            temp_dict_normalized = {}
            for col in self.classes:
                temp_dict[mapping[col]] = self.table[row][col]
                temp_dict_normalized[mapping[col]
                                     ] = self.normalized_table[row][col]
            table_temp[mapping[row]] = temp_dict
            normalized_table_temp[mapping[row]] = temp_dict_normalized
        self.table = table_temp
        self.normalized_table = normalized_table_temp
        self.matrix = self.table
        self.normalized_matrix = self.normalized_table
        for param in self.class_stat:
            temp_dict = {}
            for classname in self.classes:
                temp_dict[mapping[classname]
                          ] = self.class_stat[param][classname]
            self.class_stat[param] = temp_dict
        temp_label_map = {}
        for prime_label, new_label in self.label_map.items():
            temp_label_map[prime_label] = mapping[new_label]
        self.label_map = temp_label_map
        self.positions = None
        self.classes = [mapping[x] for x in self.classes]
        if sort:
            self.classes = sorted(self.classes)
        self.TP = self.class_stat["TP"]
        self.TN = self.class_stat["TN"]
        self.FP = self.class_stat["FP"]
        self.FN = self.class_stat["FN"]
        __class_stat_init__(self)

    @metrics_off_check
    def average(self, param: str, none_omit: bool = False) -> Union[float, str]:
        """
        Calculate the average of the input parameter.

        :param param: input parameter
        :param none_omit: none items omitting flag
        """
        return self.weighted_average(
            param=param,
            weight=self.POP,
            none_omit=none_omit)

    @metrics_off_check
    def weighted_average(self, param: str, weight: Optional[Dict[Any, float]]
                         = None, none_omit: bool = False) -> Union[float, str]:
        """
        Calculate the weighted average of the input parameter.

        :param param: input parameter
        :param weight: explicitly passes weights
        :param none_omit: none items omitting flag
        """
        selected_weight = self.P.copy()
        if weight is not None:
            if not isinstance(weight, dict):
                raise pycmAverageError(AVERAGE_WEIGHT_ERROR)
            if set(weight) == set(self.classes) and all(
                    [isfloat(x) for x in weight.values()]):
                selected_weight = weight.copy()
            else:
                raise pycmAverageError(AVERAGE_WEIGHT_ERROR)
        if param in self.class_stat:
            selected_param = self.class_stat[param]
        else:
            raise pycmAverageError(AVERAGE_INVALID_ERROR)
        try:
            weight_list = []
            param_list = []
            for class_name in selected_param:
                if selected_param[class_name] == "None" and none_omit:
                    continue
                weight_list.append(selected_weight[class_name])
                param_list.append(selected_param[class_name])
            return numpy.average(param_list, weights=weight_list)
        except Exception:
            return "None"

    @metrics_off_check
    def weighted_kappa(self, weight: Optional[Dict[Any, Dict[Any, float]]] = None) -> float:
        """
        Calculate weighted kappa.

        :param weight: weight matrix
        """
        if matrix_check(weight) is False:
            warn(WEIGHTED_KAPPA_WARNING, RuntimeWarning)
            return self.Kappa
        if set(weight) != set(self.classes):
            warn(WEIGHTED_KAPPA_WARNING, RuntimeWarning)
            return self.Kappa
        return weighted_kappa_calc(
            self.classes,
            self.table,
            self.P,
            self.TOP,
            self.POP,
            weight)

    @metrics_off_check
    def weighted_alpha(self, weight: Optional[Dict[Any, Dict[Any, float]]] = None) -> float:
        """
        Calculate weighted Krippendorff's alpha.

        :param weight: weight matrix
        """
        if matrix_check(weight) is False:
            warn(WEIGHTED_ALPHA_WARNING, RuntimeWarning)
            return self.Alpha
        if set(weight) != set(self.classes):
            warn(WEIGHTED_ALPHA_WARNING, RuntimeWarning)
            return self.Alpha
        return weighted_alpha_calc(
            self.classes,
            self.table,
            self.P,
            self.TOP,
            self.POP,
            weight)

    @metrics_off_check
    def aickin_alpha(self, max_iter: int = 200, epsilon: float = 0.0001) -> float:
        """
        Calculate Aickin's alpha.

        :param max_iter: maximum number of iterations
        :param epsilon: difference threshold
        """
        return alpha2_calc(
            self.TOP,
            self.P,
            self.Overall_ACC,
            self.POP,
            self.classes,
            max_iter,
            epsilon)

    def brier_score(self, pos_class: Optional[Any] = None) -> float:
        """
        Calculate Brier score.

        :param pos_class: positive class name
        """
        if self.prob_vector is None or not self.binary:
            raise pycmVectorError(BRIER_LOG_LOSS_PROB_ERROR)
        if pos_class is None and isinstance(self.classes[0], str):
            raise pycmVectorError(BRIER_LOG_LOSS_CLASS_ERROR)
        return brier_score_calc(
            self.classes,
            self.prob_vector,
            self.actual_vector,
            self.weights,
            pos_class)

    def log_loss(self, normalize: bool = True, pos_class: Optional[Any] = None) -> float:
        """
        Calculate Log loss.

        :param normalize: normalization flag
        :param pos_class: positive class name
        """
        if self.prob_vector is None or not self.binary:
            raise pycmVectorError(BRIER_LOG_LOSS_PROB_ERROR)
        if pos_class is None and isinstance(self.classes[0], str):
            raise pycmVectorError(BRIER_LOG_LOSS_CLASS_ERROR)
        return log_loss_calc(
            self.classes,
            self.prob_vector,
            self.actual_vector,
            normalize,
            self.weights,
            pos_class)

    def position(self) -> Dict[Any, Dict[str, List[int]]]:
        """Return indices of TP, FP, TN and FN in the predict_vector."""
        if self.predict_vector is None or self.actual_vector is None:
            raise pycmVectorError(VECTOR_ONLY_ERROR)
        if self.positions is None:
            classes = list(self.label_map)
            positions = {
                self.label_map[_class]: {
                    'TP': [],
                    'FP': [],
                    'TN': [],
                    'FN': []} for _class in classes}
            [actual_vector, predict_vector] = vector_filter(
                self.actual_vector, self.predict_vector)
            for index, observation in enumerate(predict_vector):
                for _class in classes:
                    label = self.label_map[_class]
                    if observation == actual_vector[index]:
                        if _class == observation:
                            positions[label]['TP'].append(index)
                        else:
                            positions[label]['TN'].append(index)
                    else:
                        if _class == observation:
                            positions[label]['FP'].append(index)
                        elif _class == actual_vector[index]:
                            positions[label]['FN'].append(index)
                        else:
                            positions[label]['TN'].append(index)
            self.positions = positions
        return self.positions

    def to_array(self, normalized: bool = False, one_vs_all: bool = False,
                 class_name: Optional[Any] = None) -> numpy.ndarray:
        """
        Return the confusion matrix in form of a numpy array.

        :param normalized: a flag for getting normalized confusion matrix
        :param one_vs_all: one-vs-all mode flag
        :param class_name: target class name for one-vs-all mode
        """
        classes = self.classes
        table = self.table
        if normalized:
            table = self.normalized_table
        if one_vs_all:
            [classes, table] = one_vs_all_func(
                classes, table, self.TP, self.TN, self.FP, self.FN, class_name)
            if normalized:
                table = normalized_table_calc(classes, table)
        array = []
        for key in classes:
            row = [table[key][i] for i in classes]
            array.append(row)
        return numpy.array(array)

    def combine(self, other: "ConfusionMatrix", metrics_off: bool = False) -> "ConfusionMatrix":
        """
        Return the combination of two confusion matrices.

        :param other: the other matrix that is going to be combined
        :param metrics_off: metrics off flag
        """
        if isinstance(other, ConfusionMatrix) is False:
            raise pycmMatrixError(COMBINE_TYPE_ERROR)
        return ConfusionMatrix(
            matrix=matrix_combine(
                self.matrix, other.matrix), metrics_off=metrics_off)

    def plot(
            self,
            normalized: bool = False,
            one_vs_all: bool = False,
            class_name: Optional[Any] = None,
            title: str = 'Confusion Matrix',
            number_label: bool = False,
            cmap: Optional["matplotlib.colors.Color.ListedColormap"] = None,
            plot_lib: str = 'matplotlib') -> "matplotlib.pyplot.Axes":
        """
        Plot confusion matrix and return the plot axes.

        :param normalized: normalized flag for matrix
        :param one_vs_all: one-vs-all mode flag
        :param class_name: target class name for one-vs-all mode
        :param title: plot title
        :param number_label: number label flag
        :param cmap: color map
        :param plot_lib: plotting library
        """
        matrix = self.to_array(
            normalized=normalized,
            one_vs_all=one_vs_all,
            class_name=class_name)
        classes = self.classes
        if normalized:
            title += " (Normalized)"
        if one_vs_all and class_name in classes:
            classes = [class_name, '~']
        try:
            from matplotlib import pyplot as plt
        except (ModuleNotFoundError, ImportError):
            raise pycmPlotError(MATPLOTLIB_PLOT_LIBRARY_ERROR)
        if cmap is None:
            cmap = plt.cm.gray_r
        fig, ax = plt.subplots()
        fig.canvas.manager.set_window_title(title)
        if plot_lib == 'seaborn':
            try:
                import seaborn as sns
            except (ModuleNotFoundError, ImportError):
                raise pycmPlotError(SEABORN_PLOT_LIBRARY_ERROR)
            ax = sns.heatmap(matrix, cmap=cmap)
            return axes_gen(
                ax,
                classes,
                matrix,
                title,
                cmap,
                number_label,
                plot_lib)
        plt.imshow(matrix, cmap=cmap)
        plt.colorbar()
        return axes_gen(
            ax,
            classes,
            matrix,
            title,
            cmap,
            number_label,
            plot_lib)
