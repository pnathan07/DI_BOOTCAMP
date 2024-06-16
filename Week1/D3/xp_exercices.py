#Dictionaries 

#XP

#Exercice 1 


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

pairs = zip(keys,values)
bails = dict (pairs)

print(bails)

#Exercice 2


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0  


for member, age in family.items(): 
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10  
    else:
        ticket_price = 15
    

    total_cost += ticket_price
    

    print(f"{member.capitalize()} need to pay ${ticket_price}")


print(f"The total cost for the family is ${total_cost}.")

#Exercice 3


brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": ["blue"], "Spain": ["red"], "US": ["pink", "green"]},
}


brand["number_stores"] = 2


clients = ", ".join(brand["type_of_clothes"])
print(f"Zara's clients are: {clients}.")


brand["country_creation"] = "Spain"


if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")


del brand["creation_date"]


print(brand["international_competitors"][-1])


print(brand["major_color"]["US"])


print(len(brand))


print(brand.keys())


more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}


brand.update(more_on_zara)


print(brand["number_stores"])

#Exercice 4

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# Étape 1 : Créer disney_users_A avec une boucle for
disney_users_A = {user: index for index, user in enumerate(users)}
print(disney_users_A)

# Étape 2 : Créer disney_users_B avec une boucle for
disney_users_B = {index: user for index, user in enumerate(users)}
print(disney_users_B)

# Étape 3 : Créer disney_users_C en triant par ordre alphabétique
disney_users_C = {user: index for index, user in enumerate(sorted(users))}
print(disney_users_C)

# Étape 4 : Recréer disney_users_A pour les noms contenant la lettre "i"
disney_users_A_i = {user: index for index, user in enumerate(users) if "i" in user}
print(disney_users_A_i)

# Étape 5 : Recréer disney_users_A pour les noms commençant par "M" ou "P"
disney_users_A_mp = {user: index for index, user in enumerate(users) if user.startswith(('M', 'P'))}
print(disney_users_A_mp)





  