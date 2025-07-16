# -*- coding: utf-8 -*-
"""This file runs benchmarks for the pycm library based on specific scenarios."""

from argparse import ArgumentParser
from itertools import product
import numpy as np
from pycm.generate_random_data import generate_confusion_matrix_with_scenario
from pycm.generate_random_data import ClassDistributionScenario
from pycm import ConfusionMatrix


def evaluate_sample(num_classes, total_population, scenario, seed=None):
    """
    Generate a confusion matrix based on the specified scenario and parameters.

    This function is used to evaluate the performance of the pycm library under different class distribution scenarios

    :param num_classes: Number of classes in the confusion matrix.
    :type num_classes: int
    :param total_population: Total number of samples to generate.
    :type total_population: int
    :param scenario: The scenario for class distribution.
    :type scenario: str
    :param seed: Random seed for reproducibility.
    :type seed: int or None
    :return: Generated confusion matrix.
    """
    if seed is not None:
        np.random.seed(seed)

    confusion_matrix = generate_confusion_matrix_with_scenario(
        num_classes=num_classes,
        total_population=total_population,
        scenario=scenario
    )
    confusion_matrix = ConfusionMatrix(
        matrix=confusion_matrix
    )

    return {
        "timing": confusion_matrix.timings,
        "num_classes": num_classes,
        "total_population": total_population,
        "scenario": scenario
    }


def print_result(result):
    """
    Print the result of the evaluation in a readable format.

    :param result: Result dictionary containing timing and parameters.
    :type result: dict
    :return: None
    """
    print(f"Number of classes: {result['num_classes']}")
    print(f"Total population: {result['total_population']}")
    print(f"Class distribution scenario: {result['scenario']}")

    print(f"Timing:")
    for key, value in result["timing"].items():
        print(f"  {key.replace('_', ' ').capitalize()}: {value} s")
    print("\n")


if __name__ == "__main__":
    parser = ArgumentParser(description="Run benchmarks for the pycm library.")
    parser.add_argument('--report', action='store_true',
                        help="Generate a report of the confusion matrix (default: False)")
    parser.add_argument("-N", "--total-population", type=int, default=1000,
                        help="Total number of samples to generate (default: 1000)")
    parser.add_argument("-m", "--num-classes", type=int, default=5,
                        help="Number of classes in the confusion matrix (default: 5)")
    parser.add_argument("--scenario", type=str, choices=[s.value for s in ClassDistributionScenario],
                        default=ClassDistributionScenario.UNIFORM.value,
                        help="Class distribution scenario (default: 'uniform')")
    parser.add_argument("--seed", type=int, default=0,
                        help="Random seed for reproducibility (default: 0)")
    args = parser.parse_args()

    if not args.report:
        result = evaluate_sample(
            num_classes=args.num_classes,
            total_population=args.total_population,
            scenario=args.scenario,
            seed=args.seed
        )
        print_result(result)
    else:
        Ns = [10, 100, 1000, 10000, 100000]
        Ms = [2, 3, 5, 10, 20, 50, 100]
        scenarios = [s.value for s in ClassDistributionScenario]

        import pandas as pd

        results = []

        for N, M, scenario in product(Ns, Ms, scenarios):
            result = evaluate_sample(
                num_classes=M,
                total_population=N,
                scenario=scenario,
                seed=args.seed
            )
            timing = result.pop("timing")
            for key, value in timing.items():
                result[f"timing_{key}"] = value

            results.append(result)
        df = pd.DataFrame(results)
        df.to_csv("pycm_benchmark_results.csv", index=False)
