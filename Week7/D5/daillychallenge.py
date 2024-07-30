import pandas as pd

# Load the dataset
file_path = 'path_to_mobile_price_classification_dataset.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(df.head())

# Display the structure of the dataset
print(df.info())
# List of features and their data types
print(df.dtypes)

# Summary of the dataset
print(df.describe(include='all'))
# Check for missing values
print(df.isnull().sum())

# Fill missing values or drop rows/columns with missing values
df.fillna(method='ffill', inplace=True)  # Forward fill example
# df.dropna(inplace=True)  # Alternative: Drop missing values
# Convert categorical data to numerical using one-hot encoding
df = pd.get_dummies(df, drop_first=True)

# Alternative: Use Label Encoding if appropriate
# from sklearn.preprocessing import LabelEncoder
# label_encoder = LabelEncoder()
# df['categorical_column'] = label_encoder.fit_transform(df['categorical_column'])
import numpy as np
from scipy import stats

# Mean, median, and mode for each feature
print("Mean:\n", df.mean())
print("Median:\n", df.median())
print("Mode:\n", df.mode().iloc[0])
# Range, variance, and standard deviation for each feature
range_ = df.max() - df.min()
variance = df.var()
std_dev = df.std()

print("Range:\n", range_)
print("Variance:\n", variance)
print("Standard Deviation:\n", std_dev)
# Skewness and kurtosis
skewness = df.skew()
kurtosis = df.kurtosis()

print("Skewness:\n", skewness)
print("Kurtosis:\n", kurtosis)
# Example: Comparing two groups of prices (e.g., high vs. low)
high_prices = df[df['price_range'] == 3]['battery_power']  # Example condition
low_prices = df[df['price_range'] == 0]['battery_power']

t_stat, p_value = stats.ttest_ind(high_prices, low_prices)
print(f"T-test result: t-statistic = {t_stat:.2f}, p-value = {p_value:.2f}")
# Correlation between features and target variable
correlation = df.corr()['price_range']
print("Feature-Target Correlations:\n", correlation)
# Example: Apply advanced functions if needed
# Normal distribution fit
from scipy.stats import norm

mu, std = norm.fit(df['battery_power'])
print(f"Normal Distribution Fit: mu = {mu:.2f}, std = {std:.2f}")
import matplotlib.pyplot as plt
import seaborn as sns

# Histogram of a feature
plt.figure(figsize=(12, 6))
plt.hist(df['battery_power'], bins=30, edgecolor='k')
plt.title('Histogram of Battery Power')
plt.xlabel('Battery Power')
plt.ylabel('Frequency')
plt.show()

# Scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(df['battery_power'], df['price_range'])
plt.title('Scatter Plot of Battery Power vs. Price Range')
plt.xlabel('Battery Power')
plt.ylabel('Price Range')
plt.show()

# Box plot
plt.figure(figsize=(12, 6))
sns.boxplot(x='price_range', y='battery_power', data=df)
plt.title('Box Plot of Battery Power by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Battery Power')
plt.show()
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
