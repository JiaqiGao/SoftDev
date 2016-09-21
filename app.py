#HW02: Write a Flask app with 3 routes

from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
	return '''<a href="http://127.0.0.1:5000">Hello </a>
        <a href="/start">Start </a>
        <a href="/end">End</a>'''
	
@app.route("/start")
def start():
	return '''<a href="http://127.0.0.1:5000">Hello </a>
        <a href="/start">Start </a>
        <a href="/end">End</a>'''

@app.route("/end")
def end():
        return '''<a href="http://127.0.0.1:5000">Hello </a>
        <a href="/start">Start </a>
        <a href="/end">End</a>'''

if __name__ == "__main__":
	app.run()
