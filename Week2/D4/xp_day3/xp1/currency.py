#Exercice 1
from typing import Union, Self


class Currency:
    def __init__(self, currency: str, amount: int):
        self.currency = currency
        self.amount = amount

    def __str__(self) -> str:
        if self.amount > 1:
            return f"{self.amount} {self.currency}s"
        else:
            return f"{self.amount} {self.currency}"

    def __repr__(
        self,
    ) -> (
        str
    ):  # when we want to present the object when it is inside a collection (like a list)
        if self.amount > 1:
            return f"{self.amount} {self.currency}s"
        else:
            return f"{self.amount} {self.currency}"

    def __add__(
        self, other: Union["Currency", int]
    ) -> "Currency":  # Union(python ~3.6) == |(python v3.10)
        # isinstance - function for checking the type of the variable
        if isinstance(other, Currency):
            if other.currency == self.currency:
                return Currency(self.currency, self.amount + other.amount)
            else:
                raise ValueError(
                    f"Cannot add between Currency type {self.currency} and {other.currency}"
                )
        elif isinstance(other, int):
            return Currency(self.currency, self.amount + other)

    def __iadd__(self, other: Union["Currency", int]) -> Self:
        """Method for adding/updating the amount of the calling Currency object (i.e Self)"""
        if isinstance(other, Currency):
            self.amount += other.amount
        elif isinstance(other, int):
            self.amount += other
        return self


def main():
    c1 = Currency("dollar", 5)
    c2 = Currency("dollar", 10)
    c3 = Currency("shekel", 1)
    c4 = Currency("shekel", 10)

    # print(c1)

    currencies = [c1, c2, c3, c4]

    # print(c1 + c2)

    c3 += 5

    print(c3)


if __name__ == "__main__":
    main()

#Exercice 2 

# func.py

def sum_two_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")
# exercise_one.py

# Import de la fonction depuis func.py
from func import sum_two_numbers

# Appel de la fonction avec deux nombres
sum_two_numbers(3, 5)

#Exercice 3 
import string
import random

def generate_random_string(length=5):
    letters = string.ascii_letters  # Contient 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(letters) for i in range(length))

# Générer une chaîne de caractères aléatoire de longueur 5
random_string = generate_random_string()
print(f"Random String of length 5: {random_string}")

#Exercice 4
import datetime

def display_current_date():
    current_date = datetime.date.today()
    print(f"Today's date is: {current_date}")

# Appeler la fonction pour afficher la date actuelle
display_current_date()

#Exercice 5
import datetime

def time_until_new_year():
    # Obtenir la date et l'heure actuelles
    now = datetime.datetime.now()
    
    # Déterminer la prochaine année
    next_year = now.year + 1 if now.month == 12 and now.day == 31 else now.year
    
    # Créer un objet datetime pour le 1er janvier de l'année suivante
    new_year = datetime.datetime(next_year, 1, 1)
    
    # Calculer le temps restant
    time_left = new_year - now
    
    # Afficher le temps restant
    print(f"The 1st of January is in {time_left.days} days and {time_left.seconds//3600} hours, {(time_left.seconds//60)%60} minutes, and {time_left.seconds%60} seconds.")

# Appeler la fonction pour afficher le temps restant jusqu'au 1er janvier
time_until_new_year()

#Exercice 6
import datetime

def minutes_lived(birthdate):
    # Convertir la date de naissance en objet datetime
    birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d')
    
    # Obtenir la date et l'heure actuelles
    now = datetime.datetime.now()
    
    # Calculer la différence en minutes
    time_lived = now - birthdate
    minutes_lived = time_lived.total_seconds() // 60
    
    # Afficher le nombre de minutes vécues
    print(f"You have lived approximately {int(minutes_lived)} minutes.")

# Exemple d'appel de la fonction
birthdate = '1990-01-01'  # Format AAAA-MM-JJ
minutes_lived(birthdate)
