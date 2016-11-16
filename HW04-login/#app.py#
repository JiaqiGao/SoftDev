#Jiaqi Gao
#SoftDev Pd08
#HW5: Augment your latest Flask app to facilitate sessions and redirection.

import hashlib, csv, os
from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)

app.secret_key = os.urandom(32)

@app.route("/")
def index():
    if 'usr' in session:
        return render_template("home.html", user=session["usr"])
    return redirect(url_for('login'))

@app.route("/login")
def login():
    createdict()
    return render_template("form.html")

@app.route("/logout")
def logout():
    session.pop('usr')
    return redirect(url_for('login'))

csv = "static/storage.csv"
storage = dict()

#@app.route("/jacobo")
#def js():
 #   print(url_for("index"))
  #  return redirect("http://xkcd.com")

#creates dictionary out of the csv file data, username : password
def createdict():
    sdata = open(csv).read()
    sdata = sdata.split(';')
    sdata[:] = [x.split(',') for x in sdata]
    for i in sdata:
        storage[i[0]] = i[1]

#Does the hashing
def hasher(passw):
    return hashlib.sha224(passw.encode('utf-8')).hexdigest()
    

@app.route("/auth", methods=['POST'])
def authenticate():
    usr = request.form["username"]
    pd = request.form["password"]
    #if exists, checks if password is correct, if not, tells you pass is wrong
    if usr in storage:
        if hasher(pd) == storage[usr]:
            session['usr'] = usr 
            return render_template("home.html", user=session['usr'])
        else:
            return render_template("success.html", result="*Password is incorrect*")
    else:
        return render_template("success.html", result="The username does not exist. Go back to create an account")

@app.route("/new", methods=['POST'])
def new():
    return render_template("create.html")


@app.route("/create", methods=['POST'])
def create():
    usr = request.form["username"]
    pd = request.form["password"]
    fd = open(csv, 'a')
    if usr in storage:
        return render_template("success.html", result="An account with that username already exists. Enter the correct password at sign in or make a new account")
    fd.write(";"+usr+","+hasher(pd))
    fd.close()
    return render_template("success.html", result="Account was successfully created!")

if __name__ == "__main__":
    app.debug = True
    app.run()                                
