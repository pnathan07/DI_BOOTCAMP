personal_information_yossi = {
    "Name": "Yossi",
    "Residence": "Tel Aviv",
    "Age": 33,
}

personal_information_yossi["Phone_number"] = "+9725200000000"  # adds a new key-value

print(personal_information_yossi)


additional_info_yossi = {"Birthdate": "06/11/91", "Favorite fruit": "Kiwi"}

personal_information_yossi.update(additional_info_yossi) # adds the additional_info_yossi into the personal_information_yossi

print(personal_information_yossi)
