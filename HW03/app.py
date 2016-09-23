#HW02: Write a Flask app with 3 routes

from flask import Flask, render_template
app = Flask(__name__)

from Occupations import whichOcc, retOcc, dat


@app.route("/")
def index():
	return '''<a href="http://127.0.0.1:5000">Hello </a>
        <a href="/start">CLICK ME </a>
        <a href="/end">End</a>'''
	
@app.route("/start")
def start():
	return '''<a href="http://127.0.0.1:5000">Hello </a>
        <a href="/start">CLICK ME </a>
        <a href="/end">End</a>'''+table()+"<br> Random Occupation: "+whichOcc()

#render_template("app.html", item=table()+"<br>"+whichOcc())

def table():
    start = '''<table style="width:100%">'''
    for i in range(23):
        start += '''<tr>
        <th>'''+retOcc('O',i)+'''</th>
        <th>'''+retOcc('P',i)+'''</th>
        </tr>'''
    end = '''</table>'''
    return start+end

@app.route("/end")
def end():
        return '''<a href="http://127.0.0.1:5000">Hello </a>
        <a href="/start">CLICK ME </a>
        <a href="/end">End</a>'''

if __name__ == "__main__":
    app.debug = True
    app.run()
