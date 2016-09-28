#Jiaqi Gao
#SoftDev Pd08
#Presidential Debate

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
	return '''<a href="http://127.0.0.1:5000">Hello </a>'''

@app.route("/home")
def home():
	return '''<a href="http://127.0.0.1:5000">Back </a>'''


if __name__ == "__main__":
    app.debug = True
    app.run()
