import json

file_location = "json_files/data.json"

# Reading a json string
with open(file_location) as file:
    contents_str = file.read()  # returns a json string
    contents_dict = json.loads(contents_str)  # json.loads reads a json string
    print(type(contents_dict))

# Reading a json file
with open(file_location) as file:
    contents_dict = json.load(file)  # json.load reads a json file
    print(contents_dict)
    print(type(contents_dict))
