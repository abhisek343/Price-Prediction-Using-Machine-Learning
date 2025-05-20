# System Design: Architecture Overview 🏗️

This document provides a high-level overview of the Prices Predictor System's architecture, outlining its major components and how they interact to deliver an end-to-end MLOps solution.

## 1. Core Philosophy

The system is designed with modularity, reproducibility, and ease of use in mind. It leverages industry-standard tools like ZenML for MLOps orchestration and MLflow for experiment tracking and model management, combined with a custom Flask UI for interactive predictions.

## 2. Major Components

The system can be broken down into the following key components:

*   **Data Layer**: Handles raw data storage, ingestion, and provides access to processed data.
*   **ZenML MLOps Pipelines**: The backbone for orchestrating all machine learning operations. This includes:
    *   Data Ingestion & Validation
    *   Data Preprocessing & Feature Engineering
    *   Model Training & Evaluation
    *   (Conceptual) Model Deployment
*   **MLflow Integration**: Used for:
    *   Tracking experiments, runs, parameters, and metrics.
    *   Logging and versioning trained models and artifacts.
    *   Serving models (conceptually, via the deployment pipeline).
*   **Prediction Services**:
    *   **Local Prediction Script (`sample_predict.py`)**: For quick, local model inference.
    *   **Flask Web UI (`ui/app.py`)**: Provides an interactive interface for users to input features and receive price predictions.
*   **Execution & Orchestration Scripts**:
    *   `run_project.ps1` / `run_project.sh`: Master scripts to automate setup and the main workflow.
    *   Individual Python scripts (`run_pipeline.py`, `run_deployment.py`) for manual pipeline execution.

## 3. High-Level Interaction Diagram

The following diagram illustrates the general flow and interaction between components. 
(For the raw Mermaid code, see [diagrams/01_architecture_overview_diagram.md](./diagrams/01_architecture_overview_diagram.md))

[![Architecture Overview Diagram](./diagrams/01_architecture_overview_diagram.md)](./diagrams/01_architecture_overview_diagram.md) 
<!-- Note: GitHub might not render Mermaid from a relative link like this directly in an image tag. 
     For best viewing, users might need to open the .md file containing the diagram or use a browser extension. 
     Alternatively, one could paste the Mermaid code here directly if preferred for immediate rendering in some Markdown viewers. -->

**Diagram Explanation:**

1.  **Raw Data**: The process starts with the raw housing data.
2.  **ZenML MLOps Pipeline**:
    *   **Data Ingestion**: Loads and initially processes the data.
    *   **Preprocessing & Feature Engineering**: Cleans the data, handles missing values, creates new features, and transforms existing ones (e.g., log transformation).
    *   **Model Training & Evaluation**: Trains a regression model on the processed data and evaluates its performance.
3.  **MLflow Tracking Server**: All pipeline runs, parameters, metrics, and model artifacts (including the trained scikit-learn pipeline) are logged to MLflow. This serves as the central model registry and experiment database.
4.  **Prediction Services**:
    *   **Flask Web UI**: Loads the latest trained model from MLflow. Users interact via a web browser, inputting features. The Flask app processes this input, sends it to the model, and displays the prediction.
    *   **Local Prediction Script**: Similar to the Flask UI, it loads the model from MLflow and predicts on a sample data point, useful for quick tests.
5.  **ZenML CLI / Scripts**: Users interact with ZenML via CLI commands (e.g., `zenml stack set ...`) or by running Python scripts (`run_pipeline.py`, `run_project.ps1/sh`) that trigger ZenML pipeline executions.

## 4. Key Architectural Decisions

*   **Pipeline-first approach with ZenML**: Ensures reproducibility and automates the ML workflow.
*   **Decoupled Model Logging with MLflow**: Allows models to be tracked and versioned independently, and loaded by various services.
*   **Multiple Prediction Interfaces**: Catering to different user needs (programmatic script vs. interactive UI).
*   **Local-first Development**: The system is designed to be fully runnable and testable on a local machine, with clear paths for future scaling or cloud deployment (e.g., by changing ZenML stack components).

---

Next: [02_data_flow.md](./02_data_flow.md) (Details on data processing)
