dict1 = {"Name": "Yossi", "Residence": "tel aviv"}


# Looping through the keys
for key in dict1:
    print(key)

# Looping through the values
for value in dict1.values():
    print(value)

# Looping through the keys and values
for key, value in dict1.items():
    print(key, value)

dict2 = {"Name": "Hen"}
dict3 = {"Name": "Ron"}

dictionaries = [dict1, dict2, dict3]

for dictionary in dictionaries:
    print(f"Hello {dictionary["Name"]}!")

# 11:25