import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import plotnine as p9
import numpy as np
import plotly.graph_objects as go

# Step 1: Connect to the Database
engine = create_engine('sqlite:///chinook.db')
connection = engine.connect()

# Step 2: Reflect the Database and Prepare ORM Classes
metadata = MetaData()
metadata.reflect(engine)
Base = automap_base(metadata=metadata)
Base.prepare()

Session = sessionmaker(bind=engine)
session = Session()

# Step 3: Print Out All the Table Names
print(metadata.tables.keys())

# Step 4: Print Out the First Three Tracks in the Tracks Table
tracks_table = Base.classes.tracks
first_three_tracks = session.query(tracks_table).limit(3).all()
for track in first_three_tracks:
    print(track)

# Step 5: Print the Track Name and Albums Title of the First 20 Tracks
albums_table = Base.classes.albums
first_20_tracks = session.query(tracks_table.Name, albums_table.Title).join(albums_table, tracks_table.AlbumId == albums_table.AlbumId).limit(20).all()
for track, album in first_20_tracks:
    print(f"Track: {track}, Album: {album}")

# Step 6: Print Out the First 10 Track Sales from the Invoice Items Table
invoice_items_table = Base.classes.invoice_items
first_10_sales = session.query(invoice_items_table).limit(10).all()
for sale in first_10_sales:
    print(sale)

# Step 7: Print the Names of the Track Sold and the Quantity Sold
first_10_sales_info = session.query(tracks_table.Name, invoice_items_table.Quantity).join(invoice_items_table, tracks_table.TrackId == invoice_items_table.TrackId).limit(10).all()
for track_name, quantity in first_10_sales_info:
    print(f"Track: {track_name}, Quantity: {quantity}")

# Step 8: Print the Names of Top 10 Tracks Sold and How Many Times They Were Sold
top_10_tracks_sold = session.query(tracks_table.Name, sqlalchemy.func.sum(invoice_items_table.Quantity).label('total_quantity')).join(invoice_items_table, tracks_table.TrackId == invoice_items_table.TrackId).group_by(tracks_table.Name).order_by(sqlalchemy.desc('total_quantity')).limit(10).all()
for track_name, total_quantity in top_10_tracks_sold:
    print(f"Track: {track_name}, Total Sold: {total_quantity}")

# Step 9: Who Are the Top 10 Highest Selling Artists?
artists_table = Base.classes.artists
albums_table = Base.classes.albums

top_10_artists_sold = session.query(artists_table.Name, sqlalchemy.func.sum(invoice_items_table.Quantity).label('total_quantity')).join(albums_table, artists_table.ArtistId == albums_table.ArtistId).join(tracks_table, albums_table.AlbumId == tracks_table.AlbumId).join(invoice_items_table, tracks_table.TrackId == invoice_items_table.TrackId).group_by(artists_table.Name).order_by(sqlalchemy.desc('total_quantity')).limit(10).all()

for artist_name, total_quantity in top_10_artists_sold:
    print(f"Artist: {artist_name}, Total Sold: {total_quantity}")

# Step 11: Create a Basic Scatter Plot Using Plotnine
np.random.seed(42)
df = pd.DataFrame({
    'x': np.random.rand(20),
    'y': np.random.rand(20)
})

plot = (p9.ggplot(df, p9.aes('x', 'y')) + 
        p9.geom_point() + 
        p9.labs(title='Basic Scatter Plot', x='X-Value', y='Y-Value'))

print(plot)

# Step 12: Create a Bar Plot Showing the Frequency of Categories in a Dataset
np.random.seed(42)
categories = np.random.choice(['A', 'B', 'C'], 30)
df = pd.DataFrame({'category': categories})

plot = (p9.ggplot(df, p9.aes('category')) + 
        p9.geom_bar() + 
        p9.labs(title='Category Frequency', x='Category', y='Count'))

print(plot)

# Step 13: Create a Line Plot Comparing Two Different Data Series
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
df = pd.DataFrame({'x': x, 'y1': y1, 'y2': y2})

plot = (p9.ggplot(df) + 
        p9.geom_line(p9.aes('x', 'y1'), color='blue', size=1) + 
        p9.geom_line(p9.aes('x', 'y2'), color='red', size=1) + 
        p9.labs(title='Comparison of Two Functions', x='X-Value', y='Y-Value') + 
        p9.scale_color_manual(values=['blue', 'red']) + 
        p9.theme(legend_position='right'))

print(plot)

# Step 14: Create a Basic Line Chart Using Plotly
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [200, 210, 250, 300, 320, 340, 360, 380, 390, 400, 420, 440]

fig = go.Figure(data=go.Scatter(x=months, y=sales, mode='lines+markers'))

fig.update_layout(title='Monthly Sales Data', xaxis_title='Month', yaxis_title='Sales')

fig.show()

# Step 15: Create a Bar Chart to Represent the Number of Books Sold in Different Genres Using Plotly
genres = ['Fiction', 'Non-Fiction', 'Sci-Fi', 'Mystery', 'Biography']
books_sold = [120, 150, 90, 80, 130]

fig = go.Figure(data=[go.Bar(x=genres, y=books_sold, marker_color=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A'])])

fig.update_layout(title='Books Sold by Genre', xaxis_title='Genre', yaxis_title='Number of Books Sold')

fig.show()
