# -*- coding: utf-8 -*-
"""Outputs functions."""
from __future__ import division
from typing import List, Dict, Tuple, Any, Optional, Union
from functools import partial
from .params import *
from .utils import rounder, sort_char_num
import webbrowser


def html_dataset_type(is_binary: bool, is_imbalanced: bool) -> str:
    """
    Return HTML report file dataset type.

    :param is_binary: is_binary flag (True: binary, False: multi-class)
    :param is_imbalanced: is_imbalanced flag (True: imbalance, False: balance)
    """
    return HTML_DATASET_TYPE_TEMPLATE.format(
        balance_type="Imbalanced" if is_imbalanced else "Balanced",
        class_type="Binary Classification" if is_binary else "Multi-Class Classification",
        message1=RECOMMEND_HTML_MESSAGE,
        message2=RECOMMEND_HTML_MESSAGE2)


def color_check(color: Any) -> List[int]:
    """
    Check input color format.

    :param color: input color
    """
    if isinstance(color, (tuple, list)) and all(map(lambda x: isinstance(x, int) and x < 256, color)):
        return list(color)
    if isinstance(color, str) and color.lower() in TABLE_COLOR:
        return TABLE_COLOR[color.lower()]
    return [0, 0, 0]


def html_table_color(row: dict, item: int, color: Tuple[int, int, int]=(0, 0, 0)) -> List[int]:
    """
    Return background color of each cell of the table.

    :param row: row dictionary
    :param item: cell number
    :param color: input color
    """
    color_list = color_check(color)
    back_color_index = 255 - int((item / (sum(list(row.values())) + 1)) * 255)
    color_offset = back_color_index - max(color_list)
    return [max(0, color_offset + c) for c in color_list]


def html_table(
        classes: List[Any],
        table: Dict[str, Dict[str, int]],
        rgb_color: Tuple[int, int, int],
        normalize: bool=False,
        shortener: bool=True) -> str:
    """
    Return the confusion matrix of the HTML report file.

    :param classes: confusion matrix classes
    :param table: input confusion matrix
    :param rgb_color: input color
    :param normalize: save normalized matrix flag
    :param shortener: class name shortener flag
    """
    result = ""
    result += "<h2>Confusion Matrix "
    if normalize:
        result += "(Normalized)"
    result += ": </h2>\n"
    result += '<table>\n'
    result += '<tr style="text-align:center;">' + "\n"
    result += '<td>Actual</td>\n'
    result += '<td>Predict\n'
    table_size = str((len(classes) + 1) * 7) + "em"
    result += '<table style="border:1px solid black;border-collapse: collapse;height:{size};width:{size};">\n'\
        .format(size=table_size)
    result += '<tr style="text-align:center;">\n<td></td>\n'
    part_2 = ""
    for i in classes:
        class_name = str(i)
        if len(class_name) > 6 and shortener:
            class_name = class_name[:4] + "..."
        result += '<td style="border:1px solid ' \
                  'black;padding:10px;height:7em;width:7em;">' + \
            class_name + '</td>\n'
        part_2 += '<tr style="text-align:center;">\n'
        part_2 += '<td style="border:1px solid ' \
                  'black;padding:10px;height:7em;width:7em;">' + \
            class_name + '</td>\n'
        for j in classes:
            item = table[i][j]
            color = "black"
            back_color = html_table_color(table[i], item, rgb_color)
            if min(back_color) < 128:
                color = "white"
            part_2 += '<td style="background-color:rgb({r},{g},{b});color:{color};padding:10px;height:7em;width:7em;">'.format(
                r=str(back_color[0]), g=str(back_color[1]), b=str(back_color[2]), color=color) + str(item) + '</td>\n'
        part_2 += "</tr>\n"
    result += '</tr>\n'
    part_2 += "</table>\n</td>\n</tr>\n</table>\n"
    result += part_2
    return result


def html_overall_stat(
        overall_stat: Dict[str, Union[float, int, str]],
        digit: int=5,
        overall_param: Optional[List[str]]=None,
        recommended_list: Union[list, tuple]=(),
        alt_link: bool=False) -> str:
    """
    Return the overall stats of HTML report file.

    :param overall_stat: overall stats
    :param digit: scale (number of fraction digits)(default value: 5)
    :param overall_param: overall parameters list for print, Example: ["Kappa", "Scott PI"]
    :param recommended_list: recommended statistics list
    :param alt_link: alternative link for document flag
    """
    document_link = DOCUMENT_ADR
    if alt_link:
        document_link = DOCUMENT_ADR_ALT
    result = ""
    result += "<h2>Overall Statistics : </h2>\n"
    result += '<table style="border:1px solid black;border-collapse: collapse;">\n'
    overall_stat_keys = sort_char_num(overall_stat.keys())
    if isinstance(overall_param, list):
        if set(overall_param) <= set(overall_stat_keys):
            overall_stat_keys = sort_char_num(overall_param)
    if len(overall_stat_keys) < 1:
        return ""
    for i in overall_stat_keys:
        background_color = DEFAULT_BACKGROUND_COLOR
        if i in recommended_list:
            background_color = RECOMMEND_BACKGROUND_COLOR
        result += '<tr style="text-align:center;">\n'
        result += '<td style="border:1px solid black;padding:4px;text-align:left;background-color:{color};"><a href="'.format(
            color=background_color) + document_link + PARAMS_LINK[i] + '" style="text-decoration:None;">' + str(i) + '</a></td>\n'
        if i in BENCHMARK_LIST:
            background_color = BENCHMARK_COLOR[i][overall_stat[i]]
            result += '<td style="border:1px solid black;padding:4px;background-color:{color};">'.format(
                color=background_color)
        else:
            result += '<td style="border:1px solid black;padding:4px;">'
        result += rounder(overall_stat[i], digit) + '</td>\n'
        result += "</tr>\n"
    result += "</table>\n"
    return result


def html_class_stat(
        classes: List[Any],
        class_stat: Dict[str, Dict[str, Union[float, int, str]]],
        digit: int=5,
        class_param: Optional[List[str]]=None,
        recommended_list: Union[list, tuple]=(),
        alt_link: bool=False) -> str:
    """
    Return the class-based stats of HTML report file.

    :param classes: confusion matrix classes
    :param class_stat: class stat
    :param digit: scale (number of fraction digits)(default value: 5)
    :param class_param: class parameters list for print, Example: ["TPR", "TNR", "AUC"]
    :param recommended_list: recommended statistics list
    :param alt_link: alternative link for document flag
    """
    document_link = DOCUMENT_ADR
    if alt_link:
        document_link = DOCUMENT_ADR_ALT
    result = ""
    result += "<h2>Class Statistics : </h2>\n"
    result += '<table style="border:1px solid black;border-collapse: collapse;">\n'
    result += '<tr style="text-align:center;">\n<td>Class</td>\n'
    for i in classes:
        result += '<td style="border:1px solid black;padding:4px;border-collapse: collapse;">' + \
            str(i) + '</td>\n'
    result += '<td>Description</td>\n'
    result += '</tr>\n'
    class_stat_keys = sorted(class_stat)
    if isinstance(class_param, list):
        if set(class_param) <= set(class_stat_keys):
            class_stat_keys = class_param
    if len(classes) < 1 or len(class_stat_keys) < 1:
        return ""
    for i in class_stat_keys:
        background_color = DEFAULT_BACKGROUND_COLOR
        if i in recommended_list:
            background_color = RECOMMEND_BACKGROUND_COLOR
        result += '<tr style="text-align:center;border:1px solid black;border-collapse: collapse;">\n'
        result += '<td style="border:1px solid black;padding:4px;border-collapse: collapse;background-color:{color};"><a href="'.format(
            color=background_color) + document_link + PARAMS_LINK[i] + '" style="text-decoration:None;">' + str(i) + '</a></td>\n'
        for j in classes:
            if i in BENCHMARK_LIST:
                background_color = BENCHMARK_COLOR[i][class_stat[i][j]]
                result += '<td style="border:1px solid black;padding:4px;border-collapse: collapse;background-color:{color};">'.format(
                    color=background_color)
            else:
                result += '<td style="border:1px solid black;padding:4px;border-collapse: collapse;">'
            result += rounder(class_stat[i][j], digit) + '</td>\n'
        params_text = PARAMS_DESCRIPTION[i]
        if i not in CAPITALIZE_FILTER:
            params_text = params_text.capitalize()
        result += '<td style="border:1px solid black;padding:4px;border-collapse: collapse;text-align:left;">' + \
                  params_text + '</td>\n'
        result += "</tr>\n"
    result += "</table>\n"
    return result


def pycm_help() -> None:
    """Print pycm details."""
    print(OVERVIEW)
    print("Repo : https://github.com/sepandhaghighi/pycm")
    print("Webpage : https://www.pycm.io")


def table_print(classes: List[Any], table: Dict[str, Dict[str, int]]) -> str:
    """
    Return printable confusion matrix.

    :param classes: confusion matrix classes
    :param table: input confusion matrix
    """
    classes_len = len(classes)
    table_list = []
    for key in classes:
        table_list.extend(list(table[key].values()))
    table_list.extend(classes)
    table_max_length = max(map(len, map(str, table_list)))
    shift = "%-" + str(7 + table_max_length) + "s"
    result = shift % "Predict" + shift * \
        classes_len % tuple(map(str, classes)) + "\n"
    result = result + "Actual\n"
    for key in classes:
        row = [table[key][i] for i in classes]
        result += shift % str(key) + \
            shift * classes_len % tuple(map(str, row)) + "\n\n"
    return result


def sparse_table_print(sparse_matrix: Tuple[Dict[Any, Dict[Any, int]], List[Any], List[Any]]) -> str:
    """
    Return printable confusion matrix in sparse mode.

    :param sparse_matrix: list of the sparse matrix and it's classes
    """
    [sparse_table, actual_classes, predict_classes] = sparse_matrix
    predict_classes.sort()
    actual_classes.sort()
    classes_len = len(predict_classes)
    table_list = []
    for key in actual_classes:
        table_list.extend(list(sparse_table[key].values()))
    table_list.extend(predict_classes)
    table_max_length = max(map(len, map(str, table_list)))
    shift = "%-" + str(7 + table_max_length) + "s"
    result = shift % "Predict" + shift * \
        classes_len % tuple(map(str, predict_classes)) + "\n"
    result = result + "Actual\n"
    for key in actual_classes:
        row = [sparse_table[key][i] for i in predict_classes]
        result += shift % str(key) + \
            shift * classes_len % tuple(map(str, row)) + "\n\n"
    return result


def csv_matrix_print(classes: List[Any], table: Dict[str, Dict[str, int]], header: bool=False) -> str:
    """
    Return matrix as csv data.

    :param classes: confusion matrix classes
    :param table: input confusion matrix
    :param header: add headers to csv file
    """
    result = ""
    header_section = ""
    for i in classes:
        if header is True:
            header_section += '"' + str(i) + '"' + ","
        for j in classes:
            result += str(table[i][j]) + ","
        result = result[:-1] + "\n"
    if len(header_section) > 0:
        header_section = header_section[:-1] + "\n"
    result = header_section + result
    return result[:-1]


def csv_print(classes: List[Any], class_stat: Dict[str, Dict[str, Union[float, int, str]]],
              digit: int=5, class_param: Optional[List[str]]=None) -> str:
    """
    Return csv file data.

    :param classes: confusion matrix classes
    :param class_stat: statistic result for each class
    :param digit: scale (number of fraction digits)(default value: 5)
    :param class_param: class parameters list for print, Example: ["TPR", "TNR", "AUC"]
    """
    result = "Class"
    for item in classes:
        result += ',"' + str(item) + '"'
    result += "\n"
    class_stat_keys = sorted(class_stat)
    if isinstance(class_param, list):
        if set(class_param) <= set(class_stat_keys):
            class_stat_keys = class_param
    if len(class_stat_keys) < 1 or len(classes) < 1:
        return ""
    for key in class_stat_keys:
        row = [rounder(class_stat[key][i], digit) for i in classes]
        result += key + "," + ",".join(row)
        result += "\n"
    return result


def stat_print(
        classes: List[Any],
        class_stat: Dict[str, Dict[str, Union[float, int, str]]],
        overall_stat: Dict[str, Union[float, int, str]],
        digit: int=5,
        overall_param: Optional[List[str]]=None,
        class_param: Optional[List[str]]=None) -> str:
    """
    Return printable statistics table.

    :param classes: confusion matrix classes
    :param class_stat: statistic result for each class
    :param overall_stat: overall statistic result
    :param digit: scale (number of fraction digits)(default value: 5)
    :param overall_param: overall parameters list for print, Example: ["Kappa", "Scott PI"]
    :param class_param: class parameters list for print, Example: ["TPR", "TNR", "AUC"]
    """
    shift = max(map(len, PARAMS_DESCRIPTION.values())) + 5
    classes_len = len(classes)
    overall_stat_keys = sort_char_num(overall_stat.keys())
    result = ""
    if isinstance(overall_param, list):
        if set(overall_param) <= set(overall_stat_keys):
            overall_stat_keys = sort_char_num(overall_param)
    if len(overall_stat_keys) > 0:
        result = "Overall Statistics : " + "\n\n"
        for key in overall_stat_keys:
            result += key + " " * (shift - len(key) + 7) + \
                rounder(overall_stat[key], digit) + "\n"
    class_stat_keys = sorted(class_stat)
    if isinstance(class_param, list):
        if set(class_param) <= set(class_stat_keys):
            class_stat_keys = sorted(class_param)
    if len(class_stat_keys) > 0 and len(classes) > 0:
        class_shift = max(
            max(map(lambda x: len(str(x)), classes)) + 5, digit + 6, 14)
        class_shift_format = "%-" + str(class_shift) + "s"
        result += "\nClass Statistics :\n\n"
        result += "Classes" + shift * " " + class_shift_format * \
            classes_len % tuple(map(str, classes)) + "\n"
        rounder_map = partial(rounder, digit=digit)
        for key in class_stat_keys:
            row = [class_stat[key][i] for i in classes]
            params_text = PARAMS_DESCRIPTION[key]
            if key not in CAPITALIZE_FILTER:
                params_text = params_text.capitalize()
            result += key + "(" + params_text + ")" + " " * (
                shift - len(key) - len(PARAMS_DESCRIPTION[key]) + 5) + class_shift_format * classes_len % tuple(
                map(rounder_map, row)) + "\n"
    return result


def compare_report_print(sorted_list: List[str], scores: Dict[str, float], best_name: str) -> str:
    """
    Return compare report.

    :param sorted_list: sorted list of confusion matrices
    :param scores: scores of confusion matrices
    :param best_name: best confusion matrix name
    """
    title_items = ["Rank", "Name", "Class-Score", "Overall-Score"]
    class_scores_len = map(lambda x: len(
        str(x["class"])), list(scores.values()))
    shifts = ["%-" +
              str(len(sorted_list) +
                  4) +
              "s", "%-" +
              str(max(map(lambda x: len(str(x)), sorted_list)) +
                  4) +
              "s", "%-" +
              str(max(class_scores_len) + 11) + "s"]
    result = ""
    result += "Best : " + str(best_name) + "\n\n"
    result += ("".join(shifts)
               ) % tuple(title_items[:-1]) + title_items[-1] + "\n"
    prev_rank = 0
    for index, cm in enumerate(sorted_list):
        rank = index
        if scores[sorted_list[rank]] == scores[sorted_list[prev_rank]]:
            rank = prev_rank
        result += ("".join(shifts)) % (str(rank + 1), str(cm),
                                       str(scores[cm]["class"])) + str(scores[cm]["overall"]) + "\n"
        prev_rank = rank
    return result


def online_help(param: Optional[Union[str, int]]=None, alt_link: bool=False) -> None:
    """
    Open online document in web browser.

    :param param: input parameter
    :param alt_link: alternative link for document flag
    """
    try:
        document_link = DOCUMENT_ADR
        if alt_link:
            document_link = DOCUMENT_ADR_ALT
        params_link_keys = sort_char_num(PARAMS_LINK.keys())
        if param in params_link_keys:
            webbrowser.open_new_tab(document_link + PARAMS_LINK[param])
        elif param in range(1, len(params_link_keys) + 1):
            webbrowser.open_new_tab(
                document_link + PARAMS_LINK[params_link_keys[param - 1]])
        else:
            print("Please choose one parameter : \n")
            print('Example : online_help("J") or online_help(2)\n')
            for index, item in enumerate(params_link_keys):
                print(str(index + 1) + "-" + item)
    except Exception:  # pragma: no cover
        print("Error in online help")
