#Team Name: Dennis Chen & Damien Wasilewicz
#SoftDev pd6
#K24: A RESTful Journey Skyward
#Date: 11/3/18

from flask import Flask, render_template
import urllib
app = Flask(__name__)


@app.route("/")
def rest():
    url = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=tSOmupc7rttYZViprGK30TqKeqj23UqAbhFEukqN")
    print(url)
if __name__ == '__main__':
    app.run(debug=True)
