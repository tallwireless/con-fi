from flask import Flask
from flask import render_template
from flask import request

from con_fi.entities import User
from con_fi.db import SessionMaker
from con_fi import setup

app = Flask("ConFi")

setup.setup()


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
    # Is all the info here?
    if request.form["username"] == "":
        print("no username")
        err_msg.append("A username is required.")

    if request.form["password"] == "":
        err_msg.append("A password is required.")

    if request.form["verify_password"] == "":
        err_msg.append("Ensure you verify your password.")

    if request.form["verify_password"] != request.form["password"]:
        err_msg.append("Passwords didn't match.")

    # send back to form if errors
    if len(err_msg) != 0:
        return display_form(err_msg, request.form["username"])

    # Check to see if the user exists
    db_ses = SessionMaker()

    user = (
        db_ses.query(User.username)
        .filter_by(username=request.form["username"])
        .one_or_none()
    )

    if user is None:
        # User doesn't exist, and need to create it
        user = User(
            username=request.form["username"], password=request.form["password"]
        )
        db_ses.add(user)
        db_ses.commit()
    else:
        # update the users password
        user.password = request.form["password"]
        db_ses.commit()

    data = {
        "title": "Account Created",
        "subtitle": "Account Created",
        "content": render_template("created.tpl"),
    }
    return render_template("main.tpl", **data)
