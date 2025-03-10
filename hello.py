from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
    return ("<h1> Welcome to Home page</h1>")

@app.route("/ping",methods = ['GET'])
def ping_page():
    return ("This is a <h1>PING PAGE</h1>")


