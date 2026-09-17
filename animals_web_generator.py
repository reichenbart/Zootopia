import json



def load_json_data(file_path):
    """loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)



def get_info(animals, filter_value):
    """iterates through a list, gets specific information as a string and returns that string"""
    output = ''

    if filter_value is not None:
        for animal in animals:
            if filter_value in animal.get('characteristics', {}).get('skin_type'):
                output += serialize_animal(animal)
    else:
        for animal in animals:
            output += serialize_animal(animal)

    return output



def choose_skin_type():
    """Shows a menu, asks user for an input. Returns a string which matches the value of skin type in the json data the user wants to see"""
    print(
        'Skin types:\n',
        '1. Hair\n',
        '2. Fur\n',
        '3. Scales\n',
        '4. Show all\n'
    )
    while True:
        choice = input('Please select, which animals should be displayed based on the selected skin type (1-4): ')
        if choice == '1':
            return 'Hair'
        if choice == '2':
            return 'Fur'
        if choice == '3':
            return 'Scales'
        if choice == '4':
            return None
        else:
            print('Please enter a value between 1 and 4!')



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
    user_filter = choose_skin_type()
    fox_info = get_info(animals_data, user_filter)
    starting_page = "animals_template.html"

    page = read_template(starting_page)
    animals_html = page.replace("__REPLACE_ANIMALS_INFO__", fox_info)

    write_template(animals_html, "animals.html")



if __name__ == "__main__":
    main()