from flask import Flask

app = Flask(__name__)

@app.route("/")
def knockKnock():
    return '<a href = "/2"> Knock Knock </a>'

@app.route("/2")
def whosThere():
    return '<a href = "/3"> Who\'s There </a>'

@app.route('/3')
def noOne():
    return 'No one. Bye bye!'

if __name__ == "__main__":
    app.debug = True
    app.run()
