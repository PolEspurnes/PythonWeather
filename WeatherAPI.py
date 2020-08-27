import requests

'''
Objectives:
 - API key en un local file
 - Demanar ciutat  http://bulk.openweathermap.org/sample/city.list.json.gz
 - Retornar temps actual

Advanced Objectives:
 - GUI
 - Input de ciutat en un form
 - Mostrar temps i icon https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
'''

key_filename = "APIkey"

class WeatherAPI:

    def __init__(self):
        try:
            key_file = open(key_filename, "r")
            self.key = key_file.readline()
            key_file.close()
        except FileNotFoundError:
            print("File not found")
        pass
