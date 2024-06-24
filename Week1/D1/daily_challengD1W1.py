# Ask the user for a string
user_input = input("Enter a 10-character string: ")

# Check the length of the string
if len(user_input) < 10:
    print("String not long enough")
elif len(user_input) > 10:
    print("String too long")
else:
    print("Perfect string")

# Print the first and last characters
print("First character:", user_input[0])
print("Last character:", user_input[-1])

# Construct the string character by character
for i in range(len(user_input)):
    print(user_input[:i+1])
