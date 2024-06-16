word = 'dodo'

dictionary = {}
# langth = 0

for index, letter in enumerate(word):
    if letter in dictionary:
        dictionary[letter].append(index)
    else:
        dictionary[letter] = [index]

print(dictionary)


letters = ["a","y","g","t","z"]

# letters.sort(reverse=True)
# print(letters)

sorted_letters = sorted(letters)
print(sorted_letters)
print(letters)

# sort()
# sorted()
