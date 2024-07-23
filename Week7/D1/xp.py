#Exercice 1 
import numpy as np

# Créer un tableau NumPy contenant les nombres de 0 à 9
array_1d = np.arange(10)

# Afficher le tableau
print(array_1d)

#Exercice 2 
import numpy as np

# Liste à convertir
list_data = [3.14, 2.17, 0, 1, 2]

# Convertir la liste en tableau NumPy
array_float = np.array(list_data)

# Convertir le type de données en entier
array_int = array_float.astype(int)

# Afficher le tableau
print(array_int)

#Exercice 3 
import numpy as np

# Créer un tableau NumPy avec des valeurs de 1 à 9
array_3x3 = np.arange(1, 10).reshape(3, 3)

# Afficher le tableau
print(array_3x3)


#Exercice 4 
import numpy as np

# Créer un tableau NumPy de forme (4, 5) avec des nombres aléatoires
array_4x5 = np.random.rand(4, 5)

# Afficher le tableau
print(array_4x5)


#Exercice 5 
import numpy as np

# Créer un tableau NumPy 2D
array_2d = np.array([
    [10, 11, 12, 13, 14],
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34]
])

# Sélectionner la deuxième ligne
second_row = array_2d[1]

# Afficher la deuxième ligne
print(second_row)

#Exercice 6 
import numpy as np

# Créer un tableau NumPy 1D
array_1d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Inverser l'ordre des éléments
reversed_array = array_1d[::-1]

# Afficher le tableau inversé
print(reversed_array)


#Exercice 7 
import numpy as np

# Créer une matrice identité 4x4
identity_matrix = np.eye(4)

# Afficher la matrice identité
print(identity_matrix)


#Exercice 8 
import numpy as np

# Créer un tableau 1D
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Calculer la somme des éléments
total_sum = np.sum(array)

# Calculer la moyenne des éléments
average = np.mean(array)

# Afficher les résultats
print(f"Sum: {total_sum}, Average: {average}")

#Exercice 9
 #import numpy as np

# Créer un tableau NumPy avec des éléments de 1 à 20
array = np.arange(1, 21)

# Remodeler le tableau en une matrice 4x5
matrix = array.reshape(4, 5)

# Afficher la matrice
print(matrix)

#Exercice 10 
import numpy as np

# Créer un tableau NumPy d'exemple
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Extraire les nombres impairs
odd_numbers = array[array % 2 != 0]

# Afficher les nombres impairs
print(odd_numbers)
