# Importing necessary libraries
import pandas as pd

# Load the dataset
url = 'https://raw.githubusercontent.com/zariable/data/master/global_superstore_orders.csv'
df = pd.read_csv(url)

# Displaying the first few rows and basic info
print(df.head())
print(df.info())

# Data cleaning and preprocessing (if needed)
# Example: Handling missing values
df.dropna(inplace=True)

# Example: Converting date columns to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Further preprocessing as per specific requirements
import plotly.express as px

# Grouping data by year and summing up sales
df['Year'] = df['Order Date'].dt.year
sales_by_year = df.groupby('Year')['Sales'].sum().reset_index()

# Plotting interactive line chart
fig = px.line(sales_by_year, x='Year', y='Sales', title='Sales Trends Over Years')
fig.show()
# Grouping data by country and summing up sales
sales_by_country = df.groupby('Country')['Sales'].sum().reset_index()

# Plotting interactive map
fig = px.choropleth(sales_by_country, locations='Country', locationmode='country names',
                    color='Sales', hover_name='Country', color_continuous_scale='Viridis',
                    title='Sales Distribution by Country')
fig.show()
from plotnine import *

# Grouping data by product and summing up sales
top_products = df.groupby('Product Name')['Sales'].sum().reset_index().nlargest(10, 'Sales')

# Plotting bar chart
(ggplot(top_products, aes(x='Product Name', y='Sales')) +
 geom_bar(stat='identity', fill='skyblue') +
 theme(axis_text_x=element_text(rotation=90, hjust=1)) +
 labs(title='Top 10 Products by Sales', x='Product Name', y='Sales')
)
# Plotting scatter plot
(ggplot(df, aes(x='Discount', y='Profit')) +
 geom_point(alpha=0.6) +
 labs(title='Relationship between Profit and Discount', x='Discount', y='Profit')
)
