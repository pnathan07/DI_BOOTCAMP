#Learned topics:

# Inheritance
# overwriting methods (polymorphism)
# init() in inheritance
# super() for adding the parent attributs
# super().__init__ and Parent.__init__() are the same
# multiple inheritance


class Parent:
    def speak(self):
        return 'parent speaking'
    
class Child(Parent):
    def speak(self):
        return 'Child is now speaking'

class Grandchild(Child):
    pass

obj1 = Grandchild()
print(obj1.speak())

class Animal:
    def __init__(self, name:str, family:str, legs:int) -> None:
        self.name = name
        self.family = family
        self.legs = legs

    def make_sound(self):
        return f'{self.name} is making a sound from Animal class'
    
class Dog(Animal):
    def __init__(self, name, family, legs, trained:bool):
        super().__init__(name,family, legs)
        self.trained = trained

    # def make_sound(self):
    #     # return f'{self.name} is barking'
    #     return f'making sound from Dog class'

class Alien:
    def __init__(self,name, planet):
        self.name = name
        self.planet = planet

    def fly(self):
        return f'{self.name} is flying around'
    
    def sleep(self):
        return f'{self.name} is sleeping'
    
    def make_sound(self):
        return f'{self.name} is making a sound from Alien'


class AlienDog(Dog, Alien):
    def __init__(self, name, family, legs, trained: bool, planet):
        Dog.__init__(self, name, family, legs, trained)
        Alien.__init__(self, name, planet)

        


aliendog1 = AlienDog('Fluffy', 'Canadea', 4, True, 'Saturn')   

print(aliendog1.fly())
print(aliendog1.make_sound())

# print(aliendog1.__dict__)


# animal1 = Dog('Rex', 'Canidae', 4, True)
# print(animal1.make_sound())
        