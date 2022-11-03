from flask import Flask
from data import users
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

@app.route("/get-biryani")
def getBiryani():
    return "Here is your garma garam biryani"

@app.route("/get-all-users")
def getAllUsers():
    return {"users" : users}


@app.route("/get-time")
def getTime():
    return {"time" : datetime.now()}

if __name__ == "__main__":
    app.run()