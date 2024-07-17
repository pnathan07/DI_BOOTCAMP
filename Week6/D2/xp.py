#Exercice 1
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df is your DataFrame with CGPA data

# Example data
data = {
    'CGPA': [3.5, 3.8, 3.2, 3.9, 4.0, 3.7, 3.5, 3.6, 3.9, 3.4, 3.2, 3.8, 3.6, 3.7]
}
df = pd.DataFrame(data)

# Create a histogram using Seaborn
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='CGPA', color='skyblue', bins=5, kde=True)

# Customize the plot
plt.title('Distribution of Students\' CGPA')
plt.xlabel('CGPA')
plt.ylabel('Frequency')

# Display the plot
plt.show()

#Exercice 2 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Étape 1 : Importer les bibliothèques nécessaires
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Étape 2 : Charger le dataset (supposons qu'il soit déjà chargé)
 #df = pd.read_csv('datset.csv')


data = {
    'Choose your gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male'],
    'Do you have Anxiety?': ['Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No']
}
df = pd.DataFrame(data)

# Étape 3 : Créer un diagramme à barres pour comparer les niveaux d'anxiété selon les genres
plt.figure(figsize=(10, 6))
sns.countplot(x='Choose your gender', hue='Do you have Anxiety?', data=df, palette='Set2')

# Étape 4 : Personnaliser le graphique avec une palette de couleurs appropriée
sns.set_palette("Set2")

# Étape 5 : Ajouter un titre au graphique et l'afficher
plt.title('Proportion of Students Experiencing Anxiety Across Different Genders')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Do you have Anxiety?')
plt.show()

#Exercice 3 
# Étape 1 : Importer les bibliothèques nécessaires
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Étape 2 : Préparer les données (supposons que le DataFrame 'df' soit déjà chargé)
# Exemple de données
data = {
    'Age': [18, 19, 20, 21, 22, 23, 24, 25],
    'Panic Attack': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes']
}
df = pd.DataFrame(data)

# Convertir les réponses de crise de panique en valeurs numériques
df['Panic Attack'] = df['Panic Attack'].map({'Yes': 1, 'No': 0})

# Étape 3 : Créer un diagramme de dispersion
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Panic Attack', data=df, hue='Panic Attack', palette='Set1')

# Étape 4 : Personnaliser le graphique
plt.title('Relationship Between Age and Occurrence of Panic Attacks')
plt.xlabel('Age')
plt.ylabel('Occurrence of Panic Attacks (Yes=1, No=0)')
plt.legend(title='Panic Attack')
plt.grid(True)

# Étape 5 : Afficher le graphique
plt.show()

#Exercice 4 
# Étape 1 : Importer les bibliothèques nécessaires
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Étape 2 : Préparer les données (supposons que le DataFrame 'df' soit déjà chargé)
# Exemple de données
data = {
    'Age': [18, 19, 20, 21, 22, 23, 24, 25],
    'CGPA': [3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 3.8, 3.7],
    'Depression': [1, 0, 1, 0, 0, 1, 0, 1],
    'Anxiety': [1, 0, 1, 1, 0, 0, 1, 0],
    'Panic Attack': [0, 0, 1, 0, 0, 1, 1, 0]
}
df = pd.DataFrame(data)

# Étape 3 : Créer un pairplot
plt.figure(figsize=(10, 10))
sns.pairplot(df, hue='Depression', diag_kind='kde', palette='Set1')

# Étape 4 : Personnaliser le graphique
plt.suptitle('Pairwise Relationships and Distributions of Students\' Data', y=1.02)

# Afficher le graphique
plt.show()

#Exercice 5 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Exemple de données
data = {
    'Age': [18, 19, 20, 21, 22, 23, 24, 25],
    'CGPA': [3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 3.8, 3.7],
    'Depression': [1, 0, 1, 0, 0, 1, 0, 1],
    'Anxiety': [1, 0, 1, 1, 0, 0, 1, 0],
    'Panic Attack': [0, 0, 1, 0, 0, 1, 1, 0]
}
df = pd.DataFrame(data)

# Calculer la matrice de corrélation
corr_matrix = df.corr()

# Créer et personnaliser la heatmap
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt=".2f")

# Ajouter un titre et ajuster les étiquettes des axes
plt.title('Matrice de Corrélation des Indicateurs de Santé Mentale', fontsize=16)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()

#Exercice 6
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Exemple de données
data = {
    'Age': [18, 19, 20, 21, 22, 23, 24, 25],
    'CGPA': [3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 3.8, 3.7],
    'Depression': [1, 0, 1, 0, 0, 1, 0, 1],
    'Anxiety': [1, 0, 1, 1, 0, 0, 1, 0],
    'Panic Attack': [0, 0, 1, 0, 0, 1, 1, 0]
}
df = pd.DataFrame(data)

# Créer un FacetGrid pour explorer la distribution du CGPA par statut de dépression
g = sns.FacetGrid(df, col="Depression", height=5, aspect=1.2)
g.map(sns.histplot, "CGPA", kde=False, bins=5, color="skyblue")

# Ajouter des titres et des labels
g.set_axis_labels("CGPA", "Count")
g.set_titles(col_template="{col_name} Depression Status")
g.fig.suptitle("Distribution of CGPA Across Different Levels of Depression Status", fontsize=16)
g.fig.subplots_adjust(top=0.85)  # Ajuster l'espacement en haut pour le titre

plt.show()

