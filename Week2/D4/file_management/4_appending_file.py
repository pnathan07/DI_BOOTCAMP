file_location = "file_management/file2.txt"

new_content = "\nTHIS IS A NEW LINE TO ADD"

with open(file_location, mode="a") as file:  # 'a' means append to the end of the file
    file.write(new_content)
