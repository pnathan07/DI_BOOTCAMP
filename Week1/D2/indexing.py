a_string = "A string"

# Single indexing 

print(a_string[0])

print(len(a_string))

length_a_string = len(a_string) # 8

print(a_string[length_a_string - 1])

print(a_string[-1]) # last element

letter_s = a_string[2]

print(letter_s)


# Slicing

b_string = "Holla There"

# [start:end(excluded)]

# 0:5(value inside index 5 wont be included)

word_holla = b_string[0:5]

print(word_holla)

word_holla = b_string[:5]

print(word_holla)

word_there = b_string[-5:]

print(word_there)

