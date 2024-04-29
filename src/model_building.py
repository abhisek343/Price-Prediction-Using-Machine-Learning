import pandas as pd
from sklearn.linear_model import LinearRegression

def build_model(train_df: pd.DataFrame):
    """
    Builds a simple linear regression model (placeholder).

    Args:
        train_df: Training pandas DataFrame.

    Returns:
        A trained LinearRegression model.
    """
    try:
        # Assuming the last column is the target variable
        X_train = train_df.iloc[:, :-1]
        y_train = train_df.iloc[:, -1]
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        print(f"Error building model: {e}")
        return None

if __name__ == "__main__":
    # Example usage (will be updated later)
    pass
