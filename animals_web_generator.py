import json



def load_json_data(file_path):
    """loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_json_data('animals_data.json')



def get_info(animals):
    """prints specific info of a dict in a list"""
    output = ''
    for animal in animals:
        locations = ", ".join(animal.get("locations", []))

        output += '<li class="cards__item">\n'
        output += f'Name: {animal.get('name')}<br/>\n'
        output += f'Diet: {animal.get('characteristics').get('diet')}<br/>\n'
        output += f'Location: {locations}<br/>\n'

        if animal.get('characteristics', {}).get('type'):
            output += f'Type: {animal['characteristics']['type']}<br/>\n'

        output += '</li>\n'

    return output



fox_info = get_info(animals_data)



with open("animals_template.html", "r") as html_file:
    page = html_file.read()


animals_html = page.replace("__REPLACE_ANIMALS_INFO__", fox_info)

with open("animals.html", "w") as html_file:
    new_page = html_file.write(animals_html)