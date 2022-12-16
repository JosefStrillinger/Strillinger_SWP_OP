import json
from flask_restful import Api
from flask import Flask, render_template, request
from main import SSPES_Game

app = Flask(__name__)
app.secret_key = "SSPES_Game_Flask"
api = Api(app)

@app.route('/')
def start():
    return render_template("homepage.html")

@app.route('/statistics/<player_name>')
def show_statistics(player_name):
    return render_template("data.html")

@app.route('/game')
def play_game():
    return render_template("game.html")

if __name__ == '__main__':
    app.debug=True
    app.run()
    
#TODO:
# html, css, implement methods and find a way to play game from browser 










