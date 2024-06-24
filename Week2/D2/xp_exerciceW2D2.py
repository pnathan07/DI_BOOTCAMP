#Exercice 1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Instances des races de chat
bengal_cat = Bengal("Bengie", 3)
chartreux_cat = Chartreux("Charley", 2)
siamese_cat = Siamese("Simba", 1)

# Liste des chats
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Instance de la classe Pets pour Sara
sara_pets = Pets(all_cats)

# Promener tous les chats
sara_pets.walk()


#Exercice 2-3
# dog.py

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_strength = self.run_speed() * self.weight
        other_strength = other_dog.run_speed() * other_dog.weight

        if my_strength > other_strength:
            return f"{self.name} won the fight!"
        elif my_strength < other_strength:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a tie!"


from  dog import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join([dog.name for dog in args])
        print(f"{self.name}, {dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))

#Exercice 4
  # family.py

class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family on the birth of {kwargs['name']}!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"The {self.last_name} family:")
        for member in self.members:
            print(member)

# test_family.py

from family import Family

# Define initial members
members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
 ]

# Create a Family instance
my_family = Family(last_name="Smith", members=members)

# Test the family_presentation method
my_family.family_presentation()

# Test the born method
my_family.born(name='John', age=0, gender='Male', is_child=True)

# Test the family_presentation method again to see the new member
my_family.family_presentation()

# Test the is_18 method
print(my_family.is_18('Michael'))  # Output: True
print(my_family.is_18('Sarah'))    # Output: True
print(my_family.is_18('John'))     # Output: False

#Exercice 5 

# the_incredibles.py
[
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]


from family import Family

class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)
        for member in self.members:
            if 'power' not in member or 'incredible_name' not in member:
                raise ValueError("Each member must have 'power' and 'incredible_name' attributes")

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['name']}'s power is {member['power']}")
                else:
                    raise Exception(f"{name} is not over 18 years old")
                return
        raise Exception(f"No member found with the name {name}")

    def incredible_presentation(self):
        print("*Here is our powerful family*")
        super().family_presentation()

# test_the_incredibles.py

from the_incredibles import TheIncredibles

# Define initial members
members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

# Create an instance of TheIncredibles
incredibles_family = TheIncredibles(last_name="Incredibles", members=members)

# Test the incredible_presentation method
incredibles_family.incredible_presentation()

# Test the use_power method
try:
    incredibles_family.use_power('Michael')
    incredibles_family.use_power('Sarah')
    incredibles_family.use_power('Baby Jack')  # This should raise an exception
except Exception as e:
    print(e)

# Use the born method to add Baby Jack
incredibles_family.born(name='Baby Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='JackJack')

# Test the incredible_presentation method again to see the new member
incredibles_family.incredible_presentation()

