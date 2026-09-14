import json



def load_json_data(file_path):
    """loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_json_data('animals_data.json')



def get_info(animals):
    """prints specific info of a dict in a list"""
    output = ""
    for animal in animals:
        locations = ", ".join(animal.get("locations", []))

        output += f"Name: {animal.get('name')}\n"
        output += f"Diet: {animal.get('characteristics').get('diet')}\n"
        output += f"Location: {locations}\n"

        if animal.get('characteristics', {}).get('type'):
            output += f"Type: {animal['characteristics']['type']}\n"

        output += "\n"

    return output



fox_info = get_info(animals_data)



with open("animals_template.html", "r") as html_file:
    page = html_file.read()


animals_html = page.replace("__REPLACE_ANIMALS_INFO__", fox_info)

with open("animals.html", "w") as html_file:
    new_page = html_file.write(animals_html)