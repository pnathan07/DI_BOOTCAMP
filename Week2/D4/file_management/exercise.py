# Read the file line by line V


file_location = "file_management/star_wars.txt"

contents = ""

with open(file_location) as file:
    contents = file.read()

contents_list = contents.split(
    "\n"
)  # # Read all the file and return it as a list of strings. Then split each word


print(contents_list[4])  # Read only the 5th line of the file V


with open(file_location) as file:  # Read only the 5 first characters of the file
    chars = file.read(5)
    print("First 5 chars: ", chars)


# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
## OPTION 1 - use dict + loop
# character_count = {"Darth": 0, "Luke": 0, "Lea": 0}

# for character in contents_list:
#     character_count[character] += 1

# print(character_count)

## OPTION 2 - Use the Counter class

from collections import Counter

character_counter = Counter(contents_list)

print(character_counter)


# Append your first name at the end of the file
with open(file_location, mode="a") as file:
    file.write("\nYossi")


# Append "SkyWalker" next to each first name "Luke"
for i, character in enumerate(contents_list):  # (0, "Darth"), (1, "Luke")
    if character == "Luke":
        contents_list[i] += " SkyWalker"


star_wars_str = "\n".join(contents_list) 

print(star_wars_str)

with open(file_location, mode="w") as file:
    file.write(star_wars_str)
