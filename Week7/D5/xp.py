import pandas as pd

# Load the dataset
file_path = 'path_to_aapl_stock_data.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(df.head())

# Check for null values and data types
print(df.info())
print(df.isnull().sum())
# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Check the frequency of the time series
print(df.index.freq)

# Plot time series to examine trends
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='Closing Price')
plt.title('AAPL Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(12, 6))

# Closing Prices
plt.subplot(2, 1, 1)
plt.plot(df.index, df['Close'], label='Closing Price', color='blue')
plt.title('AAPL Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Traded Volume
plt.subplot(2, 1, 2)
plt.plot(df.index, df['Volume'], label='Traded Volume', color='orange')
plt.title('AAPL Traded Volume')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
import mplfinance as mpf

# Prepare data for candlestick chart
data = df[['Open', 'High', 'Low', 'Close']]

# Create a candlestick chart
mpf.plot(data, type='candle', style='charles', title='AAPL Candlestick Chart', ylabel='Price')
# Summary statistics for key columns
print(df[['Close', 'Volume']].describe())

# Moving Average
df['Moving_Avg_30'] = df['Close'].rolling(window=30).mean()

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='Closing Price')
plt.plot(df.index, df['Moving_Avg_30'], label='30-Day Moving Average', color='red')
plt.title('AAPL Closing Prices with 30-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
from scipy import stats

# Extract data for different years
df['Year'] = df.index.year
years = df['Year'].unique()

# Calculate average closing price for each year
average_closing_prices = df.groupby('Year')['Close'].mean()

# Perform t-test (e.g., between 2022 and 2023)
year1_prices = df[df['Year'] == 2022]['Close']
year2_prices = df[df['Year'] == 2023]['Close']

t_stat, p_value = stats.ttest_ind(year1_prices, year2_prices)
print(f"T-test result: t-statistic = {t_stat:.2f}, p-value = {p_value:.2f}")
# Calculate daily returns
df['Daily_Return'] = df['Close'].pct_change().dropna()

# Summary statistics for daily returns
print(df['Daily_Return'].describe())

# Test for normality using Shapiro-Wilk test
shapiro_test = stats.shapiro(df['Daily_Return'].dropna())
print(f"Shapiro-Wilk Test: W-statistic = {shapiro_test[0]:.2f}, p-value = {shapiro_test[1]:.2f}")
from scipy.signal import convolve

# Apply convolution for moving averages
window_size = 30
weights = np.ones(window_size) / window_size
smoothed_close = convolve(df['Close'], weights, mode='valid')

plt.figure(figsize=(12, 6))
plt.plot(df.index[window_size-1:], smoothed_close, label='Smoothed Closing Price')
plt.plot(df.index, df['Close'], label='Closing Price', color='blue')
plt.title('AAPL Closing Prices with Smoothed Data')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
# Correlation between moving average and trading volume
moving_avg_30 = df['Moving_Avg_30'].dropna()
volume = df['Volume'][moving_avg_30.index]

correlation = np.corrcoef(moving_avg_30, volume)[0, 1]
print(f"Correlation between 30-Day Moving Average and Trading Volume: {correlation:.2f}")
