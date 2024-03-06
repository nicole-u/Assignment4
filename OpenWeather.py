import urllib
import json
from urllib import request, error

def _download_url(url_to_download: str) -> dict:
    response = None
    r_obj = None

    try:
        response = urllib.request.urlopen(url_to_download)
        json_results = response.read()
        r_obj = json.loads(json_results)

    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print(f'Status code: {e.code}')

    finally:
        if response is not None:
            response.close()

    return r_obj


class OpenWeather():
    """
    A class that handles getting the data
    from the OpenWeather API and passes it
    to class data attributes to be used later.
    """
    def __init__(self, zipcode, ccode):
        self.api_key = None
        self.zipcode = zipcode
        self.country = ccode
        self.temperature = None
        self.high_temp = None
        self.low_temp = None
        self.longitude = None
        self.latitude = None
        self.description = None
        self.humidity = None
        self.city = None
        self.sunset = None

    def set_apikey(self, apikey: str) -> None:
        '''
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service
        '''
        self.api_key = apikey
        return self.api_key

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response
        in class data attributes.
        '''
        if self.api_key is None:
            raise ValueError("No API key has been inputted.")
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.country}&appid={self.api_key}"
        returned_data = _download_url(url)
        self.longitude = returned_data['coord']['lon']
        self.latitude = returned_data['coord']['lat']
        self.description = returned_data['weather'][0]['description']
        self.temperature = returned_data['main']['temp']
        self.high_temp = returned_data['main']['temp_max']
        self.low_temp = returned_data['main']['temp_min']
        self.humidity = returned_data['main']['humidity']
        self.city = returned_data['name']
        self.sunset = returned_data['sys']['sunset']

    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
            
        :returns: The transcluded message
        '''
        accepted_keyword = "@weather"
        if accepted_keyword not in message:
            raise ValueError("No keyword found in message.")
        transcluded = message.replace(accepted_keyword, self.description)
        return transcluded
