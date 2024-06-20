class Text:
    def __init__(self, text):
        self.text = text.lower()  # Stocker le texte en minuscules pour rendre les comptages insensibles à la casse
        self.words = self.text.split()  # Diviser le texte en mots

    def word_frequency(self, word):
        """Renvoie la fréquence d'un mot dans le texte."""
        word = word.lower()
        frequency = self.words.count(word)
        if frequency > 0:
            return frequency
        else:
            return f"'{word}' n'apparaît pas dans le texte."

    def most_common_word(self):
        """Renvoie le mot le plus commun dans le texte."""
        from collections import Counter
        word_counts = Counter(self.words)
        most_common = word_counts.most_common(1)
        if most_common:
            return most_common[0][0]  # Renvoie le mot le plus commun
        else:
            return "Aucun mot trouvé dans le texte."

    def unique_words(self):
        """Renvoie une liste de tous les mots uniques dans le texte."""
        unique = set(self.words)
        return list(unique)

# Exemple d'utilisation:
text = "A good book would sometimes cost as much as a good house."
text_instance = Text(text)

# Fréquence d'un mot
print(text_instance.word_frequency("good"))  # Sortie: 2
print(text_instance.word_frequency("bad"))   # Sortie: "'bad' n'apparaît pas dans le texte."

# Mot le plus commun
print(text_instance.most_common_word())  # Sortie: 'a' (ou 'good', selon la méthode de comptage)

# Liste des mots uniques
print(text_instance.unique_words())  # Sortie: ['a', 'good', 'book', 'would', 'sometimes', 'cost', 'as', 'much', 'house.']

class Text:
    def __init__(self, text):
        self.text = text.lower()
        self.words = self.text.split()

    def word_frequency(self, word):
        word = word.lower()
        frequency = self.words.count(word)
        if frequency > 0:
            return frequency
        else:
            return f"'{word}' n'apparaît pas dans le texte."

    def most_common_word(self):
        from collections import Counter
        word_counts = Counter(self.words)
        most_common = word_counts.most_common(1)
        if most_common:
            return most_common[0][0]
        else:
            return "Aucun mot trouvé dans le texte."

    def unique_words(self):
        unique = set(self.words)
        return list(unique)

    @classmethod
    def from_file(cls, file_path):
        """Crée une instance de Text à partir d'un fichier texte."""
        with open(file_path, 'r') as file:
            text = file.read()
        return cls(text)

# Utilisation de la méthode from_file:
text_instance_from_file = Text.from_file('the_stranger.txt')

# Fréquence d'un mot dans le fichier
print(text_instance_from_file.word_frequency("stranger"))

# Mot le plus commun dans le fichier
print(text_instance_from_file.most_common_word())

# Liste des mots uniques dans le fichier
print(text_instance_from_file.unique_words())
