

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="4c69590a97a1458f8099f57e7d7d86ca",
        client_secret="e17e17bddf52484c9b6f03cdc720fab9",
        show_dialog=True,
        cache_path="token.txt",
        username="Pritam Kumar Nath", 
    )
)
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_uris = ["The list of", "song URIs", "you got by", "searching Spotify"]

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
result = sp.search(q=f"track:{song} year:{year}", type="track")
print(result)
try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")