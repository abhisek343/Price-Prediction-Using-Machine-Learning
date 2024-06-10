# Data Flow

This document describes the flow of data through the Prices Predictor System.

1.  **Data Ingestion:** Raw data is read from the source (e.g., CSV file).
2.  **Data Preprocessing:** The ingested data undergoes cleaning (handling missing values) and feature engineering.
3.  **Data Splitting:** The processed data is split into training and testing datasets.
4.  **Model Training:** The training data is used to train the machine learning model.
5.  **Model Evaluation:** The trained model is evaluated using the testing data.
6.  **Model Deployment:** The trained model is prepared for serving predictions.
7.  **Prediction Service:** The deployed model is exposed as a service.
8.  **User Interface:** The UI sends requests to the prediction service with new data and displays the predictions.
