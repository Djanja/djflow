import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id='ВАШ_CLIENT_ID',
        client_secret='ВАШ_CLIENT_SECRET',
        redirect_uri='http://localhost:8888/callback',
        scope='playlist-read-private playlist-modify-public'
    ))
