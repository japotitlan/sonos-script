#
# Practica para comprender como funciona el framework Flask
#

from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "Patucasa caon ya jalo el flasc"

app.run(host="0.0.0.0", port=80)