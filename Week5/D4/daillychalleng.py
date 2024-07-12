from sklearn.preprocessing import MinMaxScaler

# Supposons que 'df' est votre DataFrame contenant les données

# Initialiser le scaler pour la Min-Max Normalization
scaler = MinMaxScaler()

# Normaliser la colonne 'salary'
df['salary_normalized'] = scaler.fit_transform(df[['salary']])

# Afficher les premières lignes du DataFrame avec la colonne normalisée
print("DataFrame with Normalized Salary:")
print(df[['salary', 'salary_normalized']].head())
from sklearn.decomposition import PCA

# Supposons que 'df' est votre DataFrame avec des caractéristiques numériques

# Sélectionner les colonnes numériques pour l'ACP
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Créer un objet PCA
pca = PCA(n_components=2)  # Réduire à 2 dimensions pour l'exemple

# Appliquer PCA aux données numériques
df_pca = pca.fit_transform(df[numeric_columns])

# Créer un nouveau DataFrame avec les composantes principales
df_pca = pd.DataFrame(data=df_pca, columns=['PCA1', 'PCA2'])

# Concaténer les composantes principales avec les autres colonnes du DataFrame d'origine si nécessaire
df_final = pd.concat([df, df_pca], axis=1)

# Afficher les premières lignes du DataFrame avec les composantes principales ajoutées
print("DataFrame with PCA Components:")
print(df_final.head())
# Supposons que vous avez une colonne 'experience_level' dans votre DataFrame 'df'

# Calculer les salaires moyens et médians par niveau d'expérience
df_agg = df.groupby('experience_level').agg({'salary': ['mean', 'median']})

# Renommer les colonnes agrégées pour plus de clarté
df_agg.columns = ['average_salary', 'median_salary']

# Afficher les statistiques par niveau d'expérience
print("Average and Median Salaries by Experience Level:")
print(df_agg)
