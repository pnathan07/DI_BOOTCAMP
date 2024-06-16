# Dictionary in python - Key-Value based Data Collection
# Lists are index based Data Collections

# Keys are always unique

# Dictionaries are useful when we have categories for the data we want to collect into a single place. 

a_dictionary = {
    "Sun": "A hot celestial body with specific characteristics...",
    "Moon": "A celestial body located next to Earth...",
}

user_choice = "Sun"

# print(a_dictionary[user_choice])

personal_information_yossi = {
    "Name": "Yossi",
    "Residence": "Tel Aviv",
    "Age": 33,
}


personal_information_hen = {
    "Name": "Hen",
    "Residence": "Paris",
    "Age": 45,
}

personal_information_ron = {
    "Name": "Ron",
    "Residence": "Eilat",
    "Age": 15,
}

people = {
    "Yossi": {
        "Name": "Yossi",
        "Residence": "Tel Aviv",
        "Age": 33,},
    
    "Ron": {
        "Name": "Hen",
        "Residence": "Paris",
        "Age": 45,
    },
    
    "Hen": {
        "Name": "Ron",
        "Residence": "Eilat",
        "Age": 15,
    },
}



print(people["Yossi"]["Residence"])