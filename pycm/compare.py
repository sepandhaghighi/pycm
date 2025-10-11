# -*- coding: utf-8 -*-
"""Compare module."""
from __future__ import division
from typing import Dict, Optional, Union
from .errors import pycmCompareError
from .output import *
from .utils import *
from .params import *
from .cm import ConfusionMatrix
import os
import numpy
from warnings import warn


class Compare():
    """
    Compare class.

    >>> cm1 = ConfusionMatrix(matrix={0:{0:2,1:50,2:6}, 1:{0:5,1:50,2:3}, 2:{0:1,1:7,2:50}})
    >>> cm2 = ConfusionMatrix(matrix={0:{0:50,1:2,2:6}, 1:{0:50,1:5,2:3}, 2:{0:1,1:55,2:2}})
    >>> cp = Compare({"cm1": cm1, "cm2": cm2})
    >>> print(cp)
    Best : cm1
    <BLANKLINE>
    Rank  Name   Class-Score       Overall-Score
    1     cm1    0.50278           0.58095
    2     cm2    0.33611           0.52857
    <BLANKLINE>
    >>> cp.best
    pycm.ConfusionMatrix(classes: [0, 1, 2])
    >>> cp.sorted
    ['cm1', 'cm2']
    >>> cp.best_name
    'cm1'
    """

    def __init__(
            self,
            cm_dict: Dict[str, "ConfusionMatrix"],
            by_class: bool=False,
            class_weight: Optional[dict]=None,
            class_benchmark_weight: Optional[dict]=None,
            overall_benchmark_weight: Optional[dict]=None,
            digit: int=5) -> None:
        """
        Init method.

        :param cm_dict: dictionary of confusion matrices
        :param by_class: compare by class flag
        :param class_weight: class weights
        :param class_benchmark_weight: class benchmark weights
        :param overall_benchmark_weight: overall benchmark weights
        :param digit: scale (number of fraction digits)(default value: 5)
        """
        self.scores = None
        self.sorted = None
        self.classes = None
        __compare_assign_handler__(
            self,
            cm_dict,
            class_weight,
            class_benchmark_weight,
            overall_benchmark_weight,
            digit)
        __compare_class_handler__(self, cm_dict)
        __compare_overall_handler__(self, cm_dict)
        __compare_rounder__(self, cm_dict)
        scores_list = list(self.scores.values())
        (max_overall_name, max_class_name) = __compare_sort_handler__(self)
        if scores_list.count(self.scores[max_class_name]) == 1:
            if by_class:
                self.best = cm_dict[max_class_name]
                self.best_name = max_class_name
            else:
                if max_overall_name == max_class_name:
                    self.best = cm_dict[max_class_name]
                    self.best_name = max_overall_name
                else:
                    warn(COMPARE_RESULT_WARNING, RuntimeWarning)
        else:
            warn(COMPARE_RESULT_WARNING, RuntimeWarning)

    def print_report(self) -> None:
        """Print Compare report."""
        report = compare_report_print(
            self.sorted, self.scores, self.best_name)
        print(report)

    def save_report(
            self,
            name: str,
            address: bool=True) -> Dict[str, Union[bool, str]]:
        """
        Save Compare report in .comp (flat file format).

        :param name: filename
        :param address: flag for address return
        """
        try:
            message = None
            file = open(name + ".comp", "w")
            report = compare_report_print(
                self.sorted, self.scores, self.best_name)
            file.write(report)
            file.close()
            if address:
                message = os.path.join(
                    os.getcwd(), name + ".comp")  # pragma: no cover
            return {"Status": True, "Message": message}
        except Exception as e:
            return {"Status": False, "Message": str(e)}

    def __repr__(self) -> str:
        """Compare object representation method."""
        return "pycm.Compare(classes: " + str(self.classes) + ")"

    def __str__(self) -> str:
        """Compare object string representation method."""
        report = compare_report_print(
            self.sorted, self.scores, self.best_name)
        return report


def __compare_class_handler__(compare: "Compare", cm_dict: Dict[str, "ConfusionMatrix"]) -> None:
    """
    Handle class score of Compare class.

    :param compare: Compare
    :param cm_dict: dictionary of confusion matrices
    """
    class_weight_sum = sum(compare.class_weight.values())
    class_benchmark_weight_sum = sum(compare.class_benchmark_weight.values())
    for c in compare.classes:
        for item in CLASS_BENCHMARK_SCORE_DICT:
            max_item_score = len(CLASS_BENCHMARK_SCORE_DICT[item]) - 1
            all_class_score = [CLASS_BENCHMARK_SCORE_DICT[item][
                cm.class_stat[item][c]] for cm in cm_dict.values()]
            if all([isinstance(x, int) for x in all_class_score]):
                for cm_name in cm_dict:
                    score = (compare.class_weight[c] / class_weight_sum) * (
                        CLASS_BENCHMARK_SCORE_DICT[item][cm_dict[cm_name].class_stat[item][c]] / max_item_score)
                    score = score * \
                        (compare.class_benchmark_weight[item] / class_benchmark_weight_sum)
                    compare.scores[cm_name]["class"] += score


def __compare_overall_handler__(compare: "Compare", cm_dict: Dict[str, "ConfusionMatrix"]) -> None:
    """
    Handle overall score of Compare class.

    :param compare: Compare
    :param cm_dict: dictionary of confusion matrices
    """
    overall_benchmark_weight_sum = sum(
        compare.overall_benchmark_weight.values())
    for item in OVERALL_BENCHMARK_SCORE_DICT:
        max_item_score = len(OVERALL_BENCHMARK_SCORE_DICT[item]) - 1
        all_overall_score = [OVERALL_BENCHMARK_SCORE_DICT[item][
            cm.overall_stat[OVERALL_BENCHMARK_MAP[item]]] for cm in cm_dict.values()]
        if all([isinstance(x, int) for x in all_overall_score]):
            for cm_name in cm_dict:
                score = OVERALL_BENCHMARK_SCORE_DICT[item][cm_dict[cm_name]
                                                           .overall_stat[OVERALL_BENCHMARK_MAP[item]]] / max_item_score
                score = score * \
                    (compare.overall_benchmark_weight[item] / overall_benchmark_weight_sum)
                compare.scores[cm_name]["overall"] += score


def __compare_rounder__(compare: "Compare", cm_dict: Dict[str, "ConfusionMatrix"]) -> None:
    """
    Round Compare.scores .

    :param compare: Compare object
    :param cm_dict: dictionary of confusion matrices
    """
    for cm_name in cm_dict:
        compare.scores[cm_name]["overall"] = numpy.around(
            compare.scores[cm_name]["overall"], compare.digit)
        compare.scores[cm_name]["class"] = numpy.around(
            compare.scores[cm_name]["class"], compare.digit)


def __compare_sort_handler__(compare: "Compare") -> Tuple[str, str]:
    """
    Handle sorting of scores.

    :param compare: Compare
    """
    sorted_by_class = sorted(
        compare.scores,
        key=lambda x: (
            compare.scores[x]['class'],
            compare.scores[x]['overall']))
    sorted_by_overall = sorted(
        compare.scores,
        key=lambda x: (
            compare.scores[x]['overall'],
            compare.scores[x]['class']))
    sorted_by_class.reverse()
    sorted_by_overall.reverse()
    compare.sorted = sorted_by_class
    max_overall_name = sorted_by_overall[0]
    max_class_name = sorted_by_class[0]
    return (max_overall_name, max_class_name)


def __compare_weight_handler__(compare: "Compare", weight: Dict[str, float], weight_type: str) -> None:
    """
    Handle different weights validation.

    :param compare: Compare
    :param weight: input weight
    :param weight_type: input weight type
    """
    valid_dict = {
        "class_weight": compare.classes,
        "class_benchmark_weight": CLASS_BENCHMARK_SCORE_DICT.keys(),
        "overall_benchmark_weight": OVERALL_BENCHMARK_SCORE_DICT.keys()}
    error_dict = {
        "class_weight": COMPARE_CLASS_WEIGHT_ERROR,
        "class_benchmark_weight": COMPARE_CLASS_BENCHMARK_WEIGHT_ERROR,
        "overall_benchmark_weight": COMPARE_OVERALL_BENCHMARK_WEIGHT_ERROR}
    warning_dict = {
        "class_weight": COMPARE_CLASS_WEIGHT_WARNING,
        "class_benchmark_weight": COMPARE_CLASS_BENCHMARK_WEIGHT_WARNING,
        "overall_benchmark_weight": COMPARE_OVERALL_BENCHMARK_WEIGHT_WARNING}
    if weight is None:
        return None
    if not isinstance(weight, dict):
        raise pycmCompareError(error_dict[weight_type])
    if set(weight) == set(valid_dict[weight_type]):
        if all([isfloat(x) for x in weight.values()]
               ) and sum(weight.values()) != 0:
            setattr(compare, weight_type, weight)
        else:
            warn(warning_dict[weight_type], RuntimeWarning)
    else:
        raise pycmCompareError(error_dict[weight_type])


def __compare_assign_handler__(
        compare: "Compare",
        cm_dict: Dict[str, "ConfusionMatrix"],
        class_weight: Dict[str, float],
        class_benchmark_weight: Dict[str, float],
        overall_benchmark_weight: Dict[str, float],
        digit: int) -> None:
    """
    Assign basic parameters to Compare.

    :param compare: Compare
    :param cm_dict: dictionary of confusion matrices
    :param class_weight: class weights
    :param class_benchmark_weight: class benchmark weights
    :param overall_benchmark_weight: overall benchmark weights
    :param digit: scale (number of fraction digits)(default value: 5)
    """
    if not isinstance(cm_dict, dict):
        raise pycmCompareError(COMPARE_FORMAT_ERROR)
    if not all(isinstance(item, ConfusionMatrix)
               for item in cm_dict.values()):
        raise pycmCompareError(COMPARE_TYPE_ERROR)
    if any(item.metrics_off for item in cm_dict.values()):
        raise pycmCompareError(COMPARE_METRICS_OFF_ERROR)
    if not list_check_equal([getattr(item, "POP")
                             for item in cm_dict.values()]):
        raise pycmCompareError(COMPARE_DOMAIN_ERROR)
    if len(cm_dict) < 2:
        raise pycmCompareError(COMPARE_NUMBER_ERROR)
    compare.classes = list(cm_dict.values())[0].classes
    compare.class_weight = {k: 1 for k in compare.classes}
    compare.class_benchmark_weight = {k: 1 for k in CLASS_BENCHMARK_LIST}
    compare.overall_benchmark_weight = {
        k: 0 if k in KAPPA_BENCHMARK_LIST[1:] else 1 for k in OVERALL_BENCHMARK_LIST}
    compare.digit = digit
    compare.best = None
    compare.best_name = None
    compare.sorted = None
    compare.scores = {k: {"overall": 0, "class": 0}.copy()
                      for k in cm_dict}
    __compare_weight_handler__(compare, class_weight, "class_weight")
    __compare_weight_handler__(
        compare,
        class_benchmark_weight,
        "class_benchmark_weight")
    __compare_weight_handler__(
        compare,
        overall_benchmark_weight,
        "overall_benchmark_weight")
