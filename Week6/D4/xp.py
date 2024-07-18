# Importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
url = 'https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv'
penguins = pd.read_csv(url)

# Data Cleaning and Exploratory Analysis
# Basic data cleaning (handling missing values, incorrect data types, etc.)
penguins.dropna(inplace=True)  # Drop rows with missing values for simplicity

# EDA - Summarize key statistics
print(penguins.describe())

# EDA - Identify unique values, ranges, and distribution of data
print(penguins.nunique())
print(penguins['species'].value_counts())

# Visualization Tasks

# Species Distribution: Bar chart
plt.figure(figsize=(8, 6))
sns.countplot(x='species', data=penguins)
plt.title('Species Distribution of Penguins')
plt.xlabel('Species')
plt.ylabel('Count')
plt.show()

# Flipper Length vs. Body Mass: Scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='flipper_length_mm', y='body_mass_g', hue='species', data=penguins)
plt.title('Flipper Length vs. Body Mass')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.show()

# Island Distribution: Pie chart
plt.figure(figsize=(8, 6))
penguins['island'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Penguins by Island')
plt.ylabel('')
plt.show()

# Sex Distribution within Species: Grouped bar charts
plt.figure(figsize=(10, 8))
sns.countplot(x='species', hue='sex', data=penguins)
plt.title('Sex Distribution within Each Penguin Species')
plt.xlabel('Species')
plt.ylabel('Count')
plt.legend(title='Sex')
plt.show()

# Heatmap of Correlations
plt.figure(figsize=(10, 8))
sns.heatmap(penguins.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Boxplots for Measurements
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
sns.boxplot(x='species', y='flipper_length_mm', data=penguins)
plt.title('Flipper Length by Species')

plt.subplot(2, 2, 2)
sns.boxplot(x='species', y='body_mass_g', data=penguins)
plt.title('Body Mass by Species')

plt.subplot(2, 2, 3)
sns.boxplot(x='species', y='bill_length_mm', data=penguins)
plt.title('Bill Length by Species')

plt.subplot(2, 2, 4)
sns.boxplot(x='species', y='bill_depth_mm', data=penguins)
plt.title('Bill Depth by Species')

plt.tight_layout()
plt.show()

# Histograms of Measurements
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
sns.histplot(penguins['bill_length_mm'], bins=15, kde=True)
plt.title('Distribution of Bill Length')

plt.subplot(1, 3, 2)
sns.histplot(penguins['bill_depth_mm'], bins=15, kde=True)
plt.title('Distribution of Bill Depth')

plt.subplot(1, 3, 3)
sns.histplot(penguins['flipper_length_mm'], bins=15, kde=True)
plt.title('Distribution of Flipper Length')

plt.tight_layout()
plt.show()

# Combine multiple plots into a single figure (using subplots) - example with pairplot
sns.pairplot(penguins, hue='species', palette='Set2')
plt.suptitle('Pairwise Relationships in Penguin Dataset', y=1.02)
plt.show()

# Conclusion
print("Insights and patterns observed from the visualizations: ...")
