# Exercice 1
# Créer un ensemble avec vos numéros favoris
my_fav_numbers = {7, 14, 21}  # Exemple de numéros favoris

# Ajouter deux nouveaux numéros à l'ensemble
my_fav_numbers.add(28)
my_fav_numbers.add(35)

# Supprimer le dernier numéro ajouté (dans les ensembles, il n'y a pas d'ordre, donc on enlève un élément arbitrairement)
my_fav_numbers.remove(35)

# Créer un ensemble avec les numéros favoris de votre ami
friend_fav_numbers = {5, 10, 15}

# Concaténer les deux ensembles pour créer un nouvel ensemble
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print("My favorite numbers:", my_fav_numbers)
print("Friend's favorite numbers:", friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)

# Exercice 2

tupple_original = (1,2,3,4,5)
nouvaux_integer = (6,7)
nouveaux_bail = tupple_original + nouvaux_integer 
print("tupple_original",tupple_original)
print("nouveaux_bail",nouveaux_bail)


# Exercice 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]


basket.remove("Banana")

# Supprimer "Blueberries" de la liste
basket.remove("Blueberries")

# Ajouter "Kiwi" à la fin de la liste
basket.append("Kiwi")

# Ajouter "Apples" au début de la liste
basket.insert(0, "Apples")

# Compter combien de pommes ("Apples") sont dans le panier
apple_count = basket.count("Apples")

# Vider le panier
basket.clear()

# Afficher le panier vide et le nombre de pommes comptées
print("Panier après modifications et vidage:", basket)
print("Nombre de pommes dans le panier:", apple_count)

# Exercice 4

sequence = [x*0.5 for x in range(3,11)]

print(sequence)

# Exercice 5

for i in range(1,21) :
#    print(i)
    
    if (i-1) % 2 == 0 :
       print(i)

# Exercice 6