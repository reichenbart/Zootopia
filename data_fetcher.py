import requests
import json


API_KEY = "U8eXhNjcTzFkDtaDo9O5zrDBwciGTaZ3qs7zkCKX"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'
    creates a json-file with the fetched data.
    Returns: nothing:
    """
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        data = response.json()
        with open("animals_data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Saved as animals_data.json")
    else:
        print("Error:", response.status_code, response.text)