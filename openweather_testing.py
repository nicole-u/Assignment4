from OpenWeather import OpenWeather


zipcode = "90703"
ccode = "US"
apikey = "37678f5231ba3e6702a5bf80a140f947"

# Regular testing
open_weather = OpenWeather(zipcode, ccode)
open_weather.set_apikey(apikey)
open_weather.load_data()
assert open_weather.city == "Cerritos"
assert open_weather.longitude == -118.0686
assert open_weather.latitude == 33.8669
print("Regular testing: success")

# Download URL testing
url_test = OpenWeather(zipcode, ccode)
url_test.set_apikey(apikey)
url_test._download_url("https://www.thisisnotopenweather.com")

#Testing wrong api key
wrong_api_key = OpenWeather(zipcode, ccode)
wrong_api_key.set_apikey("not_an_api_key_lol")
wrong_api_key.load_data()
assert wrong_api_key.longitude == None
print("Wrong API Key: Success")

#Testing no parameters
no_param_weather = OpenWeather()
no_param_weather.set_apikey(apikey)
no_param_weather.load_data()
assert no_param_weather.city == "Irvine"
assert no_param_weather.longitude == -117.8417
assert no_param_weather.latitude == 33.6425
print("No params: Success")

# Transclude testing
transclude_time = OpenWeather(zipcode, ccode)
transclude_time.set_apikey(apikey)
transclude_time.load_data()
transclude_time.transclude("This has no keyword in it!")

#Testing no api key
no_api_key = OpenWeather(zipcode, ccode)
no_api_key.load_data()