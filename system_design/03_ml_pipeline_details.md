# ML Pipeline Details

This document provides details about the machine learning pipeline.

## Stages

1.  **Data Ingestion:** Reads raw data from the specified source.
2.  **Data Preprocessing:**
    *   Handles missing values (e.g., imputation, removal).
    *   Performs feature engineering (e.g., creating new features, transforming existing ones).
    *   (Optional) Outlier detection and handling.
3.  **Data Splitting:** Divides the dataset into training and testing sets.
4.  **Model Training:** Trains a machine learning model on the training data.
5.  **Model Evaluation:** Evaluates the trained model's performance on the testing data using relevant metrics.

## Technologies

-   Pandas for data manipulation.
-   Scikit-learn for data splitting, model building, and evaluation.
-   (Future) MLflow for experiment tracking and model management.
