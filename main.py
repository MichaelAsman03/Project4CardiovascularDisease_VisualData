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

# Graph 1
plt.figure(figsize=(10, 5))  
plt.bar(clean_data['Age_Group'], clean_data['Data_Value'])
plt.title("Mortality Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Mortality Rate")
plt.xticks(rotation=45) 
plt.tight_layout()  
plt.savefig("screenshots/age_group_bar.png")
plt.close()

# Graph 2: Line chart of Mortality Over Time by Sex
plt.figure(figsize=(10, 5))
for sex in clean_data['Sex'].unique():
    sex_data = clean_data[clean_data['Sex'] == sex]
    plt.plot(sex_data['Year'], sex_data['Data_Value'], label=sex, marker='o')
plt.title("Mortality Trend by Sex")
plt.xlabel("Year")
plt.ylabel("Mortality Rate")
plt.legend()  # Show legend
plt.savefig("screenshots/trend_by_sex.png")
plt.close()

# Graph 3: Box plot of Mortality by Race
plt.figure(figsize=(12, 6))
plt.boxplot([clean_data[clean_data['Race'] == race]['Data_Value'] 
             for race in clean_data['Race'].unique()],
            labels=clean_data['Race'].unique())
plt.title("Mortality Rate by Race")
plt.xlabel("Race")
plt.ylabel("Mortality Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("screenshots/race_boxplot.png")
plt.close()

print("Done! Created 3 graphs in the screenshots folder:")
print("- age_group_bar.png")
print("- trend_by_sex.png")
print("- race_boxplot.png")