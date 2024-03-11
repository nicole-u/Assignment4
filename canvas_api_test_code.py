from WebAPI import WebAPI
from OpenWeather import OpenWeather
from Last_FM import LastFM

api_key_weather = "37678f5231ba3e6702a5bf80a140f947"
api_key_fm = "c0a60fb3ace4ff1ea2748e5319a9ee72"

def test_api(message: str, apikey: str, webapi: WebAPI):
    webapi.set_apikey(apikey)
    webapi.load_data()
    result = webapi.transclude(message)
    print(result)

opw = OpenWeather()
lastfm = LastFM()

test_api("Testing @weather", api_key_weather, opw)
test_api("Testing @lastfm", api_key_fm, lastfm)