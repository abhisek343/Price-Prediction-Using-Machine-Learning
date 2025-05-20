import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(model: LinearRegression, test_df: pd.DataFrame):
    """
    Evaluates the trained model (placeholder).

    Args:
        model: Trained LinearRegression model.
        test_df: Testing pandas DataFrame.

    Returns:
        A dictionary containing evaluation metrics.
    """
    try:
        X_test = test_df.iloc[:, :-1]
        y_test = test_df.iloc[:, -1]
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        return {"mse": mse, "r2": r2}
    except Exception as e:
        print(f"Error evaluating model: {e}")
        return None

if __name__ == "__main__":
    # Example usage (will be updated later)
    pass
