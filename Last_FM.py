import WebAPI

api_key = "c0a60fb3ace4ff1ea2748e5319a9ee72"
api_secret = "b53553283cc9dd90e82c436112353517"

class LastFM(WebAPI.web_api):
    def __init__(self, username) -> None:
        self.user = username
        self.fav_track = None
        self.fav_artist = None

    def _download_url(self, url_to_download: str) -> dict:
        downloaded = WebAPI.web_api._download_url(self, url_to_download)
        return downloaded

    def set_apikey(self, apikey: str):
        WebAPI.web_api.set_apikey(self, apikey)

    def load_data(self) -> None:
        if self.user == None:
            raise ValueError("No username detected. Please try again.")
        top_tracks = f"http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={self.user}&api_key={api_key}&format=json"
        fm_track_data = self._download_url(top_tracks)
        self.fav_track = fm_track_data['toptracks']['track'][0]['name']
        # print(f"{self.user}'s favorite track is {self.fav_track}.")
        top_artists = f"http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user={self.user}&api_key={api_key}&format=json"
        fm_artist_data = self._download_url(top_artists)
        self.fav_artist = fm_artist_data['topartists']['artist'][0]['name']
        # print(f"{self.user}'s favorite artist is {self.fav_artist}.")

    def transclude(self, message: str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
            
        :returns: The transcluded message
        '''
        accepted_keyword = "@lastfm"
        if accepted_keyword not in message:
            raise ValueError("No keyword found in message.")
        track_or_artist = input("Would you like to display your favorite tracks or artists?").lower()
        if track_or_artist[0] == "t":
            transcluded = message.replace(accepted_keyword, self.fav_track)
        elif track_or_artist[0] == "a":
            transcluded = message.replace(accepted_keyword, self.fav_artist)
        
        return transcluded

if __name__ == "__main__":
    open_weather = LastFM("nutamaaaaa")
    open_weather.set_apikey(api_key)
    open_weather.load_data()