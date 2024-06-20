file_location = "file_management/file.txt"

# 1. Reading all of the file at once

with open(file_location) as file:
    content = file.read()  # reads all of the file's contents into a single string
    print(content)


with open(file_location) as file:
    content = file.readlines(
        1
    )  # reads all of the file's contents into stribg lines in a single list
    print(content)


# 2. Manual Navigation with Cursor
cursor_location = 231

with open(file_location) as file:

    file.seek(cursor_location)
    print(file.read())

    file.seek(0)  # takes us back to the start of the file

print(cursor_location)
