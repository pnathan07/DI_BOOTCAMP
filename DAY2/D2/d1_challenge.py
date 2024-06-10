# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

user_input = input("Provide a 10 character long input: ")

if (len(user_input) < 10):
    print("string not long enough")

elif (len(user_input) > 10):
    print("string too long")

else:
    print("perfect string")
    first_character = user_input[0]
    last_character = user_input[-1] # or 9
    
    print(f"First Char: {first_character}")
    print(f"Last Char: {last_character}")

    # range(0, 9) -> 0, 1, 2, 3... 9
    
    # Example 1: using an outer variable output_string
    output_string = ""
    for i in range(0, len(user_input)):
        output_string += user_input[i] 
        print(output_string)
        
    # Example 2: string slicing
    for i in range(0, len(user_input)+1): # 0:9(exluded) 0...9
        print(user_input[:i]) # 0:0, 0:1, 0:2, 0:3, 0:4...0:9(exluded)

    # Example 3: looping through the string
    output_string = ""
    for char in user_input: # H e l l o ... 
        output_string += char
        print(output_string)

# Then, print the first and last characters of the given text.


# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "HelloWorld"
# Then, you have to construct the string character by character
# H i = 0
# He i = 1
# Hel i =2 
# ... etc
# HelloWorld