#HW03

from flask import Flask, render_template
from collections import OrderedDict 
app = Flask(__name__)

from Occupations import whichOcc


@app.route("/")
def index():
	return '''<a href="http://127.0.0.1:5000">Hello </a>
        <a href="/Occupations">CLICK ME </a>
        <a href="/end">End</a>'''

#creating dictionary for occupations
data = open("occupations.csv").read()
data = data.replace(', ', '+')
data = data.replace(',', '\n').split('\n')
for x in range(0, len(data)):
    data[x] = data[x].replace('+', ', ')

occ = []
per = []

while len(data) > 1:
    occ.append(data[0])
    per.append(data[1])
    data = data[2:]

dic = OrderedDict()
count = 0
for i in occ:
    dic[i] = per[count]
    count += 1

@app.route("/Occupations")
def start():
	return render_template("app.html", dic=dic, random_job=whichOcc())


@app.route("/end")
def end():
        return '''<a href="http://127.0.0.1:5000">Hello </a>
        <a href="/Occupations">CLICK ME </a>
        <a href="/end">End</a>'''

if __name__ == "__main__":
    app.debug = True
    app.run()
