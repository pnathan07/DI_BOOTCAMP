file_location = "file_management/file.txt"


contents = ""

# read the contents of the file into the contents variable
with open(file_location) as file:
    contents = file.readlines()

print(contents)

# Insert 'C' into the incomplete contents ['A\n', 'B\n', '\n', 'D\n', 'E']
contents[2] = "C\n"

print(contents)

# write the new contents list into the file
with open(file_location, mode="w") as file:
    file.writelines(contents)
