import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('IMd.csv')

# Inspecter les données
print(df.head())
print(df.info())
print(df.describe())
# Vérifier les valeurs manquantes
print(df.isnull().sum())

# Traiter les valeurs manquantes (exemple: supprimer les lignes avec des valeurs manquantes)
df = df.dropna()

# Convertir les types de données si nécessaire
df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
df['IMDB_Rating'] = pd.to_numeric(df['IMDB_Rating'], errors='coerce')
df['Meta_score'] = pd.to_numeric(df['Meta_score'], errors='coerce')
df['No_of_votes'] = pd.to_numeric(df['No_of_votes'], errors='coerce')
df['Gross'] = df['Gross'].str.replace(',', '').astype(float)
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Released_Year', y='IMDB_Rating')
plt.title('Trends in IMDB Rating Over the Years')
plt.xlabel('Year')
plt.ylabel('IMDB Rating')
plt.show()
plt.figure(figsize=(14, 7))
sns.countplot(y='Genre', data=df, order=df['Genre'].value_counts().index)
plt.title('Number of Movies Across Different Genres')
plt.xlabel('Number of Movies')
plt.ylabel('Genre')
plt.show()
plt.figure(figsize=(14, 7))
sns.scatterplot(x='Director', y='IMDB_Rating', data=df)
plt.title('Relationship Between Directors and Movie Ratings')
plt.xlabel('Director')
plt.ylabel('IMDB Rating')
plt.xticks(rotation=90)
plt.show()
# Sélectionner les colonnes pertinentes pour l'analyse
selected_columns = ['Stars', 'IMDB_Rating', 'Gross']

# Utiliser pairplot pour visualiser les relations
sns.pairplot(df[selected_columns])
plt.show()
plt.figure(figsize=(14, 7))
sns.boxplot(x='Genre', y='IMDB_Rating', data=df)
plt.title('Distribution of IMDB Ratings Across Different Genres')
plt.xlabel('Genre')
plt.ylabel('IMDB Rating')
plt.xticks(rotation=90)
plt.show()
plt.figure(figsize=(10, 8))
corr_matrix = df[['IMDB_Rating', 'Meta_score', 'No_of_votes', 'Gross']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
