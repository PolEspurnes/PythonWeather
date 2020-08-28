from PyQt5.QtWidgets import QApplication

from GUI.WeatherGUI import WeatherGUI

import sys


app = QApplication(sys.argv)
ex = WeatherGUI()
sys.exit(app.exec_())



'''
while True:
    city = input("Introduce city: ")
    weather.weather_request(city)
    if input("Exit? (y) ") == "y":
        exit()

'''
