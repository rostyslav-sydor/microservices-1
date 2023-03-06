import requests
from uuid import uuid1
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def facade_get():
    log = requests.get(url="http://127.0.0.1:1235/")
    msg = requests.get(url="http://127.0.0.1:1236/")
    return log.text + ", " + msg.text

@app.route("/", methods=["POST"])
def facade_post():
    data = {str(uuid1()): request.json["msg"]}
    r = requests.post(url="http://127.0.0.1:1235/", json=data)
    return r.text

app.run(host="127.0.0.1", port=1234, debug=True)