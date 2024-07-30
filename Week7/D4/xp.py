#Exercice 1 
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Define the dataset
house_sizes = np.array([50, 70, 80, 100, 120]).reshape(-1, 1)
house_prices = np.array([150000, 200000, 210000, 250000, 280000])
# Create and fit the model
model = LinearRegression()
model.fit(house_sizes, house_prices)

# Get the slope (coefficient) and intercept of the regression line
slope = model.coef_[0]
intercept = model.intercept_

print(f'Slope: {slope:.2f}')
print(f'Intercept: {intercept:.2f}')
# Predict the price for a house size of 90 square meters
house_size_to_predict = np.array([[90]])
predicted_price = model.predict(house_size_to_predict)

print(f'Predicted price for a 90 square meter house: {predicted_price[0]:.2f}')
# Plot the data and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(house_sizes, house_prices, color='blue', label='Actual Prices')
plt.plot(house_sizes, model.predict(house_sizes), color='red', linewidth=2, label='Regression Line')
plt.scatter(house_size_to_predict, predicted_price, color='green', label='Predicted Price (90 sqm)', marker='x', s=100)
plt.xlabel('House Size (square meters)')
plt.ylabel('House Price')
plt.title('House Price vs Size')
plt.legend()
plt.grid(True)
plt.show()


#Exercice 2 
import numpy as np
from scipy import stats

# Define the dataset
fertilizer_1 = np.array([5, 6, 7, 6, 5])
fertilizer_2 = np.array([7, 8, 7, 9, 8])
fertilizer_3 = np.array([4, 5, 4, 3, 4])

# Perform one-way ANOVA
f_value, p_value = stats.f_oneway(fertilizer_1, fertilizer_2, fertilizer_3)

# Print the results
print(f'F-value: {f_value:.2f}')
print(f'P-value: {p_value:.2f}')

# Interpret the results
if p_value < 0.05:
    print("The fertilizers have significantly different effects on plant growth.")
else:
    print("There is no significant difference in the effects of the fertilizers on plant growth.")


#Exercice 3 
from scipy.stats import binom

# Parameters
n = 10  # Number of trials (coin flips)
p = 0.5  # Probability of success (getting heads)
k = 5  # Number of successes (getting exactly 5 heads)

# Calculate the probability of getting exactly 5 heads
probability = binom.pmf(k, n, p)

print(f'The probability of getting exactly {k} heads in {n} coin flips is: {probability:.4f}')


#Exercice 4 
import pandas as pd
from scipy.stats import pearsonr, spearmanr

# Sample data
data = pd.DataFrame({
    'age': [23, 25, 30, 35, 40],
    'income': [35000, 40000, 50000, 60000, 70000]
})

# Extract variables
age = data['age']
income = data['income']

# Calculate Pearson correlation
pearson_corr, _ = pearsonr(age, income)

# Calculate Spearman correlation
spearman_corr, _ = spearmanr(age, income)

# Print results
print(f'Pearson correlation coefficient: {pearson_corr:.4f}')
print(f'Spearman correlation coefficient: {spearman_corr:.4f}')


#Exercice 5 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = pd.DataFrame({
    'age': [23, 25, 30, 35, 40],
    'income': [35000, 40000, 50000, 60000, 70000]
})

# Create a scatter plot with a regression line
plt.figure(figsize=(8, 6))
sns.regplot(x='age', y='income', data=data, scatter_kws={'color': 'blue', 's': 100}, line_kws={'color': 'red'})
plt.title('Scatter Plot of Age vs. Income')
plt.xlabel('Age')
plt.ylabel('Income')
plt.grid(True)
plt.show()

