"""This is your main file. All the code that executes should run from here-
for Best Practices, refactor function blocks in appropriately named files in the
lib directory later as you see fit."""

# Import Setup Packages, Don't worry about this for now
from typing import TypeVar, Generic, Annotated


# Import Relevant Packages
try:
    import numpy as np
    import pandas as pd
    from pathlib import Path
except ImportError:
    print("Failed to import packages")

# Set Type Hints
# You can use these hints to keep track of what a variable should look like
# Note: They're hints and not facts
from numpy import ndarray
from pandas import DataFrame

FeatureSet = ndarray
TargetSet = ndarray
ModelWeights = ndarray

CostError = ndarray

# Set hyperparameter constants
# Be sure to tweak these to see what works best!
# Later when you use established frameworks and libraries, this is what
# you mainly do
LEARNING_RATE = 0.01
ITERATIONS = 1000

# Load Dataset. We will do it for you for now
# If you want to know the code, ask us for more info
try:
    data_root = Path("../titanic")
except:
    print("Data Path not set")
if data_root.exists():
    data_train = data_root / "train.csv"
    data_test = data_root / "test.csv"
try:
    dataset_train = pd.read_csv(data_train)
    dataset_test = pd.read_csv(data_test)
    print("Loaded Datasets succesfully ✅")
except:
    print("Failed to load Dataset")


def hypothesis_estimation(
    X: FeatureSet,
    theta: ModelWeights,
):
    """Fill in the function. This is a one liner"""
    ...


def mean_squared_error(
    X: FeatureSet,
    y: TargetSet,
    theta: ModelWeights,
):
    """Fill in the function with the MSE Cost"""
    ...


def gradient_descent(
    X: FeatureSet,
    y: TargetSet,
    theta: ModelWeights,
    learning_rate=LEARNING_RATE,
    iterations=ITERATIONS,
) -> ModelWeights:
    """Fill in the function with the gradient descent algorithm"""
    return theta


def main() -> None:
    """This should contain all the lines that actually run"""
    ...


if """__main__""" == __name__:
    main()
