#Dennis Chen
#SoftDev pd6
#K13: Echo Echo Echo#: Assignment Name ...
#9/27/18

from flask import Flask, render_template, request
import random #used to choose btwn get and post
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('echo.html', method = random.choice(["GET","POST"]))# randomly chooses a request method
@app.route('/auth', methods = ["GET","POST"])
def authenticate():
    #request method and username stored
    requestM = request.method
    if requestM == "GET":
        username = request.args["username"]
    if requestM == "POST":
        username = request.form["username"]
    return render_template('auth.html', method = requestM, name = username, wa = "WAAAAAAAAAAAAAAAAAAAAAAAAHHHAHAHAHHAHAHAH")#template rendered using stored variables
if __name__ == '__main__':
    app.run(debug=True)
