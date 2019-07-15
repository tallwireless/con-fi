from flask import Flask
from flask import render_template
from flask import request

app = Flask("ConFi")


@app.route("/")
@app.route("/create", methods=["GET"])
def display_form(err_msg=[], username=None):
    data = {
        "title": "Wifi Registration",
        "subtitle": "WiFi Registration",
        "err_msg": err_msg,
        "username": username,
    }
    return render_template("create.tpl", **data)


@app.route("/configure")
def configure():
    data = {"title": "Configuration", "subtitle": "WiFi Configuration"}
    return render_template("configure.tpl", **data)


@app.route("/create", methods=["POST"])
def handle_form():
    err_msg = []

    if request.form["username"] == "":
        print("no username")
        err_msg.append("A username is required.")

    if request.form["password"] == "":
        err_msg.append("A password is required.")

    if request.form["verify_password"] == "":
        err_msg.append("Ensure you verify your password.")

    if request.form["verify_password"] != request.form["password"]:
        err_msg.append("Passwords didn't match.")

    if len(err_msg) != 0:
        return display_form(err_msg, request.form["username"])

    data = {
        "title": "Account Created",
        "subtitle": "Account Created",
        "content": render_template("created.tpl"),
    }
    return render_template("main.tpl", **data)
