file_location = "file_management/file2.txt"

content1 = "Hi My name is .... Today is ....\n"
content2 = "Blah Blah ..."
content = content1 + "\n" + content2

with open(file_location, mode="w") as file:  # mode "w"(write) - overwrites the file
    file.write(content)  # writes a single string into the file


contents = [content1, content2] # list of strings

with open(file_location, mode="w") as file:  # mode "w"(write) - overwrites the file
    file.writelines(contents) # write a list of strings into the file 
