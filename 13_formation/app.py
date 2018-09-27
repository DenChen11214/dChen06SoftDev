#Dennis Chen
#SoftDev pd6
#K13: Echo Echo Echo#: Assignment Name ...
#9/27/18

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def sth():
    print(app)
    return render_template('echo.html')
@app.route('/auth')
def authenticate():
    return render_template('auth.html', method = request.method, name = request.args['name'], wa = "WAAAAAAAAAAAAAAAAAAAAAAAAHHHAHAHAHHAHAHAH")
if __name__ == '__main__':
    app.run(debug=True)
