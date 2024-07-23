#Exercice 1
import numpy as np

# Create a 3x3 matrix
matrix = np.array([[1, 2, 3],
                   [0, 1, 4],
                   [5, 6, 0]])

# Calculate the determinant
determinant = np.linalg.det(matrix)
print("Determinant of the matrix:", determinant)

# Find the inverse of the matrix
try:
    inverse_matrix = np.linalg.inv(matrix)
    print("Inverse of the matrix:\n", inverse_matrix)
except np.linalg.LinAlgError:
    print("The matrix is singular and cannot be inverted.")

#Exercice 2 
import numpy as np

# Generate an array of 50 random numbers
data = np.random.rand(50)

# Calculate the mean
mean_value = np.mean(data)
print("Mean:", mean_value)

# Calculate the median
median_value = np.median(data)
print("Median:", median_value)

# Calculate the standard deviation
std_deviation = np.std(data)
print("Standard Deviation:", std_deviation)


#Exercice 3 
import numpy as np
import pandas as pd

# Générer une gamme de dates pour janvier 2023
dates = np.arange('2023-01', '2023-02', dtype='datetime64[D]')

# Convertir les dates au format YYYY/MM/DD
formatted_dates = [date.astype(str).replace('-', '/') for date in dates]

# Afficher les dates formatées
print("Original Dates:")
print(dates)
print("\nFormatted Dates:")
print(formatted_dates)


#Exercice 4 
import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(0)

# Create a DataFrame with random numbers
data = np.random.rand(5, 4)  # 5 rows and 4 columns of random numbers
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

print("Original DataFrame:")
print(df)

# Conditional selection: select rows where column 'A' > 0.5
filtered_df = df[df['A'] > 0.5]
print("\nFiltered DataFrame (A > 0.5):")
print(filtered_df)

# Aggregation functions
column_sums = df.sum()
column_averages = df.mean()

print("\nColumn Sums:")
print(column_sums)

print("\nColumn Averages:")
print(column_averages)


#Exercice 5 
import numpy as np
import matplotlib.pyplot as plt

# Create a 5x5 array with random values between 0 and 255
image = np.random.randint(0, 256, size=(5, 5), dtype=np.uint8)

print("5x5 Grayscale Image Array:")
print(image)

# Display the image using Matplotlib
plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.colorbar()
plt.title('5x5 Grayscale Image')
plt.show()

#Exercice 6
import numpy as np
from scipy import stats

# Productivity scores of employees before the training program
productivity_before = np.random.normal(loc=50, scale=10, size=30)

# Productivity scores of the same employees after the training program
productivity_after = productivity_before + np.random.normal(loc=5, scale=3, size=30)

# Calculate the mean and standard deviation before and after the training
mean_before = np.mean(productivity_before)
std_before = np.std(productivity_before, ddof=1)
mean_after = np.mean(productivity_after)
std_after = np.std(productivity_after, ddof=1)

# Print the means and standard deviations
print(f"Mean productivity before: {mean_before:.2f}")
print(f"Standard deviation before: {std_before:.2f}")
print(f"Mean productivity after: {mean_after:.2f}")
print(f"Standard deviation after: {std_after:.2f}")

# Perform the paired t-test
t_statistic, p_value = stats.ttest_rel(productivity_before, productivity_after)

# Print the t-statistic and p-value
print(f"T-statistic: {t_statistic:.2f}")
print(f"P-value: {p_value:.4f}")

# Interpretation
alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in productivity before and after the training program.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in productivity before and after the training program.")


#Exercice 7 
import numpy as np

# Create two NumPy arrays
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([15, 18, 25, 45, 40])

# Perform element-wise comparison
comparison_result = array1 > array2

# Print the result
print("Array 1:", array1)
print("Array 2:", array2)
print("Comparison Result (Array1 > Array2):", comparison_result)


#Exercice 8
import pandas as pd
import numpy as np

# Generate a date range for the year 2023
date_range = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')

# Generate random data for the time series
data = np.random.randn(len(date_range))  # Random data for demonstration

# Create a DataFrame
df = pd.DataFrame({'Date': date_range, 'Value': data})
df.set_index('Date', inplace=True)

# Print the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Slicing for different intervals
print("\nData from January to March:")
print(df['2023-01-01':'2023-03-31'])

print("\nData from April to June:")
print(df['2023-04-01':'2023-06-30'])

print("\nData from July to September:")
print(df['2023-07-01':'2023-09-30'])

print("\nData from October to December:")
print(df['2023-10-01':'2023-12-31'])


#Exercice 9 
import numpy as np
import pandas as pd

# Step 1: Convert NumPy Array to Pandas DataFrame

# Create a NumPy array
numpy_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Convert the NumPy array to a Pandas DataFrame
df_from_numpy = pd.DataFrame(numpy_array, columns=['Column1', 'Column2', 'Column3'])

print("DataFrame from NumPy Array:")
print(df_from_numpy)

# Step 2: Convert Pandas DataFrame to NumPy Array

# Convert the Pandas DataFrame back to a NumPy array
numpy_array_from_df = df_from_numpy.to_numpy()

print("\nNumPy Array from DataFrame:")
print(numpy_array_from_df)


#Exercice 10
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create a NumPy array with random numbers
np.random.seed(0)  # For reproducibility
x = np.arange(0, 10)  # X-axis values from 0 to 9
y = np.random.random(size=10)  # Random Y-axis values

# Step 2: Plot the data using Matplotlib
plt.figure(figsize=(10, 6))  # Set the size of the figure

# Create a line plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Random Data')

# Add titles and labels
plt.title('Line Graph of Random Numbers')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a legend
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
