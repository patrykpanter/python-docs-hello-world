from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Great World! <br/> And a Happy New Year!"
