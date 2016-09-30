#Jiaqi Gao
#SoftDev Pd08
#HW4: Write a Flask app to facilitate simple logins via POST.

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/auth", methods=['POST'])
def authenticate():
    if request.form["username"]=="doraemon" and request.form["password"]=="bluecatrobot":
        return render_template("success.html", result="nice")
    else:
        return render_template("success.html", result="oh no")
    
if __name__ == "__main__":
    app.debug = True
    app.run()                                
