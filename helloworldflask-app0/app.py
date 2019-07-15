from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    # return "hello world"
    # getting an argument to the index file
    name = request.args.get("name", "user")
    return render_template("index.html", name=name)