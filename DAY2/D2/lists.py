# List - Array

# can store any type of values
# a sequence and can be indexed (like with strings)
# mutable

a_list = ["a", 120, ["b", 12]]

print(len(a_list))

print(a_list[0])
print(a_list[-1])

inner_list = a_list[-1]

print(inner_list)
print(inner_list[0], inner_list[-1])

numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
]  # Important : store same type of values inside the list

# sum = 0
# for number in numbers:
#     sum += number

# print(sum)

numbers_sum = sum(numbers)
print(numbers_sum)


# slicing example
print(numbers[0:5])


# Mutable - can change and be updated

letters = ["a", "b", "x", "d", "e"]

# updating in-place - update the list directly

letters[2] = "c"

print(letters)

# adding - append method
letters.append("f")

print(letters)

# removing - remove method
letters.remove("a")

print(letters)

# insert - inserts a value at a specific index

letters_b = [
    "a",
    "c",
]
letters_b.insert(1, "b")

print(letters_b)


# list concatenation
numbers_a = [1, 2, 3]
numbers_b = [4, 5, 6]

numbers_c = numbers_a + numbers_b
print(numbers_c)


# Exercise
list1 = [5, 10, 15, 20, 25, 50, 20]

# Example 1: for loop (with range)
# for i in range(len(list1)):
#     if list1[i] == 20:
#         list1[i] *= 10
#         break

# print(list1)

# Example 2: for loop (with enumerate)
# Enumerate produces the index and value pairs for the sequence
for i, value in enumerate(list1):
    if value == 20:
        list1[i] *= 10
        break

print(list1)


# Example 3: using the index method

list2 = [5, 10, 15, 20, 25, 50, 20]

first_location_20 = list2.index(20)

list2[first_location_20] *= 10

print(list2)
