from flask import Flask, render_template, request, jsonify
import pandas as pd
# Assuming Predictor is available
# from steps.predictor import Predictor

app = Flask(__name__)

# Dummy predictor for now
class DummyPredictor:
    def predict(self, data):
        print("Making dummy predictions in Flask app...")
        # Dummy prediction logic
        return [float(i) * 10 for i in range(len(data))] # Dummy predictions

predictor = DummyPredictor() # Replace with actual predictor loading

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # Assuming data is a list of dictionaries, convert to DataFrame
        input_df = pd.DataFrame(data)
        predictions = predictor.predict(input_df)
        return jsonify(predictions.tolist())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Example usage (will be updated later)
    # app.run(debug=True)
    pass
