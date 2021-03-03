from bs4 import BeautifulSoup
import requests
import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
CLIENT_ID = ""
CLIENT_SECRET = ""

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID, 
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
        ))
user_id = sp.current_user()["id"]


date_input = input("Which year you want to travel to? type the date in this format YYYY-MM-DD: ")
# date_input = "2000-12-08"

response_billboard = requests.get("https://www.billboard.com/charts/hot-100/" + date_input)
soup = BeautifulSoup(response_billboard.text, 'html.parser')
song_names_spans = soup.find_all(name="span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

song_uris = []
year = date_input.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year: {year}", type="track")
    # pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exits in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date_input} Billboard100", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)



