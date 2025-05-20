# System Design: ML Pipeline Details ⚙️🔬

This document dives into the specifics of the ZenML training pipeline (`ml_pipeline` defined in `pipelines/training_pipeline.py`) and its integration with MLflow for experiment tracking.

## 1. Pipeline Definition

The core training pipeline is defined using the `@pipeline` decorator from ZenML.

```python
# pipelines/training_pipeline.py (Simplified)

from zenml import Model, pipeline
# ... import steps ...

@pipeline(
    model=Model(
        name="prices_predictor", # ZenML Model name
        # version=None, # Can be specified or auto-incremented
        license="Apache 2.0",
        description="Price prediction model for houses."
    ),
    enable_cache=True # Or False, depending on desired behavior for steps
)
def ml_pipeline():
    raw_data = data_ingestion_step(file_path="data/archive.zip")
    filled_data = handle_missing_values_step(raw_data)
    engineered_data = feature_engineering_step(
        filled_data, strategy="log", features=["Gr Liv Area", "SalePrice"]
    )
    clean_data = outlier_detection_step(engineered_data, column_name="SalePrice")
    X_train, X_test, y_train, y_test = data_splitter_step(clean_data, target_column="SalePrice")
    model_pipeline_artifact = model_building_step(X_train=X_train, y_train=y_train)
    evaluation_metrics, mse = model_evaluator_step(
        trained_model=model_pipeline_artifact, X_test=X_test, y_test=y_test
    )
    return model_pipeline_artifact, evaluation_metrics
```

## 2. ZenML Steps Overview

Each function decorated with `@step` in the `steps/` directory represents a distinct stage in the pipeline. ZenML manages the execution order and data passing between these steps.
(For the raw Mermaid code, see [diagrams/03_ml_pipeline_details_diagram.md](./diagrams/03_ml_pipeline_details_diagram.md))

[![ML Pipeline Details Diagram](./diagrams/03_ml_pipeline_details_diagram.md)](./diagrams/03_ml_pipeline_details_diagram.md)
<!-- Note: GitHub might not render Mermaid from a relative link like this directly in an image tag. -->

**Key Steps & Their Roles:**

1.  **`data_ingestion_step`**:
    *   **Responsibility**: Loads raw data from `data/archive.zip`.
    *   **Output**: Pandas DataFrame of raw data.

2.  **`handle_missing_values_step`**:
    *   **Responsibility**: Imputes missing values in the DataFrame.
    *   **Output**: DataFrame with missing values handled.

3.  **`feature_engineering_step`**:
    *   **Responsibility**: Applies transformations. Critically, it applies `np.log1p` to `Gr Liv Area` and `SalePrice`.
    *   **Output**: DataFrame with engineered features.

4.  **`outlier_detection_step`**:
    *   **Responsibility**: Identifies and removes outliers, particularly based on `SalePrice`.
    *   **Output**: Cleaned DataFrame.

5.  **`data_splitter_step`**:
    *   **Responsibility**: Splits data into training (`X_train`, `y_train`) and testing (`X_test`, `y_test`) sets.
    *   **Output**: Four DataFrames/Series: `X_train`, `X_test`, `y_train`, `y_test`.

6.  **`model_building_step`**:
    *   **Responsibility**:
        *   Defines a scikit-learn `Pipeline` that includes:
            *   A `ColumnTransformer` for numerical imputation and categorical one-hot encoding.
            *   A `LinearRegression` model.
        *   Trains this scikit-learn `Pipeline` on `X_train` and `y_train` (where `y_train` is log1p-transformed `SalePrice`).
        *   Uses `mlflow.sklearn.autolog()` to automatically log parameters, metrics (initial training metrics), and the *entire scikit-learn pipeline object* to MLflow.
    *   **Output**: The trained scikit-learn `Pipeline` object (annotated as `is_model_artifact=True`).
    *   **MLflow Interaction**: This step is crucial for logging the model. The `autolog()` feature captures the scikit-learn pipeline, making it available for later use via MLflow.

7.  **`model_evaluator_step`**:
    *   **Responsibility**: Evaluates the trained model pipeline on the test set (`X_test`, `y_test`).
    *   Calculates metrics like Mean Squared Error (MSE) and R-Squared.
    *   **MLflow Interaction**: Logs these evaluation metrics to the active MLflow run.
    *   **Output**: Evaluation metrics dictionary and MSE.

## 3. MLflow Integration Details

*   **Experiment Tracker**: The ZenML stack is configured with `mlflow_tracker`. When a ZenML pipeline runs, ZenML ensures that MLflow is set up to track it.
*   **Experiment Naming**:
    *   The `run_pipeline.py` script implicitly creates or uses an MLflow experiment named `ml_pipeline` (this is the default behavior of `mlflow.start_run()` if an experiment isn't explicitly set by ZenML's higher-level model versioning, or if `mlflow.set_experiment()` is called).
    *   The `@pipeline` decorator's `model=Model(name="prices_predictor")` argument in ZenML primarily relates to ZenML's own Model Control Plane for versioning and lineage, which then links to the MLflow artifacts.
*   **Artifact Logging**:
    *   **Model**: The `model_building_step` uses `mlflow.sklearn.autolog()`, which logs the scikit-learn `Pipeline` object. This object includes the preprocessor (for imputation, OHE) and the linear regression model. **Crucially, the `LogTransformation` of `Gr Liv Area` and `SalePrice` done in `feature_engineering_step` is *not* part of this logged scikit-learn pipeline object.**
    *   **Metrics**: Both `autolog()` in `model_building_step` and explicit logging in `model_evaluator_step` contribute metrics to the MLflow run.
    *   **Parameters**: `autolog()` captures hyperparameters of the scikit-learn pipeline.
*   **Accessing Runs**: The MLflow UI (started with `mlflow ui --backend-store-uri ...`) is used to view all this tracked information. The correct `--backend-store-uri` points to the ZenML artifact store's MLflow directory.

## 4. Important Considerations for Prediction

*   Because the `LogTransformation` of input features like `Gr Liv Area` happens *before* the `model_building_step` (where the scikit-learn pipeline is defined and logged), any prediction script or UI (`sample_predict.py`, `ui/app.py`) must manually apply this same `np.log1p` transformation to the raw `Gr Liv Area` input *before* passing data to the loaded MLflow model's `.predict()` method.
*   Similarly, since the target variable `SalePrice` was `log1p` transformed before training, the model predicts on this log scale. The prediction script/UI must manually apply `np.expm1()` to the model's output to get the price back on the original dollar scale.

This separation of an initial feature transformation step from the main scikit-learn preprocessing pipeline logged by MLflow is a key architectural detail to manage for consistent predictions.

---

Next: [04_prediction_services.md](./04_prediction_services.md) (How predictions are made available)
