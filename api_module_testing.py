from random import randint
from OpenWeather import OpenWeather


zipcode = "92617"
ccode = "US"
apikey = "37678f5231ba3e6702a5bf80a140f947"

# OpenWeather testing
open_weather = OpenWeather(zipcode, ccode)
open_weather.set_apikey(apikey)
open_weather.load_data()


# LastFM testing