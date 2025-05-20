import pandas as pd

def ingest_data(data_path: str) -> pd.DataFrame:
    """
    Ingests data from a specified path.

    Args:
        data_path: Path to the data file.

    Returns:
        A pandas DataFrame containing the ingested data.
    """
    try:
        df = pd.read_csv(data_path)
        return df
    except Exception as e:
        print(f"Error ingesting data from {data_path}: {e}")
        return None

if __name__ == "__main__":
    # Example usage (will be updated later)
    pass
