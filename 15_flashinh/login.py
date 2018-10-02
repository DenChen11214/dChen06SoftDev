#Team Denn is this Bo'kay - Dennis Chen & Bo Hui Lu
#SoftDev pd6
#K #14: Do I Know You?
#10/1/18
from flask import Flask, render_template, request, url_for, redirect, session,flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)
user = "bo"
pw = "dennis"

@app.route("/")
def disp_login():
    #print(session)
    if 'username' in session and session['username'].lower() == 'bo': #if logged in, go to the welcome page
        return redirect(url_for("welcome"))
    return render_template("login.html") #otherwise go to the login page


@app.route('/auth', methods = ["GET"])
def authenticate():
    #checks if the username and password are correct
    if request.args['username'].lower() != "bo" or request.args['password'].lower() != "dennis":
        flash("Wrong Username or Password") #if not, flash an error and return to login
        return redirect(url_for("disp_login"))
    session['username'] = request.args['username']
    return redirect(url_for("welcome")) #otherwise put their username into the session and redirect them to the welcome page
@app.route('/welcome')
def welcome():
    return render_template('welcome.html', # renders the template for the welcome page
                           user = "Bo")

@app.route('/logout')
def logout():
    
    #these pop() methods removes the variable we inputted in beginning, effectively logging out the user
    session.pop('username', None)
    session.pop('password', None)
    
    #goes back to the login page
    return redirect(url_for('disp_login'))


#the good ole' debugger
if __name__ == '__main__':
    app.run(debug=True)
