import pandas as pd
import numpy as np
from datetime import datetime

# Import the dataset
url = 'path_to_airplane_crashes_dataset.csv'
df = pd.read_csv(url)

# Display the first few rows of the dataframe
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Handle missing values
# For simplicity, we'll drop rows with missing crucial columns, but in practice, consider imputation or other strategies
df.dropna(subset=['Date', 'Fatalities'], inplace=True)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Convert 'Fatalities' to numeric, handling non-numeric values
df['Fatalities'] = pd.to_numeric(df['Fatalities'], errors='coerce')

# Drop rows where 'Fatalities' is NaN after conversion
df.dropna(subset=['Fatalities'], inplace=True)
# Basic statistics
print(df.describe())

# Number of crashes and fatalities
num_crashes = df.shape[0]
total_fatalities = df['Fatalities'].sum()
print(f'Number of crashes: {num_crashes}')
print(f'Total fatalities: {total_fatalities}')

# Crashes over time
df['Year'] = df['Date'].dt.year
crashes_per_year = df.groupby('Year').size()
print(crashes_per_year)

# Plot frequency of crashes over time
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(crashes_per_year.index, crashes_per_year.values, marker='o')
plt.title('Number of Airplane Crashes per Year')
plt.xlabel('Year')
plt.ylabel('Number of Crashes')
plt.grid(True)
plt.show()
from scipy import stats

# Calculate key statistics for fatalities
mean_fatalities = np.mean(df['Fatalities'])
median_fatalities = np.median(df['Fatalities'])
std_fatalities = np.std(df['Fatalities'])
print(f'Mean Fatalities: {mean_fatalities}')
print(f'Median Fatalities: {median_fatalities}')
print(f'Standard Deviation of Fatalities: {std_fatalities}')

# Hypothesis Testing: Compare average fatalities between two decades
df['Decade'] = (df['Year'] // 10) * 10
decade_groups = df.groupby('Decade')['Fatalities']

# Example: Comparing fatalities between 1980s and 1990s
fatalities_1980s = decade_groups.get_group(1980)
fatalities_1990s = decade_groups.get_group(1990)

# T-test
t_stat, p_value = stats.ttest_ind(fatalities_1980s, fatalities_1990s, equal_var=False)
print(f'T-test Statistic: {t_stat}')
print(f'P-value: {p_value}')
import seaborn as sns

# Histogram of fatalities
plt.figure(figsize=(12, 6))
sns.histplot(df['Fatalities'], bins=30, kde=True)
plt.title('Histogram of Fatalities')
plt.xlabel('Number of Fatalities')
plt.ylabel('Frequency')
plt.show()

# Bar chart of crashes by region
# Assuming 'Region' column exists
crashes_by_region = df['Region'].value_counts()
plt.figure(figsize=(12, 6))
crashes_by_region.plot(kind='bar')
plt.title('Number of Crashes by Region')
plt.xlabel('Region')
plt.ylabel('Number of Crashes')
plt.show()
