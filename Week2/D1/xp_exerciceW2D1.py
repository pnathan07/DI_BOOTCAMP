#OOP

#Exercice 1 

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
cat1 = Cat("nike", 9)
cat2 = Cat("ozzy", 3)
cat3 = Cat("max", 7)

def find_the_oldest_cat(*cats):
     oldest_cat = max(cats, key=lambda cat: cat.age)
     return oldest_cat
     
oldest_cat = find_the_oldest_cat(cat1,cat2,cat3)
print(f"the oldest cats is {oldest_cat.name} and is {oldest_cat.age}.")     

#Exercice 2 

# Create a class called Dog.
class Dog:

    # In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
    def __init__(self, name: str, height: float) -> None:
        self.name = name
        self.height = height

    # Create a method called bark that prints the following string “<dog_name> goes woof!”.
    def bark(self) -> None:
        print(f"{self.name} goes woof!")

    # Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
    def jump(self) -> None:
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

    def present(self):
        print(f"Dog name: {self.name}. Height: {self.height}")


# def present_dog(dog: Dog) -> None:
#     print(f"Dog name: {dog.name}. Height: {dog.height}")


def get_biggest_dog(dogs: list[Dog]) -> Dog:
    biggest_dog = max(dogs, key=lambda dog: dog.height)
    return biggest_dog


# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
def main():

    david_dog = Dog(name="Rex", height=50)
    # Print the details of his dog (ie. name and height) and call the methods bark and jump.
    david_dog.present()

    sarahs_dog = Dog("Teacup", 20)
    sarahs_dog.present()

    # Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
    biggest_dog = get_biggest_dog([david_dog, sarahs_dog])
    print(f"{biggest_dog.name} is the biggest dog in town")

if __name__ == "__main__": main()
   
   #Exercice 3 
class song :
    def __init__(self,lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_methode(self):
    
        for line in self.lyrics :
         print(line)
stairway = Song([
    "Theres a lady who's sure" 
    "all that glitters is gold"
    "and she s buying a stairway to heaven"])

stairway.sing_me_a_song() 
     
     #Exercice 4 

class Zoo:
    def __init__(self, zoo_name):
       
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        
        print("Les animaux dans le zoo : ", self.animals)

    def sell_animal(self, animal_sold):
        
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        
        sorted_animals = sorted(self.animals)
        grouped_animals = {}
        current_letter = ""
        group_number = 1

        for animal in sorted_animals:
            first_letter = animal[0]
            if first_letter != current_letter:
                current_letter = first_letter
                grouped_animals[group_number] = [animal]
                group_number += 1
            else:
                grouped_animals[group_number - 1].append(animal)
        
        return grouped_animals

    def get_groups(self):
    
        grouped_animals = self.sort_animals()
        for group_number, group in grouped_animals.items():
            print(f"Groupe {group_number} : {group}")

# Création d'une instance de la classe Zoo
ramat_gan_safari = Zoo ("Ramat Gan Safari")

# Appel des méthodes
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.get_animals()

# Vendre un animal
ramat_gan_safari.sell_animal("Baboon")
ramat_gan_safari.get_animals()

# Obtenir les groupes d'animaux
ramat_gan_safari.get_groups()
