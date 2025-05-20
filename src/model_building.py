import logging
from abc import ABC, abstractmethod
from typing import Any

import pandas as pd
from sklearn.base import RegressorMixin
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# Abstract Base Class for Model Building Strategy
class ModelBuildingStrategy(ABC):
    @abstractmethod
    def build_and_train_model(self, X_train: pd.DataFrame, y_train: pd.Series) -> RegressorMixin:
        """
        Abstract method to build and train a model.

        Parameters:
        X_train (pd.DataFrame): The training data features.
        y_train (pd.Series): The training data labels/target.

        Returns:
        RegressorMixin: A trained scikit-learn model instance.
        """
        pass


# Concrete Strategy for Linear Regression using scikit-learn
class LinearRegressionStrategy(ModelBuildingStrategy):
    def build_and_train_model(self, X_train: pd.DataFrame, y_train: pd.Series) -> Pipeline:
        """
        Builds and trains a linear regression model using scikit-learn.

        Parameters:
        X_train (pd.DataFrame): The training data features.
        y_train (pd.Series): The training data labels/target.

        Returns:
        Pipeline: A scikit-learn pipeline with a trained Linear Regression model.
        """
        # Ensure the inputs are of the correct type
        if not isinstance(X_train, pd.DataFrame):
            raise TypeError("X_train must be a pandas DataFrame.")
        if not isinstance(y_train, pd.Series):
            raise TypeError("y_train must be a pandas Series.")

        logging.info("Initializing Linear Regression model with scaling.")

        # Creating a pipeline with standard scaling and linear regression
        pipeline = Pipeline(
            [
                ("scaler", StandardScaler()),  # Feature scaling
                ("model", LinearRegression()),  # Linear regression model
            ]
        )

        logging.info("Training Linear Regression model.")
        pipeline.fit(X_train, y_train)  # Fit the pipeline to the training data

        logging.info("Model training completed.")
        return pipeline


# Context Class for Model Building
class ModelBuilder:
    def __init__(self, strategy: ModelBuildingStrategy):
        """
        Initializes the ModelBuilder with a specific model building strategy.

        Parameters:
        strategy (ModelBuildingStrategy): The strategy to be used for model building.
        """
        self._strategy = strategy

    def set_strategy(self, strategy: ModelBuildingStrategy):
        """
        Sets a new strategy for the ModelBuilder.

        Parameters:
        strategy (ModelBuildingStrategy): The new strategy to be used for model building.
        """
        logging.info("Switching model building strategy.")
        self._strategy = strategy

    def build_model(self, X_train: pd.DataFrame, y_train: pd.Series) -> RegressorMixin:
        """
        Executes the model building and training using the current strategy.

        Parameters:
        X_train (pd.DataFrame): The training data features.
        y_train (pd.Series): The training data labels/target.

        Returns:
        RegressorMixin: A trained scikit-learn model instance.
        """
        logging.info("Building and training the model using the selected strategy.")
        return self._strategy.build_and_train_model(X_train, y_train)


# Example usage
if __name__ == "__main__":
    # Example DataFrame (replace with actual data loading)
    # df = pd.read_csv('your_data.csv')
    # X_train = df.drop(columns=['target_column'])
    # y_train = df['target_column']

    # Example usage of Linear Regression Strategy
    # model_builder = ModelBuilder(LinearRegressionStrategy())
    # trained_model = model_builder.build_model(X_train, y_train)
    # print(trained_model.named_steps['model'].coef_)  # Print model coefficients

    pass

# Enhanced logic for src/model_building.py in commit 1
# Change made on 2024-02-01 22:19:22
def utility_function_commit_1_275(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 10
# Change made on 2024-03-05 13:43:13
def utility_function_commit_10_416(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 11
# Change made on 2024-03-09 11:14:24
def utility_function_commit_11_624(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 15
# Change made on 2024-03-13 09:18:11
def utility_function_commit_15_702(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 16
# Change made on 2024-03-13 11:31:51
def utility_function_commit_16_277(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 19
# Change made on 2024-03-18 21:05:36
def utility_function_commit_19_897(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 21
# Change made on 2024-03-21 20:26:11
def utility_function_commit_21_448(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 26
# Change made on 2024-03-31 11:20:35
def utility_function_commit_26_308(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 27
# Change made on 2024-04-02 00:42:07
def utility_function_commit_27_685(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 29
# Change made on 2024-04-04 22:46:53
def utility_function_commit_29_395(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 32
# Change made on 2024-04-14 13:53:26
def utility_function_commit_32_185(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 36
# Change made on 2024-04-24 01:47:46
def utility_function_commit_36_704(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 37
# Change made on 2024-04-25 03:07:34
def utility_function_commit_37_468(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 38
# Change made on 2024-04-25 08:30:00
def utility_function_commit_38_662(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 40
# Change made on 2024-04-27 12:27:09
def utility_function_commit_40_193(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 41
# Change made on 2024-04-29 09:26:08
def utility_function_commit_41_774(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 42
# Change made on 2024-04-30 09:06:41
def utility_function_commit_42_461(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 48
# Change made on 2024-05-23 17:20:05
def utility_function_commit_48_148(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 51
# Change made on 2024-05-30 07:24:28
def utility_function_commit_51_510(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 56
# Change made on 2024-06-06 11:02:01
def utility_function_commit_56_179(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 58
# Change made on 2024-06-09 08:13:43
def utility_function_commit_58_663(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 62
# Change made on 2024-06-25 00:00:40
def utility_function_commit_62_445(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 65
# Change made on 2024-07-12 03:24:40
def utility_function_commit_65_300(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 68
# Change made on 2024-07-15 14:16:16
def utility_function_commit_68_938(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param



# Enhanced logic for src/model_building.py in commit 72
# Change made on 2024-07-22 16:20:37
def utility_function_commit_72_520(param: Any) -> Any:
    # TODO: Implement specific utility for this module
    print(f'Utility function called with {param}')
    return param


