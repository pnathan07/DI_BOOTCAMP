# Sets - like lists BUT
# cannot be indexed
# dont hold duplicate values

# When to use:
# 1. all values have to be unique
# 2. when we want to compare between two groups of values/sets of values

a_set = {1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3}

print(a_set)  # {1,2,3}

# a_set[1] # cannot be indexed - returns an Error - need to be converted to a list to do so

b_set = {3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5}  # {3,4,5}

print(a_set.difference(b_set))  # {1,2}
print(b_set.difference(a_set))  # {4,5}

print(a_set.intersection(b_set))  # {3}

print(a_set.union(b_set))  # {1,2,3,4,5}


# lookup - checking if value is inside the data collection
print(1 in a_set)

a_set.add(6)
print(a_set)


# Exercise
a_tuple = (10, 20, 30, 40)

a, b, c, d = a_tuple

print(a)
print(b)
print(c)
print(d)

name, age = "yoss", 33
print(name)
print(age)
