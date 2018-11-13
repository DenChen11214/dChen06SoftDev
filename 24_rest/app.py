#Team Name: Dennis Chen & Damien Wasilewicz
#SoftDev pd6
#K24: A RESTful Journey Skyward
#Date: 11/3/18

from flask import Flask, render_template
import urllib.request
import json
app = Flask(__name__)


@app.route("/")
def rest():
    url = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=c9f1tityqeXECe3ENg25UCnIWGbr5s26fDeuSzR9")
    info = url.read()
    data = json.loads(info.decode("utf-8"))
    #print(data)
    image = data['url']
    #print(image)
    return render_template("index.html", link = image)
if __name__ == '__main__':
    app.run(debug=True)
