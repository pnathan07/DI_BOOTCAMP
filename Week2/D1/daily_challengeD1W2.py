class Farm:
    def __init__(self, farm_name):
        """
        Constructeur qui initialise le nom de la ferme et un dictionnaire pour stocker les animaux.
        :param farm_name: Nom de la ferme.
        """
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        """
        Ajoute un ou plusieurs animaux de type spécifié à la ferme.
        :param animal_type: Type d'animal à ajouter.
        :param count: Nombre d'animaux à ajouter (par défaut 1).
        """
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_animal_types(self):
        """
        Retourne une liste triée des types d'animaux dans la ferme.
        :return: Liste triée des types d'animaux.
        """
        return sorted(self.animals.keys())

    def get_short_info(self):
        """
        Retourne une chaîne de caractères décrivant les types d'animaux dans la ferme.
        :return: Description courte de la ferme.
        """
        animal_types = self.get_animal_types()
        plural_animals = [animal + 's' for animal in animal_types]
        return f"{self.name}'s farm has " + ", ".join(plural_animals) + "."

    def get_animals(self):
        """
        Imprime tous les animaux de la ferme avec leur nombre.
        """
        for animal, count in self.animals.items():
            print(f"{animal}: {count}")

# Création d'une instance de la classe Farm
mcdonald_farm = Farm("McDonald")

# Ajout d'animaux
mcdonald_farm.add_animal("cow", 5)
mcdonald_farm.add_animal("sheep", 2)
mcdonald_farm.add_animal("goat", 12)
mcdonald_farm.add_animal("sheep", 1)  # Ajout supplémentaire de moutons

# Afficher les animaux de la ferme
mcdonald_farm.get_animals()

# Obtenir une liste triée des types d'animaux
print(mcdonald_farm.get_animal_types())

# Obtenir une description courte de la ferme
print(mcdonald_farm.get_short_info())
