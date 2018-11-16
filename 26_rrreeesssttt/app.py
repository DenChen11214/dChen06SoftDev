#Team Name: Dennis Chen
#SoftDev pd6
#K25: Getting More REST
#Date: 11/14/18

from urllib.request import Request, urlopen
import urllib.request
import json
import operator

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def rest():
    #opens the api url and reads it

    dog = urllib.request.urlopen("https://random.dog/woof.json")
    info = dog.read()
    #print(dog)
    #loads the JSON object string and turns it into a dictionary
    data = json.loads(info)
    dogI = data['url']
    #stops mp4s from playing
    while dogI[-4:] == '.mp4':
        dog = urllib.request.urlopen("https://random.dog/woof.json")
        info = dog.read()
        data = json.loads(info)
        dogI = data['url']
    #print(data)
    akamaru = urllib.request.urlopen("https://api.jikan.moe/v3/search/character/?q=Akamaru&limit=1")
    info2 = akamaru.read()
    #print(info2)
    data2 = json.loads(info2)
    akaImage = data2['results'][0]['image_url']
    #print(akaImage)
    pokemon = "https://api.pokemontcg.io/v1/cards?name=arcanine"
    info3 = urlopen(Request(pokemon, headers={'User-Agent': 'Mozilla/5.0'})).read()
    #print(info3)
    data3 = json.loads(info3)
    arcanine = data3['cards'][0]['imageUrl']
    return render_template("index.html", dogI = dogI, aka = akaImage, arc = arcanine)

app.run(debug=True)
