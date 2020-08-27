from WeatherAPI import WeatherAPI
from CitiesDictionary import create_dictionary

weather = WeatherAPI()
create_dictionary("city.list.json")

'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}

city1 = {
  "id" : "Emil",
  "country" : "ES"
}
city2 = {
  "id" : "Tobias",
  "country" : "US"
}

thisdict["Barcelona"] = []
thisdict["Barcelona"].append(city1)
thisdict["Barcelona"].append(city2)
print(thisdict)
'''
