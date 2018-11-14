#Team Name: Dennis Chen
#SoftDev pd6
#K25: Getting More REST
#Date: 11/14/18

import urllib.request
import json
import operator

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def rest():
    #opens the api url and reads it
    url = urllib.request.urlopen("https://na1.api.riotgames.com/lol/league/v3/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=RGAPI-7307a50e-9821-4724-b6ee-69fa4a4801ed")
    info = url.read()
    #print(info)
    #loads the JSON object string and turns it into a dictionary
    data = json.loads(info.decode("utf-8"))
    #print(data)
    #gets the name of each player from the dictionary
    entries = data["entries"]
    #print(entries)
    challengers = dict()
    for player in entries:
        challengers[player['playerOrTeamName']] = player['leaguePoints']
    #print(challengers)
    sortedCTuple = sorted(challengers.items(), key=lambda x: x[1], reverse = True)
    #print(sortedCTuple)
    sortedC = []
    for player in sortedCTuple:
        sortedC.append(player[0] + ":" + str(player[1]))
    #print(sortedC)
    #loads it into an html
    return render_template("index.html",list = sortedC)
if __name__ == '__main__':
    app.run(debug=True)
