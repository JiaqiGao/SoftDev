#Jiaqi Gao
#SoftDev Pd08
#HW03

from flask import Flask, render_template
from collections import OrderedDict 
app = Flask(__name__)

from Occupations import whichOcc

############################################
#creating dictionary for occupations
data = open("static/occupationslinks.csv").read()
data = data.replace(', ', '+')
data = data.replace(',', '\n').split('\n')
for x in range(0, len(data)):
    data[x] = data[x].replace('+', ', ')
data = data[2:len(data)-2]
occ = [] #creating individual lists for occupation, percentage, and helpful link
per = []
links = [] 
while len(data) > 2:
    occ.append(data[0])
    per.append(data[1])
    links.append(data[2])
    data = data[3:]
    
dic = OrderedDict()#dictionary 
count = 0
for i in occ:
    dic.setdefault(i, [])
    #multiple values for one key by making the value a list
    dic[i].append(per[count]) 
    dic[i].append(links[count])
    count += 1

##########################################
@app.route("/")
def index():
	return '''<a href="http://127.0.0.1:5000">no </a>
        <a href="/Occupations"><h2> CLICK ME </h2> </a>
        <a href="/end">no </a>'''

@app.route("/Occupations")
def start():
	return render_template("app.html", dic=dic, random_job=whichOcc())


@app.route("/end")
def end():
        return '''<a href="http://127.0.0.1:5000">no </a>
        <a href="/Occupations"><h2> CLICK ME </h2> </a>
        <a href="/end">no </a>'''

if __name__ == "__main__":
    app.debug = True
    app.run()
