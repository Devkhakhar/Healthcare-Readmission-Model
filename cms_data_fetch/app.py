from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('readmission_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract features from form submission
    features = [float(request.form['excess_readmission_ratio']),
                float(request.form['predicted_readmission_rate']),
                float(request.form['expected_readmission_rate'])]
    
    # Predict readmission
    prediction = model.predict([features])[0]
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
