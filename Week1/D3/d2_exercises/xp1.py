# Create a set called my_fav_numbers with all your favorites numbers.
my_fav_numbers = {1, 2, 3, 4, 5, 5, 5}  # -> {1,2,3,4,5}

# Add two new numbers to the set.
my_fav_numbers.add(6)
my_fav_numbers.add(7)  # -> {1,2,3,4,5,6,7}

# Remove the last number.

# my_fav_numbers.pop() # not a good option since it removes a randomly.
# OPTION 1 - use the remove method
# my_fav_numbers.remove(7)

# OPTION 2 - use the discard method
# my_fav_numbers.discard()

# OPTION 3 (bad) - convert the set into a list and use the pop() method
my_fav_numbers = list(my_fav_numbers)
# print(my_fav_numbers)
my_fav_numbers.pop()  # removes the last element inside the list
my_fav_numbers = set(my_fav_numbers)

# Create a set called friend_fav_numbers with your friend’s favorites numbers.
friend_fav_numbers = {2, 3, 5, 7, 8, 9}

# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers) # -> {1, 2, 3, 4, 5, 6, 7, 8, 9}
