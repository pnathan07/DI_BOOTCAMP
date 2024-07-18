import pandas as pd

# Load the dataset
file_path = 'dataset.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Display the first few rows to understand the structure
df.head()
import matplotlib.pyplot as plt
import seaborn as sns

# Group by state and sum the sales
state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False).reset_index()

# Plotting the top states by sales
plt.figure(figsize=(12, 6))
sns.barplot(x='State', y='Sales', data=state_sales.head(10))
plt.title('Top 10 States by Sales')
plt.xlabel('State')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()
# Filter data for New York and California
ny_ca_sales_profit = df[df['State'].isin(['New York', 'California'])]
ny_ca_sales_profit = ny_ca_sales_profit.groupby('State')[['Sales', 'Profit']].sum()

# Display the comparison
ny_ca_sales_profit
# Filter data for New York and find the customer with the highest sales
ny_customers = df[df['State'] == 'New York']
outstanding_customer_ny = ny_customers.groupby('Customer Name')['Sales'].sum().idxmax()

outstanding_customer_ny
# Group by state and calculate profitability
state_profit = df.groupby('State')['Profit'].sum().sort_values(ascending=False).reset_index()

# Plotting the top states by profitability
plt.figure(figsize=(12, 6))
sns.barplot(x='State', y='Profit', data=state_profit.head(10))
plt.title('Top 10 States by Profitability')
plt.xlabel('State')
plt.ylabel('Total Profit')
plt.xticks(rotation=45)
plt.show()
# Calculate cumulative percentage of customers and profit
df['Cumulative Profit'] = df.sort_values('Profit', ascending=False)['Profit'].cumsum()
total_profit = df['Profit'].sum()

# Identify top 20% of customers
top_customers = df[df['Cumulative Profit'] <= 0.8 * total_profit]['Customer Name'].unique()

# Percentage of customers contributing to 80% of profit
percent_top_customers = len(top_customers) / len(df['Customer Name'].unique()) * 100
percent_top_customers
# Top 20 cities by sales
top_cities_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(20)

# Top 20 cities by profit
top_cities_profit = df.groupby('City')['Profit'].sum().sort_values(ascending=False).head(20)

# Analyze differences in profitability among these cities
top_cities_sales_vs_profit = pd.concat([top_cities_sales, top_cities_profit], axis=1)
top_cities_sales_vs_profit
# Top 20 customers by sales
top_customers_sales = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(20)

top_customers_sales
# Sort customers by sales
customers_sorted = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).reset_index()

# Calculate cumulative sales
customers_sorted['Cumulative Sales'] = customers_sorted['Sales'].cumsum()

# Plot the cumulative curve
plt.figure(figsize=(10, 6))
plt.plot(customers_sorted.index + 1, customers_sorted['Cumulative Sales'], marker='o', linestyle='-')
plt.title('Cumulative Sales by Customers')
plt.xlabel('Customers (sorted by sales)')
plt.ylabel('Cumulative Sales')
plt.grid(True)
plt.show()
