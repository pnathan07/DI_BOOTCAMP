# Accept input from the user
input_str = input("Enter a comma-separated sequence of words: ")

# Split the input string into a list of words
words = [word.strip() for word in input_str.split(',')]

# Sort the words alphabetically
sorted_words = sorted(words)

# Join the sorted words back into a comma-separated string
output_str = ','.join(sorted_words)

# Print the output string
print("Output:", output_str)

#challeng 2
def longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Initialize variables to store the longest word and its length
    longest = ''
    max_length = 0
    # Iterate over each word in the sentence
    for word in words:
        # Remove any punctuation from the word
        cleaned_word = ''.join(filter(str.isalnum, word))
        # Check if the cleaned word is longer than the current longest word
        if len(cleaned_word) > max_length:
            longest = word
            max_length = len(cleaned_word)
    return longest

# Test the function
print(longest_word("Margaret's toy is a pretty doll."))  # Output: "Margaret's"
print(longest_word("A thing of beauty is a joy forever."))  # Output: "forever."
print(longest_word("Forgetfulness is by all means powerless!"))  # Output: "Forgetfulness"
