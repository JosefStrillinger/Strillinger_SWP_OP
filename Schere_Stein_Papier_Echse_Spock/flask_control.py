import json
from flask_restful import Api
from flask import Flask, render_template, request, url_for, redirect
import matplotlib.pyplot as plt
from classes.sspes_game import SSPES_Game
import plotly
import plotly.express as px
import pandas as pd
import time

app = Flask(__name__)
app.secret_key = "SSPES_Game_Flask"
api = Api(app)

@app.route('/')
def start():
    return render_template("homepage.html")

@app.route('/statistic', methods=["POST"])
def show_statistics():
    player_name = request.form.get('player_name')
    player_stats = get_player_stats(player_name)
    player_plays = get_plays_name(player_stats)
    player_values = get_plays_value(player_stats)
    player_pd = get_plays_list_for_pd(player_plays, player_values)
    player_pd2 = get_outcome_list_for_pd(player_plays, player_values)
    plt.bar(player_plays, player_values)
    #plt.savefig("player_stats.png")
    df = pd.DataFrame(player_pd, columns = ["Play", "Value"])
    df2 = pd.DataFrame(player_pd2, columns = ["Outcome", "Amount"])
    fig = px.bar(df, x="Play", y="Value")
    fig2 = px.bar(df2, x="Outcome", y="Amount")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    graphs = [graphJSON, graphJSON2]
    return render_template("data.html", graphs = graphs)

@app.route('/upload_stats', methods = ['PUT'])
def get_player_statistic():
    print("upload start")
    save_data = request.get_json()
    print()
    with open("flask_save.json", "w") as rd:
        rd.write(json.dumps(save_data))
    print("success")
    return redirect(url_for("start"))

@app.route('/game')
def play_game():
    return render_template("game.html")

def get_player_stats(player_name):
    with open("flask_save.json", "r") as rd:
        saves = json.load(rd)     
    return saves[player_name]

def get_plays_name(player_dict):
    plays_list = []
    for i in player_dict.keys():
        plays_list.append(i)
    return plays_list

def get_plays_value(player_dict):
    value_list = []
    for i in player_dict.values():
        value_list.append(i)
    return value_list
    
def get_plays_list_for_pd(list1, list2):
    list_return = []
    for i in range(5):
        help = [list1[i], list2[i]]
        list_return.append(help)
    return list_return

def get_outcome_list_for_pd(list1, list2):
    list_return = []
    for i in range(5, len(list1)):
        help = [list1[i], list2[i]]
        list_return.append(help)
    return list_return

if __name__ == '__main__':
    app.debug=True
    app.run()
    
#TODO:
# html, css, implement methods and find a way to play game from browser 










