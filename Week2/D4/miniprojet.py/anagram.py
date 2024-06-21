import re
from .anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker('words.txt')

    while True:
        print("\nMenu:")
        print("1. Input a word")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            word = input("Enter a word: ").strip()

            # Validation du mot
            if not word.isalpha():
                print("Error: Only alphabetic characters are allowed.")
                continue

            if ' ' in word:
                print("Error: Only a single word is allowed.")
                continue

            word = word.lower()

            if not checker.is_valid_word(word):
                print(f"Error: '{word}' is not a valid English word.")
                continue

            anagrams = checker.get_anagrams(word)
            anagrams.remove(word)  # Suppression du mot lui-même de la liste des anagrammes

            print(f"\nYOUR WORD: '{word.upper()}'")
            print("This is a valid English word.")
            print("Anagrams for your word:", ", ".join(anagrams))

        elif choice == '2':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
