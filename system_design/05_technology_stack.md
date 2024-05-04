# System Design: Technology Stack 🛠️💻🐍

This document outlines the key technologies, libraries, and frameworks used in the Prices Predictor System, along with their roles.

## 1. Core Language & Environment

*   **Python 3.x**:
    *   **Role**: The primary programming language for the entire project, including data processing, machine learning model development, pipeline orchestration, and the web UI.
    *   **Reason**: Rich ecosystem of libraries for data science and web development, ease of use, and strong community support.

*   **Virtual Environment (`venv`)**:
    *   **Role**: Manages project-specific dependencies, ensuring isolation from other Python projects and system-wide packages.
    *   **Reason**: Best practice for Python development to avoid conflicts and ensure reproducibility.

## 2. MLOps & Experiment Tracking

*   **ZenML**:
    *   **Role**: Orchestrates the end-to-end machine learning pipelines (training, deployment). Defines steps, manages data flow between steps, and integrates various MLOps tools.
    *   **Reason**: Provides a structured way to build reproducible and production-ready ML pipelines, abstracting away much of the underlying infrastructure complexity.

*   **MLflow**:
    *   **Role**:
        *   **Experiment Tracking**: Logs parameters, metrics, code versions, and artifacts for each pipeline run.
        *   **Model Registry (Conceptual)**: Stores and versions trained models.
        *   **Model Serving**: Provides capabilities to deploy models as REST APIs (used conceptually in the deployment pipeline).
        *   **MLflow UI**: A web interface to browse and compare experiment runs and model artifacts.
    *   **Reason**: Industry-standard tool for managing the ML lifecycle, offering excellent tracking and model management features.

## 3. Data Science & Machine Learning

*   **Pandas**:
    *   **Role**: Primary tool for data manipulation and analysis. Used for loading data, cleaning, transformation, and structuring data in DataFrames.
    *   **Reason**: Powerful, flexible, and widely adopted for tabular data in Python.

*   **NumPy**:
    *   **Role**: Fundamental package for numerical computation in Python. Used for array operations, mathematical functions (like `np.log1p`, `np.expm1`), and as an underlying library for Pandas and Scikit-learn.
    *   **Reason**: Essential for efficient numerical operations.

*   **Scikit-learn**:
    *   **Role**:
        *   **Preprocessing**: Provides tools for data imputation (`SimpleImputer`), scaling, and encoding (`OneHotEncoder`).
        *   **Model Building**: Used for creating the `LinearRegression` model.
        *   **Pipelines**: Its `Pipeline` and `ColumnTransformer` objects are used to chain preprocessing steps with the model, ensuring consistent transformations during training and prediction.
        *   **Evaluation**: Provides metrics for model evaluation.
    *   **Reason**: Comprehensive, easy-to-use, and robust library for classical machine learning tasks.

*   **Matplotlib & Seaborn**:
    *   **Role**: Used for data visualization, primarily within the Exploratory Data Analysis (EDA) phase (e.g., in `analysis/EDA.ipynb`).
    *   **Reason**: Standard Python libraries for creating static, animated, and interactive visualizations.

*   **Statsmodels**:
    *   **Role**: Provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests and statistical data exploration. (Included in `requirements.txt`, usage might be in EDA or deeper statistical analysis parts of the original project).
    *   **Reason**: Useful for more in-depth statistical modeling and analysis beyond basic ML.

## 4. Web User Interface

*   **Flask**:
    *   **Role**: A lightweight WSGI web application framework used to build the simple, interactive web UI (`ui/app.py`) for making predictions.
    *   **Reason**: Simple to get started with, flexible, and well-suited for small to medium-sized web applications or APIs.

*   **HTML/CSS/JavaScript (implied for Flask templates)**:
    *   **Role**: Standard web technologies used to structure (`index.html`), style, and potentially add client-side interactivity to the web UI served by Flask.
    *   **Reason**: Universal standards for web front-end development.

## 5. Command-Line Interface

*   **Click**:
    *   **Role**: Used to create user-friendly command-line interfaces for scripts like `run_deployment.py` and `run_pipeline.py`.
    *   **Reason**: Simplifies the creation of CLIs with options, arguments, and help messages.

## 6. Database (Conceptual/Optional)

*   **SQLAlchemy & `psycopg2-binary`**:
    *   **Role**: These are listed in `requirements.txt`. SQLAlchemy is an SQL toolkit and Object Relational Mapper (ORM), and `psycopg2` is a PostgreSQL adapter. Their inclusion suggests potential for database interaction (e.g., storing metadata, results, or as a backend for ZenML/MLflow components in a more advanced setup).
    *   **Current Use**: In the current local setup, ZenML and MLflow use file-based backends by default. These libraries would be more relevant if scaling to a server-based setup with a PostgreSQL database.
    *   **Reason**: Standard tools for database interaction in Python.

This stack provides a comprehensive toolkit for developing, training, tracking, and interacting with the machine learning model in this project.
