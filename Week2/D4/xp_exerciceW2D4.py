#Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

#Hint : The generated sentences do not have to make sense.

#Download this word list

#Save it in your development directory.

#Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

#Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
#use the words list to get your random words.
#the amount of words should be the value of the length parameter

import random

def charger_liste_mots(chemin_fichier):
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        mots = fichier.read().splitlines()
    return mots

def generer_phrase(liste_mots, longueur):
    return ' '.join(random.choice(liste_mots) for _ in range(longueur))

def main():
    # Charger la liste de mots
    mots = charger_liste_mots('mots.txt')
    
    # Demander à l'utilisateur la longueur souhaitée de la phrase
    while True:
        try:
            longueur_phrase = int(input("Quelle devrait être la longueur de la phrase? "))
            if longueur_phrase > 0:
                break
            else:
                print("Veuillez entrer un entier positif.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    # Générer la phrase aléatoire
    phrase = generer_phrase(mots, longueur_phrase)
    
    # Afficher la phrase générée
    print(f"Phrase générée: {phrase}")

if __name__ == "__main__":
    main()

#Exercice 2
import json

# Étape 1 : Charger la chaîne JSON
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

# Étape 2 : Accéder à la clé "salary"
salary = data["company"]["employee"]["payable"]["salary"]
print(f"Le salaire est : {salary}")

# Étape 3 : Ajouter la clé "birth_date"
data["company"]["employee"]["birth_date"] = "1990-01-01"

# Étape 4 : Enregistrer le dictionnaire modifié dans un fichier JSON
with open('modified_sample.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Le fichier JSON modifié a été enregistré sous 'modified_sample.json'.")


