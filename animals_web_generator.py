import json



def load_data(file_path):
    """loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')



def get_info(animals):
    """prints specific info of a dict in a list"""
    for animal in animals:
        locations = ", ".join(animal.get("locations", []))

        print(
            "Name:", animal.get('name'),"\n"
            "Diet:", animal.get('characteristics').get('diet'),"\n"
            "Location:", locations
        )

        if animal.get('characteristics', {}).get('type'):
            print(
                "Type:", animal['characteristics']['type']
            )

        print()


print(get_info(animals_data))