import json
from flask import Flask

app = Flask(__name__)

def getAuthor ():
    with open("data.json", "r") as file:
        data=json.load(file)
        return data["Author"]

@app.route("/")
def hello_world():
    return f"<p>Hello, {getAuthor()}!</p>"
