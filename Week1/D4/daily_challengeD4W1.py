# The given matrix as a string
matrix_str = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

# Split the matrix string into rows
rows = matrix_str.split("\n")

# Transpose the rows to get columns
columns = ["".join(row[i] for row in rows) for i in range(len(rows[0]))]

# Initialize an empty string to store the decrypted message
message = ""

# Loop through each column
for column in columns:
    # Initialize a flag to keep track of whether we are in a group of symbols
    in_symbol_group = False
    # Loop through each character in the column
    for char in column:
        # If the character is alphanumeric, add it to the message
        if char.isalnum():
            message += char
            in_symbol_group = False
        # If the character is a symbol and we are not in a symbol group, add a space to the message
        elif not in_symbol_group:
            message += " "
            in_symbol_group = True

# Print the decrypted message
print("Decrypted message:", message)
