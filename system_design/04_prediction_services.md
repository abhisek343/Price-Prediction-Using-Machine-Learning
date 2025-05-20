# System Design: Prediction Services & UI 🔮💻

This document outlines how users can obtain predictions from the trained Prices Predictor model, covering both programmatic access and the interactive web UI.

## 1. Core Prediction Logic

Regardless of the interface, the core prediction process involves these key steps after a model has been trained and logged by the `ml_pipeline`:

1.  **Model Loading**: The latest version of the `prices_predictor` model is loaded from the MLflow Tracking Server. This is typically done by referencing the model's run artifact URI (e.g., `runs:/<RUN_ID>/model`). The loaded object is an MLflow `pyfunc` model, which wraps the original scikit-learn `Pipeline`.
2.  **Input Data Preparation**:
    *   Raw input features are received (either from a script or a web form).
    *   **Crucial Preprocessing**: The `Gr Liv Area` feature must be manually transformed using `np.log1p()` to match the transformation applied during the `feature_engineering_step` of the training pipeline. This is because this specific transformation is *not* part of the scikit-learn pipeline object logged by MLflow.
    *   Data types of input features are ensured to match the schema expected by the MLflow model (e.g., converting certain integers to floats).
    *   The prepared features are structured into a Pandas DataFrame.
3.  **Prediction**: The `predict()` method of the loaded MLflow `pyfunc` model is called with the prepared input DataFrame. The model's internal scikit-learn pipeline handles further preprocessing (imputation, one-hot encoding) defined within its `ColumnTransformer`. The output is a prediction on the `log1p` scale (as `SalePrice` was transformed).
4.  **Output Postprocessing**: The `log1p`-scaled prediction is inverse-transformed using `np.expm1()` to convert it back to the actual predicted sale price in dollars.

## 2. Prediction Interfaces

### A. Local Prediction Script (`sample_predict.py`)

*   **Purpose**: Provides a simple command-line interface for developers to quickly test the latest trained model with a predefined sample input.
*   **Workflow**:
    1.  Sets the MLflow tracking URI to the ZenML local store.
    2.  Queries MLflow for the latest run of the `ml_pipeline` experiment.
    3.  Constructs the model artifact URI and loads the `pyfunc` model.
    4.  Prepares a hardcoded sample data dictionary, applies `np.log1p` to `Gr Liv Area`, and converts it to a DataFrame.
    5.  Calls `model.predict()`.
    6.  Applies `np.expm1()` to the result.
    7.  Prints the input, raw prediction, and final predicted price.
*   **Diagram**: 
        (For the raw Mermaid code, see [diagrams/04a_local_prediction_script_diagram.md](./diagrams/04a_local_prediction_script_diagram.md))

        [![Local Prediction Script Diagram](./diagrams/04a_local_prediction_script_diagram.md)](./diagrams/04a_local_prediction_script_diagram.md)
        <!-- Note: GitHub might not render Mermaid from a relative link like this directly in an image tag. -->

### B. Flask Web UI (`ui/app.py`)

*   **Purpose**: Offers an interactive web interface for users to input house features and receive predictions.
*   **Workflow**:
    1.  **Initialization**:
        *   A Flask web server is started (`python ui/app.py`).
        *   The `get_model()` function attempts to load the latest MLflow model on startup (or first request) and caches it globally. This uses the same MLflow interaction logic as `sample_predict.py`.
    2.  **User Interaction (GET Request)**:
        *   User navigates to `http://127.0.0.1:5001`.
        *   Flask renders `ui/templates/index.html`, displaying an input form.
    3.  **User Interaction (POST Request)**:
        *   User fills in the form (subset of features) and submits.
        *   Flask route receives the form data.
        *   A default dictionary containing all 38 features (with sensible defaults) is created.
        *   Values from the web form override the defaults for the submitted features.
        *   Data types are explicitly cast to match the model's schema (e.g., `int(request.form['OverallQual'])`, `float(request.form['GarageCars'])`).
        *   `np.log1p` is applied to `Gr Liv Area`.
        *   The data is converted to a Pandas DataFrame.
        *   The cached model's `predict()` method is called.
        *   `np.expm1()` is applied to the prediction.
        *   The `index.html` template is re-rendered, displaying the predicted price (or an error message).
*   **Diagram**:
        (For the raw Mermaid code, see [diagrams/04b_flask_ui_workflow_diagram.md](./diagrams/04b_flask_ui_workflow_diagram.md))

        [![Flask UI Workflow Diagram](./diagrams/04b_flask_ui_workflow_diagram.md)](./diagrams/04b_flask_ui_workflow_diagram.md)
        <!-- Note: GitHub might not render Mermaid from a relative link like this directly in an image tag. -->

## 3. (Conceptual) MLflow Deployment Service

*   The `run_deployment.py` script attempts to use ZenML's `MLFlowModelDeployer` to start an MLflow model serving endpoint.
*   If successful and the service were persistently running, `sample_predict.py` (in its original form) or other HTTP clients could send JSON payloads to an `/invocations` endpoint (e.g., `http://127.0.0.1:8000/invocations`).
*   **Current Status**: Due to limitations with daemonizing local services on Windows via ZenML's current local MLflow deployer, this method is less reliable for immediate local use compared to direct model loading. The primary prediction interfaces are therefore the local script and the Flask UI which load the model directly.

This multi-faceted approach to prediction allows for both development-time testing and user-friendly interaction with the trained model.
