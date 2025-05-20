import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(df: pd.DataFrame, test_size: float = 0.2, random_state: int = 42):
    """
    Splits data into training and testing sets.

    Args:
        df: Input pandas DataFrame.
        test_size: Proportion of the dataset to include in the test split.
        random_state: Seed for random number generation.

    Returns:
        A tuple containing the training and testing DataFrames.
    """
    try:
        train_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state)
        return train_df, test_df
    except Exception as e:
        print(f"Error splitting data: {e}")
        return None, None

if __name__ == "__main__":
    # Example usage (will be updated later)
    pass
