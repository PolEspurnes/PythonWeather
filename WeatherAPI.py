import requests
from CitiesDictionary import create_dictionary


'''
 - Demanar ciutat  http://bulk.openweathermap.org/sample/city.list.json.gz
'''

key_filename = "APIkey"
city_filename = "city.list.json"

class WeatherAPI:

    def __init__(self):
        try:
            key_file = open(key_filename, "r")
            self.key = key_file.readline()
            key_file.close()
            self.cities = create_dictionary(city_filename)
            self.options_window = None
            self.result_window = None
        except FileNotFoundError:
            print("File not found")


    def GUI_option_selected(self, id):
        url = "https://api.openweathermap.org/data/2.5/weather?id=" + str(id) + "&units=metric&appid=" + self.key
        response = requests.get(url)
        if response:
            return response.json()


    '''
    The following Functions are used without the GUI. Insert this code in main.py
    
    while True:
        city = input("Introduce city: ")
        weather.weather_request(city)
        if input("Exit? (y) ") == "y":
            exit()

    '''
    def weather_request(self, city):
        l = len(self.cities[city])
        if l > 1:
            for i in range(l):
                print("  "+str(i+1)+". "+city+" - "+self.cities[city][i]["country"])
            try:
                option = int(input("Choose option: ")) - 1
                id = self.cities[city][option]["id"]
            except ValueError:
                print("Invalid input")
                return
            except IndexError:
                print("Not an option")
                return
        else:
            id = self.cities[city][0]["id"]

        url = "https://api.openweathermap.org/data/2.5/weather?id=" + str(id) + "&units=metric&appid=" + self.key
        response = requests.get(url)
        if response:
            print('Request is successful.')
            self.show_results(response.json(), city)
        else:
            print('Request returned an error.')


    def show_results(self, response, city):
        print("\n*---------- "+city+" "+response["sys"]["country"]+" ----------*")
        weather = response["weather"][0]["main"]
        print("\n* Weather conditions: "+weather)
        temps = response["main"]
        print("\n* Actual temperature: "+ str(temps["temp"]) +"ºC")
        print("\n* Minimum temperature: " + str(temps["temp_min"]) + "ºC")
        print("\n* Maximum temperature: " + str(temps["temp_max"]) + "ºC\n")


