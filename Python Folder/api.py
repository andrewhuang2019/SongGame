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
        #client_id = 'your-client-id'
        #client_secret = 'your-client-secret'

        lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


        track = spotify.artist_top_tracks(lz_uri)
        tracks = track['tracks']
        for item in tracks:
            print('audio  : ' + item['preview_url'])


        """for track in results['tracks'][:10]:
            print('track    : ' + track['name'])
            print('audio    : ' + track['preview_url'])
            print('cover art: ' + track['album']['images'][0]['url'])
            print()"""
        

    # can use current user methods
    def authorization_code_flow(self):

        scope = "user-library-read"

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

        results = sp.current_user_saved_tracks()

        user = sp.current_user()
        saved_tracks = sp.current_user_saved_tracks()
        top_tracks = sp.current_user_top_tracks()
        print(user)
        # track['preview_url']

        #for track in sp.current_user_top_tracks():
        #    print('audio: ' + track['items']['preview_url'])

        '''for idx, item in enumerate(saved_tracks['items']):
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
        # scope = sys.argv[1]

        # User ID:

        # erase cache and prompt for user permission
        # actually archived
        '''try:
            scope = util.prompt_for_user_token(username)
        except:
            os.remove(f".cache-{username}")'''

        scope = "user-library-read"

        # create spotifyObject
        spotify_object = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

        # gives data of the current user
        user = spotify_object.current_user()

        # we can then set the environment variables in the terminal using 'export'
        # check spotipy api reference for the individual methods

        # gives json data
        print(json.dumps(user, sort_keys=True, indent=4))

        # can grab the user's specific information using:
        displayName = user['display_name']
        follower = user['followers']['total']

        while True:
            print()
            print(">>> Welcome to Spotipy " + displayName + "!")
            print(">>> You have " + str(follower) + " followers.")
            print()
            print("0 - Search for an artist")
            print("1 - exit")
            print()
            choice = input("Your choice: ")

            # search for the artist
            if choice == "0":
                print()
                search_query = input("Ok, what's their name?: ")
                print()

                # get search results
                # maybe can be used to grab a specifc song and track?
                search_results = spotify_object.search(search_query, limit=1, offset=0, type="artist")
                print(json.dumps(search_results, sort_keys=True, indent=4))

                # artist details
                artist = search_results['artists']['items'][0]
                print(artist)
                print(str(artist['followers']['total']) + " followers")
                print(artist['genres'][0])
                print()
                artist_id = artist['id']

                # might need to install webbrowser in terminal
                # webbrowser.open(artist['images'][0]['url'])

                # album and track details
                track_uris = []
                track_art = []
                z = 0

                # extract album data
                album_results = spotify_object.artist_albums(artist_id)

                # most things in spotify api uses IDs: artists, tracks, etc.
                # usually json data will show ID, and it should be saved in a variable.

                album_results = album_results['items']

                for item in album_results:
                    print("ALBUM " + item['name'])
                    album_id = item['id']
                    album_art = item['images'][0]['url']

                    # extract track data
                    track_results = spotify_object.album_tracks(album_id)
                    track_results = track_results['items']

                    for item in track_results:
                        print(str(z) + ": " + item['name'])
                        track_uris.append(item['uri'])
                        track_art.append(album_art)
                        z += 1
                    print()

                # see album art
                while True:
                    song_selection = input("Enter a song number to see the album art associated with it (x to exit): ")
                    if song_selection == "x":
                        break
                    # webbrowser.open(track_art[int(song_selection)]) <-- can pull up album art

            # end program
            if choice == "1":
                break


    
