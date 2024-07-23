import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway

# Data Import and Cleaning

# Load the dataset
url = 'global_power_dataset.csv'  # Update this with the actual path or URL to your dataset
df = pd.read_csv(url)

# Identify missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Handle missing values
# For numerical columns
df['power_output'].fillna(df['power_output'].median(), inplace=True)
# For categorical columns
df['fuel_type'].fillna('Unknown', inplace=True)

# Convert columns to numerical types if necessary
df['capacity'] = pd.to_numeric(df['capacity'], errors='coerce')

# Exploratory Data Analysis

# Summary statistics for numerical columns
print("\nSummary statistics for numerical columns:")
print(df.describe())

# Mean, median, and standard deviation for power_output
mean_power_output = df['power_output'].mean()
median_power_output = df['power_output'].median()
std_power_output = df['power_output'].std()

print(f"\nMean Power Output: {mean_power_output}")
print(f"Median Power Output: {median_power_output}")
print(f"Standard Deviation of Power Output: {std_power_output}")

# Distribution of power plants by country
print("\nDistribution of power plants by country:")
print(df['country'].value_counts())

# Distribution of power plants by fuel type
print("\nDistribution of power plants by fuel type:")
print(df['fuel_type'].value_counts())

# Statistical Analysis

# Group by fuel type and calculate statistics
grouped_by_fuel = df.groupby('fuel_type')['power_output'].agg(['mean', 'std', 'count'])
print("\nPower output statistics by fuel type:")
print(grouped_by_fuel)

# Hypothesis testing using ANOVA
fuel_types = df['fuel_type'].unique()
samples = [df[df['fuel_type'] == fuel_type]['power_output'] for fuel_type in fuel_types]

# ANOVA test
f_stat, p_value = f_oneway(*samples)
print(f"\nANOVA F-statistic: {f_stat}")
print(f"ANOVA p-value: {p_value}")

# Time Series Analysis

# Ensure the time-related column is in datetime format
df['year_established'] = pd.to_datetime(df['year_established'], format='%Y')

# Extract year from the datetime column
df['year'] = df['year_established'].dt.year

# Group by year and calculate the mean power output
annual_trends = df.groupby('year')['power_output'].mean()
print("\nAnnual average power output:")
print(annual_trends)

# Plot the trend over time
plt.figure(figsize=(12, 6))
plt.plot(annual_trends.index, annual_trends.values, marker='o')
plt.title('Average Power Output Over Time')
plt.xlabel('Year')
plt.ylabel('Average Power Output')
plt.grid(True)
plt.show()

# Explore fuel type mix over the years
fuel_type_trends = df.groupby(['year', 'fuel_type']).size().unstack().fillna(0)

# Plot the trends
fuel_type_trends.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Fuel Type Distribution Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Power Plants')
plt.legend(title='Fuel Type')
plt.grid(True)
plt.show()

# Advanced Visualization

# Geographical distribution of power plants
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x='longitude', y='latitude', hue='fuel_type', palette='viridis')
plt.title('Geographical Distribution of Power Plants')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title='Fuel Type')
plt.grid(True)
plt.show()

# Matrix Operations in Real-World Context

# Example matrix operations: Relationships between attributes
attributes = df[['capacity', 'latitude', 'longitude']].dropna()
matrix = attributes.values

# Compute covariance matrix
cov_matrix = np.cov(matrix, rowvar=False)
print("\nCovariance Matrix:\n", cov_matrix)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
print("\nEigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Integrating NumPy with Pandas and Matplotlib

# NumPy for complex filtering in Pandas
high_capacity = df['capacity'] > 500
filtered_df = df[high_capacity]

# Plot using Matplotlib
plt.figure(figsize=(12, 6))
plt.hist(filtered_df['capacity'], bins=20, edgecolor='black')
plt.title('Distribution of High Capacity Power Plants')
plt.xlabel('Capacity')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Using NumPy arrays for visualization
# Example: Calculate and plot the correlation matrix
corr_matrix = np.corrcoef(attributes.T)
plt.figure(figsize=(8, 6))
cax = plt.matshow(corr_matrix, cmap='coolwarm')
plt.colorbar(cax)
plt.xticks(ticks=np.arange(len(attributes.columns)), labels=attributes.columns, rotation=45)
plt.yticks(ticks=np.arange(len(attributes.columns)), labels=attributes.columns)
plt.title('Correlation Matrix of Power Plant Attributes')
plt.show()
