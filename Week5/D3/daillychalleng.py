import pandas as pd

# Étape 1 : Chargement des Données
df = pd.read_csv('iris.csv')
print("Original DataFrame:\n", df.head())

# Étape 2 : Nettoyage des Données - Gestion des Valeurs Manquantes
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)
df.fillna(df.mean(), inplace=True)
print("Missing Values After Imputation:\n", df.isnull().sum())

# Étape 3 : Nettoyage des Données - Renommer les Colonnes
df.rename(columns={
    'sepal_length': 'Sepal Length (cm)',
    'sepal_width': 'Sepal Width (cm)',
    'petal_length': 'Petal Length (cm)',
    'petal_width': 'Petal Width (cm)',
    'species': 'Species'
}, inplace=True)
print("Renamed Columns:\n", df.columns)

# Étape 4 : Exporter vers un Fichier Excel
cleaned_excel_file = 'cleaned_iris.xlsx'
df.to_excel(cleaned_excel_file, index=False)
print(f"DataFrame exported to {cleaned_excel_file}")

# Étape 5 : Importer depuis un Fichier Excel
df_cleaned = pd.read_excel(cleaned_excel_file)
print("Imported Cleaned DataFrame:\n", df_cleaned.head())
assert df.equals(df_cleaned), "Imported data does not match the cleaned data."
print("Imported data matches the cleaned data.")

# Étape 6 : Sauvegarder un Sous-ensemble en JSON
df_subset = df_cleaned[['Sepal Length (cm)', 'Species']].head(10)
subset_json_file = 'iris_subset.json'
df_subset.to_json(subset_json_file, orient='records', lines=True)
print(f"Subset of DataFrame exported to {subset_json_file}")
