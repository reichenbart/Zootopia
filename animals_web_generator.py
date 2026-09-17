import json



def load_json_data(file_path):
    """loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)



def get_info(animals):
    """iterates through a list, gets specific information as a string and returns that string"""
    output = ''
    for animal in animals:
        output += serialize_animal(animal)

    return output



def serialize_animal(animal_obj):
    output = ''
    locations = ", ".join(animal_obj.get("locations", []))

    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj.get('name')}</div><br/>\n'
    output += '<div class="card__text">\n'
    output += f'<ul><li><strong>Diet:</strong> {animal_obj.get('characteristics').get('diet')}</li>\n'
    output += f'<li><strong>Location:</strong> {locations}</li>\n'

    if animal_obj.get('characteristics', {}).get('type'):
        output += f'<li><strong>Type:</strong> {animal_obj['characteristics']['type']}</li>\n'

    output += '</ul></div></li>\n'

    return output



def read_template(file_path):
    """opens, reads and closes a given file. Returns the files content as a string"""
    with open(file_path, "r") as html_file:
        page = html_file.read()
    return page



def write_template(content, file_path):
    """opens, writes given content to and closes a given file. Returns that file"""
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