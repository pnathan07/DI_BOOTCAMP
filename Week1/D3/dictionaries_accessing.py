personal_information_yossi = {
    "Name": "Yossi",
    "Residence": "Tel Aviv",
    "Age": 33,
}

personal_information_hen = {
    "Name": "Hen",
    "Residence": "Paris",
    "Age": 45,
    "Phone_number": "+9725454545454",
}

name = personal_information_yossi["Name"] # get the value assumin there's such (Name) key
print(name)


phone_number_yossi = personal_information_yossi.get("Phone_number", "+97243434343434") # get the value assuming 
                                                                                    # there might not be such key. 
print(phone_number_yossi)
print(personal_information_yossi)

phone_number_hen = personal_information_hen.get("Phone_number", "+97243434343434")
print(phone_number_hen)
