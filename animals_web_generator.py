import json



def load_json_data(file_path):
    """loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)



def get_info(animals):
    """prints specific info of a dict in a list"""
    output = ''
    for animal in animals:
        locations = ", ".join(animal.get("locations", []))

        output += '<li class="cards__item">\n'
        output += f'<div class="card__title">{animal.get('name')}</div>\n'
        output += f'<p class="card__text">'
        output += f'<strong>Diet:</strong> {animal.get('characteristics').get('diet')}<br/>\n'
        output += f'<strong>Location:</strong> {locations}<br/>\n'

        if animal.get('characteristics', {}).get('type'):
            output += f'<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n'

        output += '</p></li>\n'

    return output



def read_template(file_path):
    with open(file_path, "r") as html_file:
        page = html_file.read()
    return page



def write_template(content, file_path):
    with open(file_path, "w") as html_file:
        new_page = html_file.write(content)
    return new_page



def main():
    animals_data = load_json_data('animals_data.json')
    fox_info = get_info(animals_data)
    starting_page = "animals_template.html"

    page = read_template(starting_page)
    animals_html = page.replace("__REPLACE_ANIMALS_INFO__", fox_info)

    write_template(animals_html, "animals.html")



if __name__ == "__main__":
    main()