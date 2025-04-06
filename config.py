import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

print("CLIENT_ID:", os.getenv("SPOTIPY_CLIENT_ID"))
print("REDIRECT_URI:", os.getenv("SPOTIPY_REDIRECT_URI"))
# Очистка кэша токена, если менялся scope
if os.path.exists(".cache"):
    os.remove(".cache")


def get_spotify_client():
    print("CLIENT_ID:", os.getenv("SPOTIPY_CLIENT_ID"))
    print("REDIRECT_URI:", os.getenv("SPOTIPY_REDIRECT_URI"))
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope='playlist-read-private playlist-modify-public'
    ))
