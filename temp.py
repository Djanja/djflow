# import os
# from spotipy.oauth2 import SpotifyOAuth
# import spotipy
# from dotenv import load_dotenv
#
# load_dotenv()
#
# print("CLIENT_ID:", os.getenv("SPOTIPY_CLIENT_ID"))
# print("SPOTIPY_CLIENT_SECRET:", os.getenv("SPOTIPY_CLIENT_SECRET"))
# print("REDIRECT_URI:", os.getenv("SPOTIPY_REDIRECT_URI"))
#
#
#
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
#     client_id=os.getenv("SPOTIPY_CLIENT_ID"),
#     client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
#     redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
#     scope='playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private'
# ))
#
# print("Success! Authenticated as:", sp.current_user()['display_name'])
