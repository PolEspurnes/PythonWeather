import json

'''
In this function we want to create a dictionary with the city name as the key and insert a nested dictionary with 
id and country as value. If the city name is repeated (which is possible) the value will contain a list of nested 
dictionaries 
'''
def create_dictionary(filename):
    data = readJSON(filename)
    # Iterating through the json
    # list
    dictionary = {}
    for element in data:
        city = {
            "id": element["id"],
            "country": element["country"]
        }
        if element["name"] in dictionary:  # Check for same city but from different country
            new = True
            for saved in dictionary[element["name"]]:
                if saved["country"] == element["country"]:
                    new = False
                    break

            if new:
                dictionary[element["name"]].append(city)
        else:
            dictionary[element["name"]] = []
            dictionary[element["name"]].append(city)

    return dictionary


def readJSON(filename):
    # Opening JSON file
    f = open(filename, "r", encoding='utf-8')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Closing file
    f.close()
    return data
