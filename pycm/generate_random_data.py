# -*- coding: utf-8 -*-
"""This file contains a function to generate a random confusion matrix."""
import numpy as np
from enum import Enum


class Scenario(Enum):
    """
    Enum to represent different scenarios for generating class percentages.

    - UNIFORM: All classes have equal representation.
    - MAJORITY_CLASS: One class has a majority representation, others are minority.
    - MINORITY_CLASS: One class has a minority representation, others are majority.
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
    if scenario == Scenario.UNIFORM:
        # Equal percentage for all classes
        return [100 / num_classes] * num_classes
    elif scenario == Scenario.MAJORITY_CLASS:
        # One class has a majority class, others share the rest equally
        majority_percentage = (100 / num_classes) * 5
        remaining_percentage = (100 - majority_percentage) / (num_classes - 1)
        return [majority_percentage] + [remaining_percentage] * (num_classes - 1)
    elif scenario == Scenario.MINORITY_CLASS:
        # One class has a minority percentage, others share the rest equally
        minority_percentage = (100 / num_classes) * 0.2
        remaining_percentage = (100 - minority_percentage) / (num_classes - 1)
        return [minority_percentage] + [remaining_percentage] * (num_classes - 1)
    else:
        raise ValueError("Invalid scenario")


def _calculate_class_counts(class_percentages, total_population):
    """
    Calculate the number of samples for each class based on percentages and total population.

    :param class_percentages: dict of percentages for each class (sum should be 100)
    :type class_percentages: dict
    :param total_population: total number of samples
    :type total_population: int
    :return: dictionary of sample counts for each class
    """
    # Normalize percentages to ensure they sum to 1 (to handle floating point inaccuracies)
    normalized_percentages = np.array(class_percentages) / sum(class_percentages)

    # Calculate the number of samples for each class
    class_counts = (normalized_percentages * total_population).astype(int)

    # Handle any remaining counts due to rounding
    remainder = total_population - sum(class_counts)
    if remainder > 0:
        class_counts[np.argmax(normalized_percentages)] += remainder

    return class_counts


def generate_confusion_matrix(class_percentages, total_population):
    """
    Generate a random confusion matrix with given class percentages and total population.

    :param class_percentages: dict or list of percentages for each class (sum should be 100)
    :type class_percentages: dict | list
    :param  total_population: total number of samples in the confusion matrix
    :type total_population: int
    :return: confusion matrix as a dictionary
    """
    num_classes = len(class_percentages)

    if num_classes < 2:
        raise ValueError("Number of classes must be at least 2.")

    class_counts = _calculate_class_counts(class_percentages, total_population)

    # Initialize confusion matrix
    confusion_matrix = np.zeros((num_classes, num_classes), dtype=int)

    # For each actual class (row)
    for i in range(num_classes):
        if class_counts[i] == 0:
            continue

        dirichlet_params = np.ones(num_classes)
        dirichlet_params[i] *= 10  # Makes the i-th element likely the largest

        # Generate probabilities where the i-th element is likely the largest
        probs = np.random.dirichlet(dirichlet_params)

        # Calculate counts for each predicted class
        counts = (probs * class_counts[i]).astype(int)

        # Handle any remaining counts due to rounding
        remainder = class_counts[i] - sum(counts)
        if remainder > 0:
            counts[np.argmax(probs)] += remainder

        # Assign to confusion matrix
        confusion_matrix[i, :] = counts

    return confusion_matrix


def generate_confusion_matrix_with_scenario(
    num_classes, total_population, scenario=Scenario.UNIFORM
):
    """
    Generate a random confusion matrix based on the given scenario.

    :param num_classes: number of classes.
    :type num_classes: int
    :param total_population: total number of samples.
    :type total_population: int
    :param scenario: the scenario to generate the confusion matrix for. Defaults to UNIFORM.
    :type scenario: Scenario
    :return: confusion matrix as a dictionary.
    """
    if isinstance(scenario, str):
        scenario = Scenario[scenario.upper()]
    class_percentages = _generate_class_percentages(num_classes, scenario)
    return generate_confusion_matrix(class_percentages, total_population)
