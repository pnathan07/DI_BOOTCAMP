import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Définir les paramètres
num_cities = 10
num_months = 12
cities = [f'City_{i+1}' for i in range(num_cities)]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Générer des températures aléatoires entre -5 et 35 degrés Celsius
np.random.seed(0)  # Pour la reproductibilité
temperatures = np.random.uniform(low=-5, high=35, size=(num_cities, num_months))

# Créer un DataFrame
df = pd.DataFrame(temperatures, index=cities, columns=months)

# Afficher les premières lignes du DataFrame
print("DataFrame des températures mensuelles :")
print(df.head())
# Calculer la température moyenne annuelle pour chaque ville
annual_avg_temp = df.mean(axis=1)

# Trouver la ville avec la température moyenne la plus élevée et la plus basse
city_highest_temp = annual_avg_temp.idxmax()
city_lowest_temp = annual_avg_temp.idxmin()

print("\nTempérature moyenne annuelle pour chaque ville :")
print(annual_avg_temp)

print(f"\nVille avec la température moyenne la plus élevée : {city_highest_temp} ({annual_avg_temp[city_highest_temp]:.2f} °C)")
print(f"Ville avec la température moyenne la plus basse : {city_lowest_temp} ({annual_avg_temp[city_lowest_temp]:.2f} °C)")
# Tracer les températures moyennes mensuelles pour chaque ville
plt.figure(figsize=(14, 8))
for city in cities:
    plt.plot(df.columns, df.loc[city], label=city)

plt.xlabel('Mois')
plt.ylabel('Température (°C)')
plt.title('Températures mensuelles pour chaque ville')
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
plt.grid(True)
plt.show()
# Tracer la température moyenne annuelle pour chaque ville
plt.figure(figsize=(10, 6))
annual_avg_temp.plot(kind='bar', color='skyblue')
plt.xlabel('Ville')
plt.ylabel('Température Moyenne Annuelle (°C)')
plt.title('Température Moyenne Annuelle pour chaque Ville')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
