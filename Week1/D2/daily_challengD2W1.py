#challenge 1 
# Ask the user for a number and a length
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

# Create a list of multiples of the number
multiples = [number * i for i in range(1, length + 1)]

# Print the list
print(multiples)

#challenge 2 
# Ask the user for a string
word = input("Enter a word: ")

# Remove consecutive duplicates
new_word = ""
prev_char = None
for char in word:
    if char != prev_char:
        new_word += char
    prev_char = char

# Print the new string
print(new_word)
