import requests
import pandas as pd

def download_dataset():
    # Download URL provided in the metadata
    download_url = "https://data.cms.gov/provider-data/sites/default/files/resources/bfd0c8c38e221fa2045de81691a6e300_1720656704/FY_2024_Hospital_Readmissions_Reduction_Program_Hospital.csv"
    
    response = requests.get(download_url)
    
    if response.status_code == 200:
        # Save the CSV file
        with open('hospital_readmissions_data.csv', 'wb') as file:
            file.write(response.content)
        print("Dataset downloaded successfully and saved as 'hospital_readmissions_data.csv'")
    else:
        print(f"Failed to download dataset. Status code: {response.status_code}")

if __name__ == "__main__":
    download_dataset()
