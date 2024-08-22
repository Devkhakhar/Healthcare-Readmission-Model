import pandas as pd

def load_and_preview_data():
    # Load the downloaded dataset
    df = pd.read_csv('hospital_readmissions_data.csv')
    
    # Preview the first few rows
    print(df.head())
    
if __name__ == "__main__":
    load_and_preview_data()
