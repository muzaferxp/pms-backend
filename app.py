from flask import *
import data
app = Flask(__name__)


# default router
@app.route("/")
def index():
    return "Welcome to PMS backend APIs"



# api to return list of users
@app.route("/get-all-users")
def getAllUsers():
    return {"data" : data.users}


# api to return list of projects
@app.route("/get-all-projects")
def getAllProjects():
    return {"data" : data.projects}


# api for users login
@app.route("/login")
def login():
    return "Logged in successfully"



if __name__ == "__main__":
    app.run()

