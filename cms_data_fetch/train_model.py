import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Step 1: Load the Processed Data
print("Loading the processed data...")
df = pd.read_csv('processed_hospital_readmissions_data.csv')

# Step 2: Convert 'Number of Readmissions' to numeric, coercing errors, and then to binary
df['Number of Readmissions'] = pd.to_numeric(df['Number of Readmissions'], errors='coerce')

# Handle NaN values by assuming no readmission (0) for non-numeric cases
df['Readmitted'] = df['Number of Readmissions'].apply(lambda x: 1 if pd.notnull(x) and x > 0 else 0)

# Step 3: Select relevant features for modeling
features = df[['Excess Readmission Ratio', 'Predicted Readmission Rate', 'Expected Readmission Rate']]
target = df['Readmitted']

# Display the first few rows to ensure everything is correct
print("Features and Target Variables:")
print(features.head())
print(target.head())

# Step 4: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Step 5: Initialize and train the model
print("Training the Logistic Regression model...")
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(report)

# Step 8: Save the trained model to a file
joblib.dump(model, 'readmission_model.pkl')
print("Trained model saved as 'readmission_model.pkl'")
