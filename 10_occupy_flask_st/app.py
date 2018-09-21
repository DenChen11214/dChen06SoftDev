from flask import Flask,render_template

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
collection = [0,1,1,2,3,5,8]
@app.route('/myTemplate')
def collList():
    return render_template("myTemplate.html", foo = "HELLO WORLD", coll = collection)
    
if __name__ == "__main__":
    app.debug = True
    app.run()
