from flask import Flask
from flask import render_template

app = Flask("ConFi")


@app.route("/")
@app.route("/create", methods=["GET"])
def display_form():
    data = {
        "title": "Wifi Registration",
        "subtitle": "WiFi Registration",
        "content": render_template("create.tpl"),
    }
    return render_template("main.tpl", **data)


@app.route("/configure")
def configure():
    data = {
        "title": "Configuration",
        "subtitle": "WiFi Configuration",
        "content": render_template("configure.tpl"),
    }
    return render_template("main.tpl", **data)


@app.route("/create", methods=["POST"])
def handle_form():
    data = {
        "title": "Wifi Registration",
        "subtitle": "WiFi Registration",
        "content": "You created something!",
    }
    return render_template("main.tpl", **data)
