import numpy as np
import pandas as pd

# Seed for reproducibility
np.random.seed(0)

# Number of entries
n_entries = 1000

# Simulating dataset
time = np.linspace(0, 100, n_entries)
temperature = 20 + 5 * np.sin(np.pi * time / 50) + np.random.normal(0, 0.5, n_entries)
pressure = 1013 + 20 * np.cos(np.pi * time / 25) + np.random.normal(0, 1, n_entries)
chemical_concentration = 5 + 2 * np.sin(np.pi * time / 10) + np.random.normal(0, 0.2, n_entries)

# Creating DataFrame
ninja_data = pd.DataFrame({
    'Time': time,
    'Temperature': temperature,
    'Pressure': pressure,
    'Chemical Concentration': chemical_concentration
})

# Normalization function
def normalize(column):
    return (column - column.mean()) / column.std()

# Applying normalization
normalized_data = ninja_data.copy()
for column in ['Temperature', 'Pressure', 'Chemical Concentration']:
    normalized_data[column] = normalize(ninja_data[column])

print("Normalized Data (first 5 rows):")
print(normalized_data.head())
# Applying logarithmic scaling to avoid log(0) issues, we add a small constant.
log_scaled_data = ninja_data.copy()
for column in ['Temperature', 'Pressure', 'Chemical Concentration']:
    log_scaled_data[column] = np.log(ninja_data[column] + 1)  # Adding 1 to avoid log(0)

print("Log-scaled Data (first 5 rows):")
print(log_scaled_data.head())
from numpy.fft import fft, fftfreq

# Fourier Transformation for temperature data
N = len(ninja_data['Time'])
T = ninja_data['Time'][1] - ninja_data['Time'][0]  # Time step
yf = fft(normalized_data['Temperature'])
xf = fftfreq(N, T)[:N // 2]

# Plotting Fourier Transform
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))
plt.title('Fourier Transform of Temperature Data')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
# Descriptive statistics
print("Descriptive Statistics:")
print(ninja_data.describe())
# Correlation analysis
correlation_matrix = ninja_data.corr()
print("Correlation Matrix:")
print(correlation_matrix)
from scipy import stats

# Example hypothesis test: t-test between Temperature and Pressure
t_stat, p_value = stats.ttest_ind(ninja_data['Temperature'], ninja_data['Pressure'])
print(f"T-test result: t-statistic = {t_stat:.2f}, p-value = {p_value:.2f}")
import seaborn as sns

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
sns.pairplot(ninja_data, diag_kind='kde')
plt.suptitle('Pairplot of Variables')
plt.show()
