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


# Step 3
import os
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Graph 1: Bar chart of Mortality by Age Group
plt.figure(figsize=(10, 5))  
plt.bar(clean_data['Age_Group'], clean_data['Data_Value'])
plt.title("Mortality Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Mortality Rate")
plt.xticks(rotation=45) 
plt.tight_layout()  
plt.savefig("screenshots/age_group_bar.png")
plt.close()