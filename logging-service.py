from flask import Flask, request

app = Flask(__name__)

messages = {}

@app.route("/", methods=["GET"])
def logging_get():
    return ', '.join(list(messages.values()))

@app.route("/", methods=["POST"])
def logging_post():
    messages.update(request.json)
    print(messages.values())
    return ''

app.run(host="127.0.0.1", port=1235, debug=True)