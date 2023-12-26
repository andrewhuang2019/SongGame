# api.py

import os
import sys
import json
import spotipy
import webbrowser
import requests
import spotipy as util
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

class API:
    def __init__(self):
        os.environ['SPOTIPY_CLIENT_ID'] = '11fa54af84e7489eb6ceeea69ccd38d6'
        os.environ['SPOTIPY_CLIENT_SECRET'] = '257c188fd54c4e9c86a964982f22bcc8'

        # can change it later to the website url
        os.environ['SPOTIPY_REDIRECT_URI'] = 'http://google.com/'

    def quick_start(self):
        lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        results = spotify.artist_top_tracks(lz_uri)

        for track in results['tracks'][:10]:
            print('track    : ' + track['name'])
            print('audio    : ' + track['preview_url'])
            print('cover art: ' + track['album']['images'][0]['url'])
            print()

    # can use current user methods
    def authorization_code_flow(self):

        scope = "user-library-read"

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

        results = sp.current_user_saved_tracks()

        user = sp.current_user()
        print(user)

        '''for idx, item in enumerate(results['items']):
            track = item['track']
            print(idx, track['artists'][0]['name'], " – ", track['name'])'''

    # cannot use current user methods
    # must use ID
    def client_credentials_flow(self):

        auth_manager = SpotifyClientCredentials()
        sp = spotipy.Spotify(auth_manager=auth_manager)
        user_id = '317apgb6nqp6r6rpndfwb2hw4s74?si=9d82f8b318434677'

        playlists = sp.user_playlists(user_id)

        # User ID: 317apgb6nqp6r6rpndfwb2hw4s74?si=9d82f8b318434677
        # Playlist Link: https://open.spotify.com/playlist/49se2DJsnGlPGrbXZgwQ5T?si=5003f7fdee084eab

        print(json.dumps(playlists, sort_keys=True, indent=4))
        print(sp.user(user_id))

        '''while playlists:
            for i, playlist in enumerate(playlists['items']):
                print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
            if playlists['next']:
                playlists = sp.next(playlists)
            else:
                playlists = None'''

    def spotipy_tutorial(self):
        # find User ID from logging into spotify and share + link.
        # it's the numbers after the link

        # get username from terminal
        scope = sys.argv[1]

        # User ID:

        # erase cache and prompt for user permission
        # actually archived
        '''try:
            scope = util.prompt_for_user_token(username)
        except:
            os.remove(f".cache-{username}")'''

        # create spotifyObject
        auth_manager = SpotifyClientCredentials()
        spotify_object = spotipy.Spotify(auth_manager=auth_manager)

        # gives data of the current user
        user = spotify_object.current_user()

        # gives json data
        print(json.dumps(user, sort_keys=True, indent=4))

        # can grab the user's specific information using:
        displayName = user['display_name']
        follower = user['followers']['total']

        # we can then set the environment variables in the terminal using 'export'
        # check spotipy api reference for the individual methods
    
