import pandas as pd
import matplotlib.pyplot as plt
import os

# Configuration
FILENAME = 'Rates_and_Trends_in_Heart_Disease_and_Stroke_Mortality_Among_US_Adults__35___by_County__Age_Group__Race_Ethnicity__and_Sex___2000-2019.csv'
SAMPLE_ROWS = 500  # Increased sample size
os.makedirs('screenshots', exist_ok=True)

def load_data():
    """Load dataset with increased sample size"""
    print("\nLoading data...")
    
    try:
        data = pd.read_csv(
            FILENAME,
            nrows=SAMPLE_ROWS,
            usecols=['Year', 'Data_Value', 'Stratification1', 'Stratification2', 'Stratification3'],
            dtype={'Data_Value': float},
            encoding='utf-8'
        )
        
        if data.empty:
            raise ValueError("Empty DataFrame after loading")
            
        data = data.rename(columns={
            'Stratification1': 'Age_Group',
            'Stratification2': 'Race',
            'Stratification3': 'Sex'
        }).dropna(subset=['Data_Value'])
        
        print(f"Loaded {len(data)} valid records")
        print("Data sample:")
        print(data[['Year', 'Age_Group', 'Data_Value']].head())
        return data
        
    except Exception as e:
        print(f"Data loading failed: {str(e)}")
        return None

def create_visualizations(data):
    """Create three professional plots with built-in styles"""
    if data is None or data.empty:
        print("Cannot create visualizations - no valid data")
        return
    
    print("\nGenerating visualizations...")
    
    # Use built-in style
    plt.style.use('ggplot')  # Alternative professional style
    
    # Plot 1: Time Trend of Mortality Rates
    plt.figure(figsize=(12, 6))
    if 'Year' in data.columns:
        yearly_data = data.groupby('Year')['Data_Value'].mean()
        plt.plot(yearly_data.index, yearly_data.values, 
                color='#1f77b4', linewidth=2, marker='o')
        plt.title("Trend of Cardiovascular Mortality Rates (2000-2019)", 
                 fontsize=14, pad=20)
        plt.xlabel("Year", fontsize=12)
        plt.ylabel("Mortality Rate (per 100,000)", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('screenshots/mortality_trend.png', dpi=300)
        plt.close()
        print("- Created mortality trend line plot")
    
    # Plot 2: Age Group Distribution
    plt.figure(figsize=(10, 6))
    if 'Age_Group' in data.columns:
        age_dist = data['Age_Group'].value_counts().sort_index()
        bars = plt.bar(age_dist.index, age_dist.values, 
                      color='#2ca02c', alpha=0.8)
        plt.title("Distribution of Mortality Cases by Age Group", 
                 fontsize=14, pad=20)
        plt.xlabel("Age Group", fontsize=12)
        plt.ylabel("Number of Cases", fontsize=12)
        plt.xticks(rotation=45)
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}', 
                    ha='center', va='bottom')
            
        plt.tight_layout()
        plt.savefig('screenshots/age_distribution.png', dpi=300)
        plt.close()
        print("- Created age group distribution plot")
    
    # Plot 3: Race/Ethnicity Comparison
    plt.figure(figsize=(12, 6))
    if 'Race' in data.columns:
        # Filter for races with sufficient data
        race_counts = data['Race'].value_counts()
        valid_races = race_counts[race_counts >= 5].index
        
        if len(valid_races) > 0:
            plot_data = []
            colors = ['#ff7f0e', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']
            
            for i, race in enumerate(valid_races):
                values = data[data['Race'] == race]['Data_Value']
                plt.boxplot(values, positions=[i], widths=0.6,
                           patch_artist=True,
                           boxprops=dict(facecolor=colors[i % len(colors)]))
            
            plt.xticks(range(len(valid_races)), valid_races)
            plt.title("Mortality Rate Distribution by Race/Ethnicity", 
                     fontsize=14, pad=20)
            plt.xlabel("Race/Ethnicity", fontsize=12)
            plt.ylabel("Mortality Rate (per 100,000)", fontsize=12)
            plt.xticks(rotation=45)
            plt.grid(True, axis='y', linestyle='--')
            plt.tight_layout()
            plt.savefig('screenshots/race_comparison.png', dpi=300)
            plt.close()
            print("- Created race comparison boxplot")
        else:
            print("- Skipped race plot: insufficient data points per category")

if __name__ == "__main__":
    data = load_data()
    create_visualizations(data)
    print("\nProcess completed. Check 'screenshots' folder for:")
    print("- mortality_trend.png")
    print("- age_distribution.png")
    print("- race_comparison.png")