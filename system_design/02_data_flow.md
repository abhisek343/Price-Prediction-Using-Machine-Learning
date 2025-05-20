# System Design: Data Flow 💧Pipeline

This document details the journey of data within the Prices Predictor System, from its raw form to the features used for model training and prediction.

## 1. Overview

The data flow is managed primarily by the ZenML pipeline, ensuring consistency and reproducibility in data transformations.
(For the raw Mermaid code, see [diagrams/02_data_flow_diagram.md](./diagrams/02_data_flow_diagram.md))

[![Data Flow Diagram](./diagrams/02_data_flow_diagram.md)](./diagrams/02_data_flow_diagram.md)
<!-- Note: GitHub might not render Mermaid from a relative link like this directly in an image tag. -->

## 2. Data Stages and Transformations

### Stage 1: Data Ingestion
*   **Input**: `data/archive.zip` containing `AmesHousing.csv`.
*   **Process**:
    *   The `data_ingestion_step` (using `DataIngestorFactory` and `ZipDataIngestor` from `src/ingest_data.py`) extracts `AmesHousing.csv` from the zip file into the `extracted_data/` directory.
    *   The CSV is then read into a Pandas DataFrame.
*   **Output**: Raw Pandas DataFrame with all original columns and rows.

### Stage 2: Handling Missing Values
*   **Input**: Raw DataFrame from Stage 1.
*   **Process**:
    *   The `handle_missing_values_step` (using `HandleMissingValues` and strategies like `MeanImputation` from `src/handle_missing_values.py`) processes the DataFrame.
    *   Numerical missing values are imputed using the mean strategy.
    *   Categorical missing values are imputed using the most frequent strategy.
*   **Output**: DataFrame with missing values imputed.

### Stage 3: Feature Engineering (Log Transformation)
*   **Input**: DataFrame from Stage 2.
*   **Process**:
    *   The `feature_engineering_step` (using `FeatureEngineer` and `LogTransformation` from `src/feature_engineering.py`) is applied.
    *   Specifically, `np.log1p` (log(1+x)) transformation is applied to features specified in the pipeline (e.g., `Gr Liv Area`, `SalePrice`). This helps normalize skewed distributions.
*   **Output**: DataFrame with specified features log-transformed. `SalePrice` (target variable) is now on a log1p scale.

### Stage 4: Outlier Detection
*   **Input**: DataFrame from Stage 3.
*   **Process**:
    *   The `outlier_detection_step` (using `OutlierDetector` and strategies like `ZScoreOutlierRemoval` from `src/outlier_detection.py`) identifies and removes outliers.
    *   For this project, it typically focuses on outliers in the target variable (`SalePrice` which is already log-transformed) or other critical features.
*   **Output**: DataFrame with outliers removed based on the chosen strategy.

### Stage 5: Data Splitting
*   **Input**: Cleaned DataFrame from Stage 4.
*   **Process**:
    *   The `data_splitter_step` (using `DataSplitter` from `src/data_splitter.py`) splits the data into training and testing sets.
    *   The target column (`SalePrice`, which is log1p-transformed) is separated into `y_train` and `y_test`.
    *   The remaining features form `X_train` and `X_test`.
*   **Output**: `X_train`, `X_test`, `y_train`, `y_test`.

## 3. Data Flow for Prediction

When making predictions (either via `sample_predict.py` or the Flask UI):

1.  **Input Data Preparation**:
    *   User provides raw input features.
    *   The script/application manually applies `np.log1p` to `Gr Liv Area` to match the transformation done during training pipeline's feature engineering step. This is critical because this specific transformation is *not* part of the scikit-learn pipeline logged by MLflow.
    *   Data types are ensured to match the schema expected by the MLflow model (e.g., converting certain integer inputs to floats like `GarageCars`).

2.  **Model Prediction**:
    *   The prepared Pandas DataFrame (with transformed `Gr Liv Area`) is passed to the `loaded_model.predict()` method.
    *   The loaded MLflow model (which is a scikit-learn `Pipeline`) internally handles further preprocessing defined in its `ColumnTransformer` (like imputation and one-hot encoding for categorical features) on the input data.
    *   The underlying regression model makes a prediction. This prediction is on the `log1p` scale because `y_train` was `log1p` transformed.

3.  **Output Postprocessing**:
    *   The raw prediction (on `log1p` scale) is inverse-transformed using `np.expm1()` to get the final predicted price on the original dollar scale.

This careful management of transformations at each stage, especially ensuring consistency between training and prediction, is key to accurate model performance.

---

Next: [03_ml_pipeline_details.md](./03_ml_pipeline_details.md) (Deep dive into the ZenML training pipeline)
