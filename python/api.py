# api.py

import random
import os
import spotipy
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
from track_details import TrackDetails

class API:
    def __init__(self):
        os.environ['SPOTIPY_CLIENT_ID'] = '11fa54af84e7489eb6ceeea69ccd38d6'
        os.environ['SPOTIPY_CLIENT_SECRET'] = '257c188fd54c4e9c86a964982f22bcc8'

        # can change it later to the website url
        os.environ['SPOTIPY_REDIRECT_URI'] = 'http://google.com/'


    def get_album_data(self,playlist_link):
        playlist_link = playlist_link.split('/')

        cid = '11fa54af84e7489eb6ceeea69ccd38d6'
        secret = '257c188fd54c4e9c86a964982f22bcc8'
        client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
        sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

        playlist = sp.user_playlist('11fa54af84e7489eb6ceeea69ccd38d6',playlist_link[-1])

        #returns list with playlist name and image url, respectively 
        return([playlist['name'],sp.playlist_cover_image(playlist_link[-1])[0]['url']])



    def get_playlist_urls(self,playlist_link):
        tracks = []
        random_songs = []
        playlist_link = playlist_link.split('/')

        # oauth setup for our spotify account
        cid = '11fa54af84e7489eb6ceeea69ccd38d6'
        secret = '257c188fd54c4e9c86a964982f22bcc8'
        client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
        sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

        # pulling playlist info
        playlist = sp.user_playlist_tracks('11fa54af84e7489eb6ceeea69ccd38d6',playlist_link[-1])["items"]
        for track in playlist: 
            tracks.append(TrackDetails(track['track']['preview_url'],track['track']['name'],track['track']['artists'][0]['name']))


        while random_songs.length < 8:
            random_songs.append(TrackDetails())

        # randomly selecting 8 songs
        try:
            index_list = random.sample(range(0, len(tracks)-1), 8)
        except:
            print("\nPlaylist must contain 8 or more songs.\n")
        else:
            for index in index_list:
                random_songs.append(tracks[index])

            return random_songs

