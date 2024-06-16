# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).

user_input_fruits = input(
    "Please provide the names of your favorite fruits, separated by a blank space: "
)

fruits = user_input_fruits.split(" ")
# Now that we have a list of fruits, ask the user to input a name of any fruit.

user_input_fruit = input("Please provide a name of a fruit: ")

# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.

if user_input_fruit in fruits:
    print("You chose one of your favorite fruits! Enjoy!")

# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
else:
    print("You chose a new fruit. I hope you enjoy")
