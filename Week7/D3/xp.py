#Exercice 1 
import scipy
import scipy.__version__

print("SciPy version:", scipy.__version__)

#Exercice 2 
import numpy as np
from scipy import stats

# Sample dataset
data = [12, 15, 13, 12, 18, 20, 22, 21]

# Calculer la moyenne
mean = np.mean(data)
print(f'Mean: {mean}')

# Calculer la médiane
median = np.median(data)
print(f'Median: {median}')

# Calculer la variance
variance = np.var(data, ddof=1)  # ddof=1 pour obtenir la variance de l'échantillon
print(f'Variance: {variance}')

# Calculer l'écart type
std_deviation = np.std(data, ddof=1)  # ddof=1 pour obtenir l'écart type de l'échantillon
print(f'Standard Deviation: {std_deviation}')


#Exercice 3 
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Paramètres de la distribution normale
mean = 50
std_deviation = 10

# Générer des données
data = np.linspace(mean - 4*std_deviation, mean + 4*std_deviation, 1000)
pdf = norm.pdf(data, mean, std_deviation)

# Tracer la distribution
plt.figure(figsize=(10, 6))
plt.plot(data, pdf, label='Distribution normale')
plt.title('Distribution normale (moyenne = 50, écart type = 10)')
plt.xlabel('Valeur')
plt.ylabel('Densité de probabilité')
plt.legend()
plt.grid(True)
plt.show()


#Exercice 4
import numpy as np
from scipy import stats

# Générer deux ensembles de données aléatoires
np.random.seed(0)  # Pour la reproductibilité des résultats
data1 = np.random.normal(loc=50, scale=10, size=100)
data2 = np.random.normal(loc=55, scale=12, size=100)

# Effectuer un test T indépendant
t_stat, p_value = stats.ttest_ind(data1, data2)

# Afficher les résultats
print("Ensemble de données 1:")
print(data1)
print("\nEnsemble de données 2:")
print(data2)
print("\nTest T:")
print(f"Statistique t: {t_stat}")
print(f"Valeur p: {p_value}")


#Exercice 5 
import pandas as pd
import seaborn as sns
from scipy import stats

# Charger le dataset Iris en utilisant seaborn
df = sns.load_dataset('iris')

# Afficher les premières lignes du dataset
print(df.head())

# Calculer les statistiques descriptives pour la colonne 'sepal_length'
sepal_length = df['sepal_length']

mean = sepal_length.mean()
median = sepal_length.median()
variance = sepal_length.var()
std_dev = sepal_length.std()

# Afficher les statistiques descriptives
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")

# Utiliser SciPy pour calculer les statistiques descriptives
mean_scipy = stats.tmean(sepal_length)
median_scipy = stats.scoreatpercentile(sepal_length, 50)
variance_scipy = stats.tvar(sepal_length)
std_dev_scipy = stats.tstd(sepal_length)

# Afficher les statistiques descriptives calculées avec SciPy
print(f"\nSciPy Mean: {mean_scipy}")
print(f"SciPy Median: {median_scipy}")
print(f"SciPy Variance: {variance_scipy}")
print(f"SciPy Standard Deviation: {std_dev_scipy}")


#Exercice 6 
import numpy as np
from scipy.stats import kurtosis, skew
import matplotlib.pyplot as plt

# Générer un dataset aléatoire avec une distribution normale
data = np.random.normal(0, 1, 1000)

# Calculer la skewness (asymétrie)
data_skewness = skew(data)
print(f"Skewness: {data_skewness}")

# Calculer la kurtosis (kurtose)
data_kurtosis = kurtosis(data)
print(f"Kurtosis: {data_kurtosis}")

# Visualiser la distribution des données
plt.hist(data, bins=30, edgecolor='k', alpha=0.7)
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()



