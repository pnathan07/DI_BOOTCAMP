#Exercice 1 
import pandas as pd

# Étape 1 : Charger le Dataset Titanic
df = pd.read_csv('titanic.csv')
print("Original DataFrame:\n", df.head())

# Étape 2 : Identifier les Duplicatas
duplicates = df.duplicated()
print(f"Number of duplicate rows: {duplicates.sum()}")

# Étape 3 : Supprimer les Duplicatas
df_cleaned = df.drop_duplicates()

# Étape 4 : Vérifier la Suppression des Duplicatas
original_row_count = df.shape[0]
cleaned_row_count = df_cleaned.shape[0]

print(f"Number of rows before removing duplicates: {original_row_count}")
print(f"Number of rows after removing duplicates: {cleaned_row_count}")

#Exercice 2
import pandas as pd
from sklearn.impute import SimpleImputer

# Charger le dataset Titanic
df = pd.read_csv('titanic.csv')

# Identifier les colonnes avec des valeurs manquantes
missing_values = df.isnull().sum()
print("Columns with missing values:\n", missing_values)

# Supprimer les lignes avec des valeurs manquantes dans certaines colonnes spécifiques
df_cleaned = df.dropna(subset=['Age', 'Embarked'])

# Créer un imputer pour remplacer les NaN par la médiane dans la colonne 'Age'
imputer = SimpleImputer(strategy='median')
df_cleaned['Age'] = imputer.fit_transform(df_cleaned[['Age']])

# Remplir les valeurs manquantes dans la colonne 'Embarked' avec la valeur la plus fréquente
most_frequent_value = df_cleaned['Embarked'].mode()[0]
df_cleaned['Embarked'].fillna(most_frequent_value, inplace=True)

# Exporter le DataFrame nettoyé vers un nouveau fichier CSV
df_cleaned.to_csv('cleaned_titanic.csv', index=False)

#Exercice 3 
import pandas as pd
import re
from sklearn.preprocessing import StandardScaler

# Charger le dataset Titanic
df = pd.read_csv('titanic.csv')

# Créer une nouvelle colonne 'FamilySize'
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# Extraire le titre à partir de la colonne 'Name'
df['Title'] = df['Name'].apply(lambda x: re.search(' ([A-Za-z]+)\.', x).group(1))

# One-Hot Encoding pour 'Sex' et 'Title'
df = pd.get_dummies(df, columns=['Sex', 'Title'])

# Standardisation des colonnes 'Age' et 'Fare'
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# Afficher les premières lignes du DataFrame transformé
print(df.head())

#Exercice 4 
# Calculer l'IQR pour 'Fare'
Q1_fare = df['Fare'].quantile(0.25)
Q3_fare = df['Fare'].quantile(0.75)
IQR_fare = Q3_fare - Q1_fare

# Définir les seuils pour les valeurs aberrantes
lower_bound_fare = Q1_fare - 1.5 * IQR_fare
upper_bound_fare = Q3_fare + 1.5 * IQR_fare

# Identifier les valeurs aberrantes pour 'Fare'
outliers_fare = df[(df['Fare'] < lower_bound_fare) | (df['Fare'] > upper_bound_fare)]

# Afficher les valeurs aberrantes
print("Outliers in 'Fare':")
print(outliers_fare[['Name', 'Fare']])

from scipy import stats

# Calculer le Z-score pour 'Age'
df['Age_zscore'] = stats.zscore(df['Age'])

# Identifier les valeurs aberrantes pour 'Age' (Z-score absolu > 3)
outliers_age = df[abs(df['Age_zscore']) > 3]

# Afficher les valeurs aberrantes
print("Outliers in 'Age':")
print(outliers_age[['Name', 'Age']])

# Capper les valeurs aberrantes pour 'Fare' avec les seuils IQR
df.loc[df['Fare'] < lower_bound_fare, 'Fare'] = lower_bound_fare
df.loc[df['Fare'] > upper_bound_fare, 'Fare'] = upper_bound_fare

# Vérifier l'impact sur le dataset
print("Dataset after handling outliers in 'Fare':")
print(df[['Name', 'Fare']].loc[outliers_fare.index])

#Exercice 5 
import pandas as pd

# Supposons que 'df' est votre DataFrame contenant les données du Titanic

# Afficher les statistiques descriptives des colonnes numériques
print("Descriptive statistics of numerical columns:")
print(df.describe())

# Afficher les histogrammes des colonnes numériques pour visualiser la distribution
df.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()
from sklearn.preprocessing import StandardScaler

# Sélectionner les colonnes numériques à standardiser (par exemple, 'Age' et 'Fare')
numerical_cols = ['Age', 'Fare']

# Créer un objet StandardScaler
scaler = StandardScaler()

# Appliquer la standardisation aux données sélectionnées
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Afficher les statistiques descriptives après la standardisation
print("Descriptive statistics after standardization:")
print(df.describe())
from sklearn.preprocessing import MinMaxScaler

# Sélectionner les colonnes numériques à normaliser (par exemple, 'Age' et 'Fare')
numerical_cols = ['Age', 'Fare']

# Créer un objet MinMaxScaler
scaler = MinMaxScaler()

# Appliquer la normalisation aux données sélectionnées
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Afficher les statistiques descriptives après la normalisation
print("Descriptive statistics after normalization:")
print(df.describe())

#Exercice 6
import pandas as pd

# Supposons que 'df' est votre DataFrame contenant les données du Titanic

# Afficher les types de données pour identifier les colonnes catégorielles
print("Data types of columns:")
print(df.dtypes)

# Identifier les colonnes catégorielles
categorical_cols = ['Sex', 'Embarked']  # Ajoutez d'autres colonnes au besoin
# Appliquer one-hot encoding aux variables nominales
df_encoded = pd.get_dummies(df, columns=categorical_cols)

# Afficher les premières lignes du DataFrame encodé
print("Encoded DataFrame with one-hot encoding:")
print(df_encoded.head())
from sklearn.preprocessing import LabelEncoder

# Créer un objet LabelEncoder
label_encoder = LabelEncoder()

# Appliquer label encoding à la colonne 'Pclass' par exemple
df_encoded['Pclass_encoded'] = label_encoder.fit_transform(df['Pclass'])

# Afficher les premières lignes du DataFrame avec la colonne encodée
print("Encoded DataFrame with label encoding for 'Pclass':")
print(df_encoded[['Pclass', 'Pclass_encoded']].head())
# Supposons que 'df' est votre DataFrame principal
# Intégrer les colonnes encodées dans le DataFrame principal
df_encoded_final = pd.concat([df.drop(columns=categorical_cols), df_encoded], axis=1)

# Afficher les premières lignes du DataFrame final avec toutes les fonctionnalités encodées
print("Final DataFrame with encoded features:")
print(df_encoded_final.head())

#Exerice 7 
import pandas as pd

# Supposons que 'df' est votre DataFrame contenant les données du Titanic

# Définir les intervalles pour les groupes d'âge
bins = [0, 18, 30, 50, 100]  # Par exemple, groupes d'âge : 0-18, 19-30, 31-50, 51-100

# Définir les étiquettes pour les groupes d'âge
labels = ['0-18', '19-30', '31-50', '51+']

# Créer une nouvelle colonne 'AgeGroup' en utilisant pd.cut()
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# Afficher les premières lignes du DataFrame avec la nouvelle colonne 'AgeGroup'
print("DataFrame with Age Groups:")
print(df[['Age', 'AgeGroup']].head())
# Appliquer one-hot encoding à la colonne 'AgeGroup'
df_encoded = pd.get_dummies(df, columns=['AgeGroup'])

# Afficher les premières lignes du DataFrame encodé
print("Encoded DataFrame with Age Groups:")
print(df_encoded.head())

