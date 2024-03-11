import unittest
from OpenWeather import OpenWeather

zipcode = "90703"
ccode = "US"
apikey = "37678f5231ba3e6702a5bf80a140f947"

class RegularTest(unittest.TestCase):
    def regular_test(self):
        open_weather = OpenWeather(zipcode, ccode)
        open_weather.set_apikey(apikey)
        open_weather.load_data()
        assert open_weather.city == "Cerritos"
        assert open_weather.longitude == -118.0686
        assert open_weather.latitude == 33.8669

class DownloadURL(unittest.TestCase):
    def url_download_test(self):
        url_test = OpenWeather(zipcode, ccode)
        url_test.set_apikey(apikey)
        url_test._download_url("https://www.thisisnotopenweather.com")

class WrongAPIKey(unittest.TestCase):
    def wrongAPIKey(self):
        wrong_api_key = OpenWeather(zipcode, ccode)
        wrong_api_key.set_apikey("not_an_api_key_lol")
        wrong_api_key.load_data()
        assert wrong_api_key.longitude == None

class NoParameters(unittest.TestCase):
    def no_params(self):
        no_param_weather = OpenWeather()
        no_param_weather.set_apikey(apikey)
        no_param_weather.load_data()
        assert no_param_weather.city == "Irvine"
        assert no_param_weather.longitude == -117.8417
        assert no_param_weather.latitude == 33.6425

class TranscludeTest(unittest.TestCase):
    def transclude_testing(self):
        transclude_time = OpenWeather(zipcode, ccode)
        transclude_time.set_apikey(apikey)
        transclude_time.load_data()
        print(transclude_time.transclude("Today it is @weather"))
        print(transclude_time.transclude("No keyword lmao"))

class NoAPIKey(unittest.TestCase):
    def no_key(self):
        no_api_key = OpenWeather(zipcode, ccode)
        no_api_key.load_data()
