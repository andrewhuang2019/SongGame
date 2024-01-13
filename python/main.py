# main.py

import spotipy
import requests

from menu import Menu
from api import API

menu = Menu()
#menu.run()
api = API()

api.get_playlist_urls('https://open.spotify.com/playlist/5VvixKeAd1Q2pjsxwG9b2X')
#api.get_playlist_information('https://open.spotify.com/playlist/5VvixKeAd1Q2pjsxwG9b2X')

def testing():
    pass

testing()

