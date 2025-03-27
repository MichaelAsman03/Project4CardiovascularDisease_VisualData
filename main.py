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

    