# flask_file.py

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('mainpage.html')

@app.route('/game')
def game_page():
    return render_template('game.html')



