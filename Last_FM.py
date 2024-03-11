import WebAPI

DEV_FM_KEY = "c0a60fb3ace4ff1ea2748e5319a9ee72"
api_secret = "b53553283cc9dd90e82c436112353517"

class LastFM(WebAPI.WebAPI):
    def __init__(self, username = "nutamaaaaa") -> None:
        self.user = username
        self.fav_track = None
        self.fav_artist = None

    def _download_url(self, url_to_download: str) -> dict:
        downloaded = WebAPI.WebAPI._download_url(self, url_to_download)
        return downloaded

    def set_apikey(self, apikey: str):
        try:
            WebAPI.WebAPI.set_apikey(self, apikey)
        except:
            print("Error with API key.")
            WebAPI.WebAPI.set_apikey(self, DEV_FM_KEY)

    def load_data(self) -> None:
        if self.user is None:
            raise ValueError("No username detected. Please try again.")
        top_tracks = f"http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={self.user}&api_key={self.api_key}&format=json"
        fm_track_data = self._download_url(top_tracks)
        if type(fm_track_data) == None:
            raise TypeError("Error with downloading track data from LastFM.")
        self.fav_track = fm_track_data['toptracks']['track'][0]['name']
        top_artists = f"http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user={self.user}&api_key={self.api_key}&format=json"
        fm_artist_data = self._download_url(top_artists)
        if type(fm_artist_data) is None:
            raise TypeError("Error with downloading artist data from LastFM.")
        self.fav_artist = fm_artist_data['topartists']['artist'][0]['name']

    def transclude(self, message: str, keyword= "@lastfm") -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
            
        :returns: The transcluded message
        '''
        if keyword not in message:
            raise ValueError("No keyword found in message.")
        if keyword == "@lastfm":
            transcluded = message.replace(keyword, self.fav_track)
        if keyword == "@artist":
            transcluded = message.replace(keyword, self.fav_artist)
        
        return transcluded
