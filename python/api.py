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
    
    def get_playlist_information(self, playlist_link):

        #playlist_link = playlist_link.split('/')

        cid = '11fa54af84e7489eb6ceeea69ccd38d6'
        secret = '257c188fd54c4e9c86a964982f22bcc8'
        client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
        sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

        playlist = sp.user_playlist('11fa54af84e7489eb6ceeea69ccd38d6', playlist_link)

        playlist_name = playlist['name']

        playlist_image = playlist['images'][0]['url']

        return [playlist_name, playlist_image]


    def get_playlist_urls(self,playlist_link):
        tracks = []
        random_songs = []
        #playlist_link = playlist_link.split('/')

        # oauth setup for our spotify account
        cid = '11fa54af84e7489eb6ceeea69ccd38d6'
        secret = '257c188fd54c4e9c86a964982f22bcc8'
        client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
        sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

        # pulling playlist info
        #playlist = sp.user_playlist_tracks('11fa54af84e7489eb6ceeea69ccd38d6', playlist_link[-1])["items"]

        playlist = sp.user_playlist_tracks('11fa54af84e7489eb6ceeea69ccd38d6', playlist_link)['items']

        for track in playlist: 

            preview_url = track['track']['preview_url']

            song_name = track['track']['name']

            song_artist = track['track']['artists'][0]['name']

            album_image = track['track']['album']['images'][0]['url']

            album_name = track['track']['album']['name']

            tracks.append(TrackDetails(preview_url, song_name, song_artist, album_image, album_name))

        # randomly selecting 8 songs
        try:
            index_list = random.sample(range(0, len(tracks)-1), 8)
        except:
            print("\nPlaylist must contain 8 or more songs.\n")
        else:
            for index in index_list:
                random_songs.append(tracks[index])

            return random_songs

