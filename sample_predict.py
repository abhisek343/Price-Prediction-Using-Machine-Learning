import mlflow
import pandas as pd
import numpy as np

# Sample input data for prediction
sample_data_dict = {
    "Order": 1, "PID": 5286, "MS SubClass": 20, "Lot Frontage": 80.0, "Lot Area": 9600,
    "Overall Qual": 5, "Overall Cond": 7, "Year Built": 1961, "Year Remod/Add": 1961,
    "Mas Vnr Area": 0.0, "BsmtFin SF 1": 700.0, "BsmtFin SF 2": 0.0, "Bsmt Unf SF": 150.0,
    "Total Bsmt SF": 850.0, "1st Flr SF": 856, "2nd Flr SF": 854, "Low Qual Fin SF": 0,
    "Gr Liv Area": 1710.0, "Bsmt Full Bath": 1.0, "Bsmt Half Bath": 0.0, "Full Bath": 1,
    "Half Bath": 0, "Bedroom AbvGr": 3, "Kitchen AbvGr": 1, "TotRms AbvGrd": 7,
    "Fireplaces": 2, "Garage Yr Blt": 1961.0, "Garage Cars": 2.0, "Garage Area": 500.0,
    "Wood Deck SF": 210, "Open Porch SF": 0, "Enclosed Porch": 0, "3Ssn Porch": 0,
    "Screen Porch": 0, "Pool Area": 0, "Misc Val": 0, "Mo Sold": 5, "Yr Sold": 2010,
}
input_df_original = pd.DataFrame([sample_data_dict])

def predict_locally_from_run():
    """Loads the latest model from the 'ml_pipeline' experiment run and predicts."""
    try:
        # Create a copy for modification
        input_df = input_df_original.copy()

        # Apply the same log transformation to 'Gr Liv Area' as done during training
        if 'Gr Liv Area' in input_df.columns:
            print(f"Original 'Gr Liv Area': {input_df['Gr Liv Area'].iloc[0]}")
            input_df['Gr Liv Area'] = np.log1p(input_df['Gr Liv Area'])
            print(f"Log-transformed 'Gr Liv Area': {input_df['Gr Liv Area'].iloc[0]}")
        
        # Use the tracking URI provided by ZenML's MLflow integration output
        mlflow.set_tracking_uri(r"file:C:\Users\babhi\AppData\Roaming\zenml\local_stores\b8276e3d-26f6-4f13-afb4-43b15f763144\mlruns")
        experiment_name = "ml_pipeline" # Experiment name from run_pipeline.py output
        
        client = mlflow.tracking.MlflowClient()
        experiment = client.get_experiment_by_name(experiment_name)
        if not experiment:
            print(f"Experiment '{experiment_name}' not found.")
            return

        # Get all runs for the experiment, order by start time descending to get the latest
        runs = client.search_runs(
            experiment_ids=[experiment.experiment_id],
            order_by=["start_time DESC"],
            max_results=1
        )
        
        if not runs:
            print(f"No runs found in experiment '{experiment_name}'.")
            print("Please run 'python run_pipeline.py' first to train a model.")
            return

        latest_run = runs[0]
        run_id = latest_run.info.run_id
        # The model is typically logged as an artifact named 'model' within the run
        model_uri = f"runs:/{run_id}/model" 
        
        print(f"Loading model from experiment '{experiment_name}', run_id '{run_id}', URI '{model_uri}'...")
        loaded_model = mlflow.pyfunc.load_model(model_uri)
        print("Model loaded successfully.")

        print("\nInput DataFrame for prediction (after Gr Liv Area transformation):")
        print(input_df)
        
        prediction = loaded_model.predict(input_df)
        
        # The feature_engineering_step used np.log1p for SalePrice, so inverse is np.expm1
        actual_prediction = np.expm1(prediction)

        print(f"\nRaw Prediction (log1p scale): {prediction[0]}")
        print(f"Predicted Sale Price (after inverse transformation): {actual_prediction[0]}")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Ensure 'run_pipeline.py' has been run successfully to train and log a model.")

if __name__ == "__main__":
    predict_locally_from_run()
