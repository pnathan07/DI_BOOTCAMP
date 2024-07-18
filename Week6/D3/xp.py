#Exercice 1 
import urllib.request
import zipfile
from functools import partial
import os

chinook_url = 'http://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip'
if not os.path.exists('chinook.zip'):
    print('downloading chinook.zip ', end='')
    with urllib.request.urlopen(chinook_url) as response:
        with open('chinook.zip', 'wb') as f:
            for data in iter(partial(response.read, 4*1024), b''):
                print('.', end='', flush=True)
                f.write(data)

zipfile.ZipFile('chinook.zip').extractall()
assert os.path.exists('chinook.db')
from IPython.display import display
import pandas as pd

def sql(query):
    print()
    print(query)
    print()

def get_results(query):
    global engine
    q = query.statement if isinstance(query, sqlalchemy.orm.query.Query) else query
    return pd.read_sql(q, engine)

def display_results(query):
    df = get_results(query)
    display(df)
    sql(query)
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

# Create an engine object
engine = sqlalchemy.create_engine('sqlite:///chinook.db')

# Connect to the database
cur = engine.connect()

# Reflect the database schema
metadata = sqlalchemy.MetaData()
metadata.reflect(engine)

# Automap the base
Base = automap_base(metadata=metadata)
Base.prepare()

# Prepare an ORM session
Session = sessionmaker(bind=engine)
session = Session()

#Eercice 2 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

# Create an engine object
engine = sqlalchemy.create_engine('sqlite:///chinook.db')

# Connect to the database
cur = engine.connect()

# Reflect the database schema
metadata = sqlalchemy.MetaData()
metadata.reflect(engine)

# Automap the base
Base = automap_base(metadata=metadata)
Base.prepare()

# Prepare an ORM session
Session = sessionmaker(bind=engine)
session = Session()

# Print out all the table names
print("Tables in the database:")
for table in metadata.tables.keys():
    print(table)

# Get the Track class
Track = Base.classes.tracks

# Print out the first three tracks in the tracks table
first_three_tracks = session.query(Track).limit(3).all()
print("\nFirst three tracks:")
for track in first_three_tracks:
    print(f"Track ID: {track.TrackId}, Name: {track.Name}")

# Get the Album class
Album = Base.classes.albums

# Print out the track name and albums title of the first 20 tracks in the tracks table
tracks_with_albums = (
    session.query(Track.Name, Album.Title)
    .join(Album, Track.AlbumId == Album.AlbumId)
    .limit(20)
    .all()
)

print("\nFirst 20 tracks with their album titles:")
for track_name, album_title in tracks_with_albums:
    print(f"Track Name: {track_name}, Album Title: {album_title}")

#Exercice 3 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

# Create an engine object
engine = sqlalchemy.create_engine('sqlite:///chinook.db')

# Connect to the database
cur = engine.connect()

# Reflect the database schema
metadata = sqlalchemy.MetaData()
metadata.reflect(engine)

# Automap the base
Base = automap_base(metadata=metadata)
Base.prepare()

# Prepare an ORM session
Session = sessionmaker(bind=engine)
session = Session()

# Get the required classes
InvoiceItem = Base.classes.invoice_items
Track = Base.classes.tracks
Album = Base.classes.albums
Artist = Base.classes.artists

# Step 1: Print out the first 10 track sales from the invoice_items table
first_10_sales = session.query(InvoiceItem).limit(10).all()
print("First 10 track sales from the invoice_items table:")
for sale in first_10_sales:
    print(f"InvoiceItem ID: {sale.InvoiceLineId}, Track ID: {sale.TrackId}, Quantity: {sale.Quantity}")

# Step 2: Print the names of the tracks sold and the quantity sold for these first 10 sales
first_10_sales_with_names = (
    session.query(InvoiceItem.Quantity, Track.Name)
    .join(Track, InvoiceItem.TrackId == Track.TrackId)
    .limit(10)
    .all()
)

print("\nNames of the tracks sold and the quantity sold for the first 10 sales:")
for quantity, track_name in first_10_sales_with_names:
    print(f"Track Name: {track_name}, Quantity Sold: {quantity}")

# Step 3: Print the names of the top 10 tracks sold and how many times they were sold
top_10_tracks_sold = (
    session.query(Track.Name, func.count(InvoiceItem.TrackId).label('sales_count'))
    .join(InvoiceItem, Track.TrackId == InvoiceItem.TrackId)
    .group_by(Track.Name)
    .order_by(func.count(InvoiceItem.TrackId).desc())
    .limit(10)
    .all()
)

print("\nTop 10 tracks sold and how many times they were sold:")
for track_name, sales_count in top_10_tracks_sold:
    print(f"Track Name: {track_name}, Sales Count: {sales_count}")

# Step 4: Print the top 10 highest selling artists
top_10_selling_artists = (
    session.query(Artist.Name, func.sum(InvoiceItem.Quantity).label('total_sold'))
    .join(Track, InvoiceItem.TrackId == Track.TrackId)
    .join(Album, Track.AlbumId == Album.AlbumId)
    .join(Artist, Album.ArtistId == Artist.ArtistId)
    .group_by(Artist.Name)
    .order_by(func.sum(InvoiceItem.Quantity).desc())
    .limit(10)
    .all()
)

print("\nTop 10 highest selling artists:")
for artist_name, total_sold in top_10_selling_artists:
    print(f"Artist Name: {artist_name}, Total Sold: {total_sold}")

#Exercice 4
import pandas as pd
import numpy as np
from plotnine import ggplot, aes, geom_point, labs, theme

# Step 1: Create a pandas DataFrame with two columns, x and y, each containing 20 random numbers
np.random.seed(42)  # for reproducibility
data = {
    'x': np.random.rand(20),
    'y': np.random.rand(20)
}
df = pd.DataFrame(data)

# Step 2: Use Plotnine to create a scatter plot of y versus x
# Step 3: Add x and y-axis labels as ‘X-Value’ and ‘Y-Value’, respectively. Also, add a plot title ‘Basic Scatter Plot’.
plot = (
    ggplot(df, aes(x='x', y='y')) +
    geom_point() +
    labs(title='Basic Scatter Plot', x='X-Value', y='Y-Value') +
    theme(figure_size=(8, 6))
)

# Display the plot
print(plot)

#Exercice 5
import pandas as pd
import numpy as np
from plotnine import ggplot, aes, geom_bar, labs, theme

# Step 1: Generate a pandas DataFrame with a column category
categories = ['A', 'B', 'C']
np.random.seed(42)  # for reproducibility
data = {
    'category': np.random.choice(categories, 30)
}
df = pd.DataFrame(data)

# Step 2: Create a bar plot that shows the count of each category using Plotnine
plot = (
    ggplot(df, aes(x='category')) +
    geom_bar() +
    labs(title='Category Frequency', x='Category', y='Frequency') +
    theme(figure_size=(8, 6))
)

# Step 3: Display the plot
print(plot)

#Exercice 6 
import pandas as pd
import numpy as np
from plotnine import ggplot, aes, geom_line, labs, theme

# Step 1: Create a pandas DataFrame with columns x, y1, and y2
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

data = {
    'x': x,
    'y1': y1,
    'y2': y2
}
df = pd.DataFrame(data)

# Step 2: Melt the DataFrame to long format for Plotnine compatibility
df_melted = df.melt(id_vars=['x'], value_vars=['y1', 'y2'], var_name='function', value_name='value')

# Step 3: Create a line plot using Plotnine
plot = (
    ggplot(df_melted, aes(x='x', y='value', color='function')) +
    geom_line() +
    labs(title='Comparison of Two Functions', x='X-Value', y='Y-Value') +
    theme(figure_size=(10, 6))
)

# Step 4: Display the plot
print(plot)

#Exercice 7 
import plotly.graph_objects as go

# Step 1: Define the data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [200, 210, 250, 300, 320, 340, 360, 380, 390, 400, 420, 440]

# Step 2: Create a line chart
fig = go.Figure()

# Step 3: Add data to the line chart
fig.add_trace(go.Scatter(x=months, y=sales, mode='lines+markers', name='Sales'))

# Step 4: Add a title to the chart
fig.update_layout(title='Monthly Sales Data', xaxis_title='Month', yaxis_title='Sales')

# Step 5: Display the plot
fig.show()

#Exercice 8
import plotly.graph_objects as go

# Step 1: Define the data
genres = ['Fiction', 'Non-Fiction', 'Sci-Fi', 'Mystery', 'Biography']
books_sold = [120, 150, 90, 80, 130]

# Step 2: Create a bar chart
fig = go.Figure()

# Step 3: Add data to the bar chart
fig.add_trace(go.Bar(x=genres, y=books_sold, marker_color=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A'], name='Books Sold'))

# Step 4: Add a title to the chart
fig.update_layout(title='Books Sold by Genre', xaxis_title='Genre', yaxis_title='Number of Books Sold')

# Step 5: Display the plot
fig.show()

