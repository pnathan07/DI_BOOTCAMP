# Tuples - like lists BUT
# they are Not Mutable - cannot be changed
# Read only - ideal for storing sensitive data
# Good for storing constant information

a_tuple = ("yossi", 33, "Tel Aviv", "Israel", "0520342")

first_element = a_tuple[0]
last_element = a_tuple[-1]

for element in a_tuple:
    print(element)

print(33 in a_tuple)  # True


b_tuple = (1, 2, 3, 4)

b_tuple = list(b_tuple)
b_tuple.append(5)

b_tuple = tuple(b_tuple)

print(b_tuple)
