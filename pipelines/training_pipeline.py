import pandas as pd
from src.ingest_data import ingest_data
from src.handle_missing_values import handle_missing_values
from src.feature_engineering import feature_engineer
from src.data_splitter import split_data
from src.model_building import build_model
from src.model_evaluator import evaluate_model

def train_pipeline(data_path: str):
    """
    Basic training pipeline (placeholder).

    Args:
        data_path: Path to the raw data file.
    """
    print("Starting training pipeline...")

    # 1. Ingest data
    df = ingest_data(data_path)
    if df is None:
        print("Data ingestion failed. Exiting.")
        return

    print("Data ingested successfully.")

    # 2. Handle missing values
    df = handle_missing_values(df)
    print("Missing values handled.")

    # 3. Feature engineering
    df = feature_engineer(df)
    print("Feature engineering completed.")

    # 4. Split data
    train_df, test_df = split_data(df)
    if train_df is None or test_df is None:
        print("Data splitting failed. Exiting.")
        return

    print("Data split into training and testing sets.")

    # 5. Build model
    model = build_model(train_df)
    if model is None:
        print("Model building failed. Exiting.")
        return

    print("Model built successfully.")

    # 6. Evaluate model
    metrics = evaluate_model(model, test_df)
    if metrics is None:
        print("Model evaluation failed. Exiting.")
        return

    print(f"Model evaluated. Metrics: {metrics}")

    print("Training pipeline finished.")

if __name__ == "__main__":
    # Example usage (will be updated later)
    pass
