import unittest
from OpenWeather import OpenWeather
from WebAPI import WebAPI

zipcode = "90703"
ccode = "US"
weather_apikey = "37678f5231ba3e6702a5bf80a140f947"


class RegularTest(unittest.TestCase):
    def test_regular(self):
        open_weather = OpenWeather(zipcode, ccode)
        open_weather.set_apikey(weather_apikey)
        open_weather.load_data()
        assert open_weather.city == "Cerritos"
        assert open_weather.longitude == -118.0686
        assert open_weather.latitude == 33.8669


class DownloadURL(unittest.TestCase):
    def test_url(self):
        url_test = OpenWeather(zipcode, ccode)
        url_test.set_apikey(weather_apikey)
        url_test._download_url("https://www.thisisnotopenweather.com")


class WrongAPIKey(unittest.TestCase):
    def test_wrongAPIKey(self):
        wrong_api_key = OpenWeather(zipcode, ccode)
        wrong_api_key.set_apikey("not_an_api_key_lol")
        wrong_api_key.load_data()
        assert wrong_api_key.longitude == None


class NoParameters(unittest.TestCase):
    def test_no_params(self):
        no_param_weather = OpenWeather()
        no_param_weather.set_apikey(weather_apikey)
        no_param_weather.load_data()
        assert no_param_weather.city == "Irvine"
        assert no_param_weather.longitude == -117.8417
        assert no_param_weather.latitude == 33.6425


class TranscludeTest(unittest.TestCase):
    def test_transclude(self):
        transclude_time = OpenWeather(zipcode, ccode)
        transclude_time.set_apikey(weather_apikey)
        transclude_time.load_data()
        print(transclude_time.transclude("Today it is @weather"))
        print(transclude_time.transclude("No keyword lmao"))


class NoAPIKey(unittest.TestCase):
    def test_no_key(self):
        no_api_key = OpenWeather(zipcode, ccode)
        no_api_key.load_data()

if __name__ == "__main__":
    unittest.main()
