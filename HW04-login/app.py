#Jiaqi Gao
#SoftDev Pd08
#HW4: Write a Flask app to facilitate simple logins via POST.

import hashlib, csv 
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

csv = "static/storage.csv"

#storage = open("static/storage.csv").read()
#storage = storage.split(';')

def hasher(passw):
    hash_obj = hashlib.sha1(b'passw')
    hex_dig = hash_obj.hexdigest()
    return(hex_dig)

@app.route("/auth", methods=['POST'])
def authenticate():
    fd = open(csv, 'a')    
    fd.write(request.form["username"]+","+hasher(request.form["password"])+";")
    fd.close()
    return render_template("success.html", result="nice")
    
if __name__ == "__main__":
    app.debug = True
    app.run()                                
