from random import randint
from OpenWeather import OpenWeather


zipcode = "92617"
ccode = "US"
apikey = "37678f5231ba3e6702a5bf80a140f947"

# Standard testing
open_weather = OpenWeather(zipcode, ccode)
open_weather.set_apikey(apikey)
open_weather.load_data()
print(open_weather.transclude("The weather in Irvine is @weather"))
print(f"The temperature for {zipcode} is {open_weather.temperature} degrees")
print(f"The high for today in {zipcode} will be {open_weather.high_temp} degrees")
print(f"The low for today in {zipcode} will be {open_weather.low_temp} degrees")
print(f"The coordinates for {zipcode} are {open_weather.longitude} longitude and {open_weather.latitude} latitude")
print(f"The current weather for {zipcode} is {open_weather.description}")
print(f"The current humidity for {zipcode} is {open_weather.humidity}")
print(f"The sun will set in {open_weather.city} at {open_weather.sunset}")

# Triggering errors on purpose