# flask_file.py

from flask import Flask, render_template
from api import API


app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('mainpage.html')

@app.route('/game')
def game_page():
    song_api = API()
    #https://open.spotify.com/playlist/0xZnpACpVA3NdZbNpoVjWD?si=43c9cae91e7645bc
    #https://open.spotify.com/playlist/5VvixKeAd1Q2pjsxwG9b2X
    track_details = song_api.get_playlist_urls('https://open.spotify.com/playlist/5VvixKeAd1Q2pjsxwG9b2X')
    playlist_details = song_api.get_playlist_information('https://open.spotify.com/playlist/5VvixKeAd1Q2pjsxwG9b2X')
    return render_template('game.html', track_details=track_details, playlist_details=playlist_details)

app.run(debug=True)



