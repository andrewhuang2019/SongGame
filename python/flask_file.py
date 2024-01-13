# flask_file.py

from flask import Flask, request, render_template
from api import API


app = Flask(__name__)


@app.route('/',  methods =["GET", "POST"])
def main_page():
    print("main page accessed")
    if request.method == "GET":
        print("getting")
        #haven't recieved input from user yet
        return render_template('mainpage.html')
    elif request.method == "POST":
        print("posting")
        #have recieved input, use request to get the html input value
        playlist_url = request.form.get("playlist")
        print(playlist_url)
        return game_page(playlist=playlist_url)

@app.route('/game')
def game_page(playlist="https://open.spotify.com/playlist/5VvixKeAd1Q2pjsxwG9b2X"):
    song_api = API()
    #https://open.spotify.com/playlist/0xZnpACpVA3NdZbNpoVjWD?si=43c9cae91e7645bc
    #https://open.spotify.com/playlist/5VvixKeAd1Q2pjsxwG9b2X
    track_details = song_api.get_playlist_urls(playlist)
    print("game page template rendered")
    playlist_details = song_api.get_playlist_information('https://open.spotify.com/playlist/5VvixKeAd1Q2pjsxwG9b2X')
    return render_template('game.html', track_details=track_details, playlist_details=playlist_details)

app.run(debug=True) 