import pandas as pd

# Load the dataset
df = pd.read_csv('world_happiness_report.csv')

# Display the first few rows and check the structure
print(df.head())
# Filter data for the year 2019
df_2019 = df[df['Year'] == 2019]

# Inspect the structure and contents for the year 2019
print(df_2019.head())
# Check for missing values
print(df_2019.isnull().sum())

# Drop rows with missing values
df_2019.dropna(inplace=True)
import matplotlib.pyplot as plt

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df_2019['Social_Support'], df_2019['Happiness_Score'], alpha=0.8)
plt.title('Relationship between Social Support and Happiness Score (2019)')
plt.xlabel('Social Support')
plt.ylabel('Happiness Score')
plt.grid(True)
plt.show()
# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Bar plot for GDP per Capita
ax1.bar(df_2019['Region'], df_2019['GDP_per_Capita'], color='blue', alpha=0.6)
ax1.set_title('GDP per Capita across Regions (2019)')
ax1.set_xlabel('Region')
ax1.set_ylabel('GDP per Capita')
ax1.tick_params(axis='x', rotation=90)

# Line plot for Healthy Life Expectancy
ax2.plot(df_2019['Region'], df_2019['Healthy_Life_Expectancy'], marker='o', color='green', linestyle='-', linewidth=2, markersize=8)
ax2.set_title('Healthy Life Expectancy across Regions (2019)')
ax2.set_xlabel('Region')
ax2.set_ylabel('Healthy Life Expectancy')
ax2.tick_params(axis='x', rotation=90)

plt.tight_layout()
plt.show()
