import os
import mlflow
import pandas as pd
import numpy as np
from flask import Flask, request, render_template

# Initialize Flask app
# Correctly locate the template folder
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)

# Global variable to cache the loaded model
loaded_model = None

def get_model():
    """Loads the MLflow model if not already loaded."""
    global loaded_model
    if loaded_model is None:
        try:
            # Use the tracking URI provided by ZenML's MLflow integration output
            # Ensure this path is correct for your environment
            mlflow.set_tracking_uri(r"file:C:\Users\babhi\AppData\Roaming\zenml\local_stores\b8276e3d-26f6-4f13-afb4-43b15f763144\mlruns")
            experiment_name = "ml_pipeline" 
            
            client = mlflow.tracking.MlflowClient()
            experiment = client.get_experiment_by_name(experiment_name)
            if not experiment:
                raise Exception(f"Experiment '{experiment_name}' not found.")

            runs = client.search_runs(
                experiment_ids=[experiment.experiment_id],
                order_by=["start_time DESC"],
                max_results=1
            )
            if not runs:
                raise Exception(f"No runs found in experiment '{experiment_name}'.")

            latest_run = runs[0]
            run_id = latest_run.info.run_id
            model_uri = f"runs:/{run_id}/model"
            
            print(f"Loading model from experiment '{experiment_name}', run_id '{run_id}', URI '{model_uri}'...")
            loaded_model = mlflow.pyfunc.load_model(model_uri)
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise # Reraise to be caught by the route
    return loaded_model

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction_result = None
    error_message = None

    if request.method == 'POST':
        try:
            model = get_model()
            if model is None:
                raise Exception("Model could not be loaded.")

            # Start with a default full feature set (like sample_predict.py)
            # This ensures all columns expected by the model are present.
            # Values will be overridden by form input.
            # Important: Ensure data types match what the model expects after schema inference.
            data = {
                "Order": 1, "PID": 5286, "MS SubClass": 20, "Lot Frontage": 80.0, "Lot Area": 9600,
                "Overall Qual": 7, "Overall Cond": 5, "Year Built": 2005, "Year Remod/Add": 2005,
                "Mas Vnr Area": 0.0, "BsmtFin SF 1": 700.0, "BsmtFin SF 2": 0.0, "Bsmt Unf SF": 150.0,
                "Total Bsmt SF": 850.0, "1st Flr SF": 856, "2nd Flr SF": 0, "Low Qual Fin SF": 0, # Default 2nd Flr SF to 0 if not a 2-story house by default
                "Gr Liv Area": 1710.0, "Bsmt Full Bath": 1.0, "Bsmt Half Bath": 0.0, "Full Bath": 2,
                "Half Bath": 0, "Bedroom AbvGr": 3, "Kitchen AbvGr": 1, "TotRms AbvGrd": 7,
                "Fireplaces": 1, "Garage Yr Blt": 2005.0, "Garage Cars": 2.0, "Garage Area": 500.0,
                "Wood Deck SF": 210, "Open Porch SF": 60, "Enclosed Porch": 0, "3Ssn Porch": 0,
                "Screen Porch": 0, "Pool Area": 0, "Misc Val": 0, "Mo Sold": 5, "Yr Sold": 2010,
            }

            # Update with form data, converting to appropriate types
            # These are the fields from the form
            data["Overall Qual"] = int(request.form['OverallQual'])
            data["Gr Liv Area"] = float(request.form['GrLivArea']) # Will be log1p transformed
            data["Year Built"] = int(request.form['YearBuilt'])
            data["Total Bsmt SF"] = float(request.form['TotalBsmtSF'])
            data["Full Bath"] = int(request.form['FullBath'])
            data["Garage Cars"] = float(request.form['GarageCars']) # Schema expects double

            # Manually ensure other fields that model schema expects as float are float
            # (even if their default whole number might make pandas infer int)
            float_fields_from_schema = ["Lot Frontage", "Mas Vnr Area", "BsmtFin SF 1", "BsmtFin SF 2", 
                                        "Bsmt Unf SF", "Total Bsmt SF", "Gr Liv Area", "Bsmt Full Bath", 
                                        "Bsmt Half Bath", "Garage Yr Blt", "Garage Cars", "Garage Area"]
            for field in float_fields_from_schema:
                if field in data:
                    data[field] = float(data[field])
            
            # Ensure integer fields are int
            int_fields_from_schema = ["Order", "PID", "MS SubClass", "Lot Area", "Overall Qual", "Overall Cond", 
                                      "Year Built", "Year Remod/Add", "1st Flr SF", "2nd Flr SF", "Low Qual Fin SF", 
                                      "Full Bath", "Half Bath", "Bedroom AbvGr", "Kitchen AbvGr", "TotRms AbvGrd", 
                                      "Fireplaces", "Wood Deck SF", "Open Porch SF", "Enclosed Porch", 
                                      "3Ssn Porch", "Screen Porch", "Pool Area", "Misc Val", "Mo Sold", "Yr Sold"]
            for field in int_fields_from_schema:
                 if field in data:
                    data[field] = int(data[field])


            input_df = pd.DataFrame([data])
            
            # Apply log transformation to 'Gr Liv Area' as done during training
            if 'Gr Liv Area' in input_df.columns:
                input_df['Gr Liv Area'] = np.log1p(input_df['Gr Liv Area'])
            
            raw_prediction = model.predict(input_df)
            prediction_result = np.expm1(raw_prediction[0])

        except Exception as e:
            error_message = str(e)
            print(f"Error during prediction: {e}")

    return render_template('index.html', prediction=prediction_result, error=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5001) # Run on a different port than MLflow UI
