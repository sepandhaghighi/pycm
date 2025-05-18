# -*- coding: utf-8 -*-
"""This file contains a function to generate a random confusion matrix."""
import numpy as np
from enum import Enum


class ClassDistributionScenario(Enum):
    """
    Enum to represent different scenarios for generating class percentages.

    - UNIFORM: All classes have equal representation.
    - MAJORITY_CLASS: Only one class has a majority representation, others are minority.
    - MINORITY_CLASS: Only one class has a minority representation, others are majority.
    """
    
    UNIFORM = "uniform"
    MAJORITY_CLASS = "majority_class"
    MINORITY_CLASS = "minority_class"


def _generate_class_percentages(num_classes, scenario):
    """
    Generate class percentages based on the given scenario.

    :params num_classes: number of classes.
    :type num_classes: int
    :params scenario: the scenario to generate percentages for.
    :type scenario: scenario
    :return: list of percentages for each class.
    """
    if num_classes < 2:
        raise ValueError("Number of classes must be at least 2.")
    if scenario == ClassDistributionScenario.UNIFORM:
        # Equal percentage for all classes
        return [100 / num_classes] * num_classes
    elif scenario == ClassDistributionScenario.MAJORITY_CLASS:
        # One class has a majority class, others share the rest equally
        raw_ratio_list = [5] + [1] * (num_classes - 1)
    elif scenario == ClassDistributionScenario.MINORITY_CLASS:
        # One class has a minority percentage, others share the rest equally
        raw_ratio_list = [0.2] + [1] * (num_classes - 1)
    else:
        raise ValueError("Invalid scenario")

    return list((100 * np.array(raw_ratio_list)) / np.sum(raw_ratio_list))

def _calculate_class_counts(class_percentages, total_population):
    """
    Calculate the number of samples for each class based on percentages and total population.

    :param class_percentages: dict of percentages for each class (sum should be 100)
    :type class_percentages: dict
    :param total_population: total number of samples
    :type total_population: int
    :return: dictionary of sample counts for each class
    """
    classes = list(class_percentages.keys())
    percentages = np.array(list(class_percentages.values()), dtype=float)

    if len(classes) < 2:
        raise ValueError("Number of classes must be at least 2.")

    normalized_percentages = percentages / percentages.sum()
    class_counts = (normalized_percentages * total_population).astype(int)

    remainder = total_population - class_counts.sum()
    if remainder > 0:
        class_counts[np.argmax(normalized_percentages)] += remainder

    return dict(zip(classes, class_counts.astype(int).tolist()))


def generate_confusion_matrix(class_percentages, total_population):
    """
    Generate a random confusion matrix with given class percentages and total population.

    :param class_percentages: dict or list of percentages for each class (sum should be 100)
    :type class_percentages: dict or list
    :param  total_population: total number of samples in the confusion matrix
    :type total_population: int
    :return: confusion matrix as a dictionary
    """
    if total_population <= 0:
        raise ValueError("Total population must be positive.")
    if isinstance(class_percentages, list):
        class_percentages = dict(enumerate(class_percentages))

    class_labels = list(class_percentages.keys())
    num_classes = len(class_percentages)

    if num_classes < 2:
        raise ValueError("Number of classes must be at least 2.")

    class_counts = _calculate_class_counts(class_percentages, total_population)
    confusion_matrix = {
        actual: {pred: 0 for pred in class_labels} for actual in class_labels
    }

    for actual in class_labels:
        count = class_counts[actual]
        if count == 0:
            continue

        dirichlet_params = np.ones(num_classes)
        actual_idx = class_labels.index(actual)
        dirichlet_params[actual_idx] *= 10  # Bias toward correct class

        probs = np.random.dirichlet(dirichlet_params)
        predicted_counts = (probs * count).astype(int)

        remainder = count - predicted_counts.sum()
        if remainder > 0:
            predicted_counts[np.argmax(probs)] += remainder

        for pred_idx, pred_class in enumerate(class_labels):
            confusion_matrix[actual][pred_class] = int(predicted_counts[pred_idx])

    return confusion_matrix


def generate_confusion_matrix_with_scenario(
    num_classes, total_population, scenario=ClassDistributionScenario.UNIFORM
):
    """
    Generate a random confusion matrix based on the given scenario.

    :param num_classes: number of classes.
    :type num_classes: int
    :param total_population: total number of samples.
    :type total_population: int
    :param scenario: the scenario to generate the confusion matrix for.
    :type scenario: ClassDistributionScenario
    :return: confusion matrix as a dictionary.
    """
    if isinstance(scenario, str):
        try:
            scenario = ClassDistributionScenario[scenario.upper()]
        except KeyError:
            raise ValueError(f"Invalid scenario. Must be one of {[sen.value for sen in ClassDistributionScenario]}.")
    class_percentages = _generate_class_percentages(num_classes, scenario)
    return generate_confusion_matrix(class_percentages, total_population)
