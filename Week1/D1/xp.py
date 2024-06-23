# Exercice 1 
print('\n'.join(['Hello world']*4))

#Exercice 2
result = (99 ** 3) * 8
print(result)

#Exercice 3
print(5 < 3)           # False
print(3 == 3)          # True
print(3 == "3")        # False
print("3" > str(3))    # True
print("Hello" == "hello")  # False

#Exercice 4 
computer_brand = "Dell"
print(f"I have a {computer_brand} computer.")

#Exercice 5 
name = "Alice"
age = 30
shoe_size = 8
info = f"My name is {name}, I am {age} years old, and my shoe size is {shoe_size}."
print(info)

#Exercice 6 
a = 10
b = 5
if a > b:
    print("Hello World")

#Exercice 7 
# Demander à l'utilisateur d'entrer un nombre
number = int(input("Entrez un nombre : "))

# Vérifier si le nombre est pair ou impair
if number % 2 == 0:
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")

#Exercice 8 
# Votre nom
your_name = "John"  # Remplacez "John" par votre nom

# Demander à l'utilisateur son nom
user_name = input("Entrez votre nom : ")

# Vérifier si l'utilisateur a le même nom que vous
if user_name.lower() == your_name.lower():
    print("Oh, nous avons le même nom ! Nous sommes destinés à être des amis !")
else:
    print(f"Désolé {user_name}, mais j'ai déjà un ami avec votre nom !")

#Exercice 9
# Demander à l'utilisateur sa taille en centimètres
height = float(input("Quelle est votre taille en centimètres ? "))

# Vérifier si l'utilisateur est assez grand pour monter
if height > 145:
    print("Vous êtes assez grand pour monter !")
else:
    print("Vous devez grandir un peu plus pour monter.")
