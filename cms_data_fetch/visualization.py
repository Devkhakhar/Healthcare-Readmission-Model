import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_preview_data():
    print("Step 1: Loading dataset...")
    
    # Load the dataset
    df = pd.read_csv('hospital_readmissions_data.csv')
    print("Step 1 Completed: Dataset loaded.")
    
    # Preview the first few rows
    print("First few rows of the dataset:")
    print(df.head())

    # Basic summary statistics
    print("\nSummary statistics:")
    print(df.describe())

    # Check for missing values
    print("\nMissing values in each column:")
    print(df.isnull().sum())
    
    # Handle missing values
    print("Handling missing values...")
    df.fillna(df.median(), inplace=True)  # Fill missing numeric values with the median
    df.fillna('Unknown', inplace=True)    # Fill missing categorical values with 'Unknown'
    print("Missing values handled.")
    
    # Save the processed data
    df.to_csv('processed_hospital_readmissions_data.csv', index=False)
    print("Processed data saved to 'processed_hospital_readmissions_data.csv'")
    
    return df

def visualize_data(df):
    print("Step 2: Visualizing data...")
    
    # Visualize the distribution of Excess Readmission Ratio
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Excess Readmission Ratio'].dropna(), bins=30, kde=True)
    plt.title('Distribution of Excess Readmission Ratio')
    plt.xlabel('Excess Readmission Ratio')
    plt.ylabel('Frequency')
    plt.savefig('excess_readmission_ratio_distribution.png')  # Save plot
    print("Plot saved as 'excess_readmission_ratio_distribution.png'")
    
    # Scatter plot of Predicted vs. Expected Readmission Rate
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Expected Readmission Rate', y='Predicted Readmission Rate', data=df)
    plt.title('Predicted vs. Expected Readmission Rate')
    plt.xlabel('Expected Readmission Rate')
    plt.ylabel('Predicted Readmission Rate')
    plt.savefig('predicted_vs_expected_readmission_rate.png')  # Save plot
    print("Plot saved as 'predicted_vs_expected_readmission_rate.png'")
    
    print("Step 2 Completed: Visualizations generated and saved.")

if __name__ == "__main__":
    # Step 1: Load and preprocess the data
    df = load_and_preview_data()
    
    # Step 2: Visualize the data
    visualize_data(df)
