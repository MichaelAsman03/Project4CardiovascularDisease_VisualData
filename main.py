import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1
try:
    data = pd.read_csv("data/Rates_and_Trends_ in_Heart_Disease _and_Stroke_Mortality_Among_US_Adults_35_by_County_Age_Group_Race_Ethnicity_and_Sex_2000-2019.csv", nrows=20)
    print("Successfully loaded 20 rows of data")
except Exception as e:
    print("Error:", e)
    print("Make sure:")
    print("Files in directory", os.listdir('.'))
    exit()

    # Step 2
clean_data = data.dropna(subset=['Data_Value'])
clean_data = clean_data.rename(columns={
    'Stratification1': 'Age_Group',
    'Stratification2': 'Race',
    'Stratification3': 'Sex'
})

if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Graph 1
plt.figure(figsize=(12, 6))  
plt.bar(clean_data['Age_Group'], clean_data['Data_Value'], color='skyblue')
plt.title("Mortality Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Mortality Rate")
plt.xticks(rotation=45) 
plt.tight_layout()  
plt.savefig("screenshots/age_group_bar.png")
plt.close()

# Graph 2: Line chart of Mortality Over Time by Sex
plt.figure(figsize=(12, 6))
for sex in clean_data['Sex'].unique():
    sex_data = clean_data[clean_data['Sex'] == sex]
    plt.plot(sex_data['Year'], sex_data['Data_Value'], label=sex, marker='o')
plt.title("Mortality Trend by Sex")
plt.xlabel("Year")
plt.ylabel("Mortality Rate")
plt.legend()
plt.grid(True)  
plt.savefig("screenshots/trend_by_sex.png")
plt.close()

# Graph 3: Box plot of Mortality by Race
plt.figure(figsize=(14, 7))
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


print("Successfully created 3 graphs in the screenshots folder!")
