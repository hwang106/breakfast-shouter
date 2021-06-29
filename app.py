# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
# from flask import render_template
# from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return "hello world"

@app.route('/secret')
def secret():
    return "this is a secret page"

@app.route('/jeff')
def jeff():
    return "<h1>MY NAME IS JEFF!</h1> <img src='https://media1.tenor.com/images/bdae5cd93f9ec469fdd2e27af1d7a5ed/tenor.gif?itemid=8025876'/>"