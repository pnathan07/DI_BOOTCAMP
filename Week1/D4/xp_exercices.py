#Functions XP

#Exercice 1 

def display_message():
    print("i learn python")
display_message()
 
#Exercice 2

def favorit_book(title):
   print(f"One of my favorit book is {title}.")
favorit_book("La Reussite")

#Exercice 3
def describe_city(name,contry):
    print(f"{name} is in {contry}.")
describe_city("Paris","France")


#Exercice 4

import random

def compare_number(user_number):
    if not (1 <= user_number <= 100):
        print("The number is not on the list")
        return

    random_number = random.randint(1, 100)
    
    if random_number == user_number:
        print(f"Success! The two numbers are {user_number}.")
    else:
        print(f"Error. Your number is {user_number}, but the random number is {random_number}.")


compare_number(50)

#Exercice 5

def make_shirt(size, message):
    print(f"The size of the shirt is {size} and the text is '{message}'.")

make_shirt("large", "I love Python")

make_shirt("medium", "I love Python")

make_shirt("small", "Hello, World!")

#Exercice 6 


magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    for magician in magician_names:
        print(magician)

def make_great():
    global magician_names
    magician_names = [f"{magician} the Great" for magician in magician_names]

make_great()

show_magicians()

#Exercice 7


import random

def get_random_temp(season):
    if season.lower() == 'winter':
        return random.randint(-10, 16)
    elif season.lower() == 'spring' or season.lower() == 'autumn' or season.lower() == 'fall':
        return random.randint(-5, 23)
    elif season.lower() == 'summer':
        return random.randint(16, 40)
    else:
        return random.randint(-10, 40)

def main():
    season = input("Enter the current season (summer, autumn, winter, spring): ")
    temperature = get_random_temp(season)
    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temperature < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temperature < 24:
        print("Nice weather, enjoy your day!")
    elif 24 <= temperature < 32:
        print("Getting warm, stay hydrated.")
    else:
        print("Hot day! Keep cool.")

main()

