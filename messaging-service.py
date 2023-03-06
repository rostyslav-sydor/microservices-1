from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def messaging():
    return "Not implemented yet"

app.run(host="127.0.0.1", port=1236, debug=True)