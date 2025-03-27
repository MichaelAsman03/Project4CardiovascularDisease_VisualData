import pandas as pd
import matplotlib.pyplot as plt

# Step 1
try:
    data = pd.read_csv("data/hypertension_cvd_mortality.csv", nrows=20)
    print("Successfully loaded 20 rows of data")
except:
    print("Error: Could not load the CSV file")
    print("Make sure:")
    print("1. The file is named 'hypertension_cvd_mortality.csv'")
    print("2. It's in a folder called 'data'")
    exit()

    # Step 2
clean_data = data.dropna(subset=['Data_Value'])

clean_data = clean_data.rename(columns={
    'Stratification1': 'Age_Group',
    'Stratification2': 'Race',
    'Stratification3': 'Sex'
})

print(f"Working with {len(clean_data)} rows after cleaning")


