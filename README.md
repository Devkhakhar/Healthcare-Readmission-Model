# Hospital_Readmission_Predictor
This project is a web-based application that predicts the likelihood of a patient being readmitted to the hospital based on specific health metrics. The prediction model is built using Logistic Regression, trained on a dataset of hospital readmissions, and deployed via a Flask web application.

## Features

- **User Input Form:** Users can input values for `Excess Readmission Ratio`, `Predicted Readmission Rate`, and `Expected Readmission Rate`.
- **Prediction Output:** The application predicts whether a patient is likely to be readmitted to the hospital or not.
- **Real-Time Feedback:** The prediction is displayed instantly after the user submits the form.
- **Responsive Design:** The web application is styled with CSS to be user-friendly and accessible on different devices.

## How It Works

The prediction is made using a Logistic Regression model trained on historical hospital readmission data. The model evaluates the input features and returns a binary prediction indicating whether a readmission is likely (`1`) or unlikely (`0`).

### Input Fields

- **Excess Readmission Ratio:** A ratio that indicates how much higher the readmission rate is compared to an expected standard. Values greater than 1 indicate higher risk.
- **Predicted Readmission Rate:** The predicted percentage of patients expected to be readmitted.
- **Expected Readmission Rate:** The expected percentage of readmissions based on historical data.

### Example Inputs and Outputs

- **Example 1:**
  - **Input:** `Excess Readmission Ratio = 1.20`, `Predicted Readmission Rate = 25.00`, `Expected Readmission Rate = 22.00`
  - **Output:** Readmission Likely
  
- **Example 2:**
  - **Input:** `Excess Readmission Ratio = 0.85`, `Predicted Readmission Rate = 10.00`, `Expected Readmission Rate = 12.00`
  - **Output:** Readmission Unlikely

## Project Structure
Readmission_predictor_Project/
├── cms_data_fetch/
│ ├── app.py # Flask application
│ ├── train_model.py # Script to train the model
│ ├── readmission_model.pkl # Trained model file
│ ├── processed_hospital_readmissions_data.csv # Dataset used for training
│ ├── visualization.py # Data visualization script
│ └── templates/
│ └── index.html # HTML template for the web app
│ └── static/
│ └── style.css # CSS styling for the web app
├── README.md # This file
└── requirements.txt # Python dependencies

## Installation and Setup

To run this application locally, follow these steps:

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation Steps

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/Readmission_predictor_Project.git
    cd Readmission_predictor_Project/cms_data_fetch/
    ```

2. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**
    ```bash
    python app.py
    ```

5. **Access the application:**
    - Open your web browser and navigate to `http://127.0.0.1:5000`

## Dependencies

The project requires the following Python packages, which are listed in the `requirements.txt` file:

- Flask==3.0.0
- pandas==1.4.4
- scikit-learn==1.0.2
- joblib==1.3.2

Install them using:
```bash
pip install -r requirements.txt
Future Improvements

Model Enhancement: Experiment with more complex models (e.g., Random Forest, XGBoost) to improve prediction accuracy.
User Authentication: Add user authentication to allow users to save and view past predictions.
Deployment: Deploy the application on a cloud platform like Heroku, AWS, or Azure for public access.
License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

Thanks to the Centers for Medicare & Medicaid Services (CMS) for providing the dataset used in this project.


