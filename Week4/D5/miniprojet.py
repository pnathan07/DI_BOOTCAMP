import numpy as np
import pandas as pd
import sqlite3
from sqlalchemy import create_engine

# Load the datasets
df_olist_customers = pd.read_csv('path/to/olist_customers_dataset.csv')
df_olist_sellers = pd.read_csv('path/to/olist_sellers_dataset.csv')
df_olist_order_reviews = pd.read_csv('path/to/olist_order_reviews_dataset.csv')
df_olist_order_items = pd.read_csv('path/to/olist_order_items_dataset.csv')
df_olist_products = pd.read_csv('path/to/olist_products_dataset.csv')
df_olist_geolocation = pd.read_csv('path/to/olist_geolocation_dataset.csv')
df_product_category_name_translation = pd.read_csv('path/to/product_category_name_translation.csv')
df_olist_orders = pd.read_csv('path/to/olist_orders_dataset.csv')
df_olist_order_payments = pd.read_csv('path/to/olist_order_payments_dataset.csv')

# Create SQLite engine
engine = create_engine('sqlite://', echo=False)

# Export dataframes to SQLite database
df_olist_customers.to_sql("olist_customers", con=engine, if_exists='replace', index=False)
df_olist_sellers.to_sql("olist_sellers", con=engine, if_exists='replace', index=False)
df_olist_order_reviews.to_sql("olist_order_reviews", con=engine, if_exists='replace', index=False)
df_olist_order_items.to_sql("olist_order_items", con=engine, if_exists='replace', index=False)
df_olist_products.to_sql("olist_products", con=engine, if_exists='replace', index=False)
df_olist_geolocation.to_sql("olist_geolocation", con=engine, if_exists='replace', index=False)
df_product_category_name_translation.to_sql("product_category_name_translation", con=engine, if_exists='replace', index=False)
df_olist_orders.to_sql("olist_orders", con=engine, if_exists='replace', index=False)
df_olist_order_payments.to_sql("olist_order_payments", con=engine, if_exists='replace', index=False)

# Test the setup by selecting the first 5 rows from olist_customers
sql = '''
SELECT * FROM olist_customers
LIMIT 5;
'''

df_sql = pd.read_sql_query(sql, con=engine)
print(df_sql)
query1 = '''
SELECT 
    COUNT(*) AS total_orders,
    SUM(CASE WHEN review_score = 5 THEN 1 ELSE 0 END) AS five_star_orders,
    (SUM(CASE WHEN review_score = 5 THEN 1 ELSE 0 END) * 1.0 / COUNT(*)) * 100 AS percentage_five_star
FROM 
    olist_orders o
JOIN 
    olist_order_reviews r ON o.order_id = r.order_id
WHERE 
    strftime('%Y-%m', order_purchase_timestamp) = '2018-01';
'''

df_query1 = pd.read_sql_query(query1, con=engine)
print(df_query1)
query2 = '''
SELECT 
    strftime('%Y', order_purchase_timestamp) AS year,
    COUNT(*) AS total_orders
FROM 
    olist_orders
GROUP BY 
    strftime('%Y', order_purchase_timestamp)
ORDER BY 
    year;
'''

df_query2 = pd.read_sql_query(query2, con=engine)
print(df_query2)
query3 = '''
SELECT 
    customer_id,
    AVG(payment_value) AS avg_order_value
FROM 
    olist_orders o
JOIN 
    olist_order_payments p ON o.order_id = p.order_id
GROUP BY 
    customer_id;
'''

df_query3 = pd.read_sql_query(query3, con=engine)
print(df_query3.head())
query4 = '''
SELECT 
    customer_city,
    SUM(payment_value) AS total_revenue
FROM 
    olist_orders o
JOIN 
    olist_order_payments p ON o.order_id = p.order_id
JOIN 
    olist_customers c ON o.customer_id = c.customer_id
WHERE 
    strftime('%Y', order_purchase_timestamp) BETWEEN '2016' AND '2018'
GROUP BY 
    customer_city
ORDER BY 
    total_revenue DESC
LIMIT 5;
'''

df_query4 = pd.read_sql_query(query4, con=engine)
print(df_query4)
query5 = '''
SELECT 
    customer_state,
    SUM(payment_value) AS total_revenue
FROM 
    olist_orders o
JOIN 
    olist_order_payments p ON o.order_id = p.order_id
JOIN 
    olist_customers c ON o.customer_id = c.customer_id
WHERE 
    strftime('%Y', order_purchase_timestamp) BETWEEN '2016' AND '2018'
GROUP BY 
    customer_state;
'''

df_query5 = pd.read_sql_query(query5, con=engine)
print(df_query5)
query6 = '''
SELECT 
    seller_id,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.price) AS total_revenue,
    COUNT(DISTINCT o.customer_id) AS total_customers
FROM 
    olist_orders o
JOIN 
    olist_order_items oi ON o.order_id = oi.order_id
GROUP BY 
    seller_id
ORDER BY 
    total_revenue DESC
LIMIT 5;
'''
query7 = '''
SELECT 
    customer_state,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN order_delivered_customer_date IS NOT NULL THEN 1 ELSE 0 END) AS successful_deliveries,
    (SUM(CASE WHEN order_delivered_customer_date IS NOT NULL THEN 1 ELSE 0 END) * 1.0 / COUNT(*)) * 100 AS success_rate
FROM 
    olist_orders o
JOIN 
    olist_customers c ON o.customer_id = c.customer_id
GROUP BY 
    customer_state;
'''

df_query7 = pd.read_sql_query(query7, con=engine)
print(df_query7)
query8 = '''
SELECT 
    pc.product_category_name,
    p.payment_type,
    COUNT(*) AS total_payments
FROM 
    olist_order_items oi
JOIN 
    olist_products p ON oi.product_id = p.product_id
JOIN 
    product_category_name_translation pc ON p.product_category_name = pc.product_category_name
JOIN 
    olist_order_payments op ON oi.order_id = op.order_id
GROUP BY 
    pc.product_category_name, p.payment_type
ORDER BY 
    total_payments DESC;
'''

df_query8 = pd.read_sql_query(query8, con=engine)
print(df_query8.head())
import math

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1 
    dlon = lon2 - lon1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

query9 = '''
SELECT 
    c1.city AS city1, c2.city AS city2, 
    c1.lat AS lat1, c1.lng AS lng1, 
    c2.lat AS lat2, c2.lng AS lng2
FROM 
    (SELECT DISTINCT city, lat, lng FROM olist_geolocation) c1
CROSS JOIN 
    (SELECT DISTINCT city, lat, lng FROM olist_geolocation) c2
WHERE 
    c1.city < c2.city
'''

df_query9 = pd.read_sql_query(query9, con=engine)

# Calculate the distance
df_query9['distance'] = df_query9.apply(lambda row: haversine(row['lat1'], row['lng1'], row['lat2'], row['lng2']), axis=0)

print(df_query9.head())
