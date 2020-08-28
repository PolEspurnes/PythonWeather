from WeatherAPI import WeatherAPI


weather = WeatherAPI()

while True:
    city = input("Introduce city: ")
    weather.weather_request(city)
    if input("Exit? (y) ") == "y":
        exit()
