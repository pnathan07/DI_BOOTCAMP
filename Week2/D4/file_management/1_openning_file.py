# Manual approach - manually openning and closing

file_location = "file_management/file.txt"
file = open(file_location)

"""DO SOMETHING HERE"""

file.close()

# Context Manager approach - automatically closes the file Stream
with open(
    file_location
) as file:  # context manager - it opens the file and closes it (automatically)
    """DO SOMETHING HERE"""

# File is closed after performing the operations inside the context manager
