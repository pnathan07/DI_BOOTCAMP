import requests
import json

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)
data: dict = response.json()

print(data)
print(type(data))

new_json_file_location = "json_files/new_data.json"


with open(new_json_file_location, mode="w") as file:
    json.dump(data, file)
