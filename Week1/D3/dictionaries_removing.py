personal_information_yossi = {
    "Name": "Yossi",
    "Residence": "Tel Aviv",
    "Age": 33,
}

# Option 1 - use pop to remove a key+value and return the removed value
residence = personal_information_yossi.pop("Residence")

print(personal_information_yossi)

print(residence)

# Option 2 - Use del to directly delete the key-value
del personal_information_yossi["Age"]

print(personal_information_yossi)
