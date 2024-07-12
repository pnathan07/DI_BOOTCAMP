#Exercice 1 
import pandas as pd

# Load the CSV file
titanic_data = pd.read_csv('train.csv')

# Display the first few rows of the dataset
print(titanic_data.head())

#Exercice 2 
import pandas as pd

# Load the CSV file
iris_data = pd.read_csv('iris.csv')

# Display the first five rows of the dataset
print(iris_data.head())

#Exercice 3 
import pandas as pd
import requests

# URL des données JSON
url = "https://api.example.com/data.json"

# Récupérer les données JSON
response = requests.get(url)
json_data = response.json()

# Charger les données JSON dans un DataFrame Pandas
df = pd.json_normalize(json_data)

# Afficher les cinq premières entrées du DataFrame
print(df.head())

#Exercice 4 
import pandas as pd

# Spécifiez le nom du fichier Excel. Assurez-vous qu'il est dans le même répertoire que votre notebook.
file_path = "sample_excel_file.xlsx"

# Lire le fichier Excel
df = pd.read_excel(file_path)

# Afficher les cinq premières lignes du DataFrame
print(df.head())

#Exercice 5 
import pandas as pd

# Créer un DataFrame simple
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Exporter le DataFrame vers un fichier Excel
excel_file_path = 'simple_dataframe.xlsx'
df.to_excel(excel_file_path, index=False)
print(f"DataFrame exported to {excel_file_path}")

# Exporter le DataFrame vers un fichier JSON
json_file_path = 'simple_dataframe.json'
df.to_json(json_file_path, orient='records', lines=True)
print(f"DataFrame exported to {json_file_path}")
