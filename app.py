from flask import Flask
from flask import render_template
from flask import request

import config

from con_fi.entities import User
from con_fi import setup

app = Flask("ConFi")

# Set up the database session factory
SessionMaker = setup.setup(config)


# Handle default connections
# displays the form for user registation
@app.route("/")
@app.route("/create", methods=["GET"])
def display_form(err_msg=[], username=""):
    data = {
        "title": "Wifi Registration",
        "subtitle": "WiFi Registration",
        "err_msg": err_msg,
        "username": username,
    }
    return render_template("create.tpl", **data)


# Information on how to configure devices to connect
@app.route("/configure")
def configure():
    data = {"title": "Configuration", "subtitle": "WiFi Configuration"}
    return render_template("configure.tpl", **data)


# Handle the creation of the account in the database
@app.route("/create", methods=["POST"])
def handle_form():
    err_msg = []
    # Is all the info here?
    if request.form["username"] == "":
        err_msg.append("A username is required.")

    if request.form["password"] == "":
        err_msg.append("A password is required.")

    if request.form["verify_password"] == "":
        err_msg.append("Ensure you verify your password.")

    if request.form["verify_password"] != request.form["password"]:
        err_msg.append("Passwords didn't match.")

    if len(request.form["password"]) < 8:
        err_msg.append("Password needs to be at least 8 characters")

    # send back to form if errors
    if len(err_msg) != 0:
        return display_form(err_msg, request.form["username"])

    # Check to see if the user exists
    db_ses = SessionMaker()

    # see if username already exists
    user = db_ses.query(User).filter_by(username=request.form["username"]).one_or_none()

    if user is None:
        # User doesn't exist, and need to create it
        user = User(
            username=request.form["username"], password=request.form["password"]
        )
        db_ses.add(user)
        db_ses.commit()
        data = {
            "title": "Account Created",
            "subtitle": "Account Created",
            "username": user.username,
            "success": True,
        }
    else:
        # update the users password
        data = {
            "title": "Account Exists",
            "subtitle": "Account Exists",
            "username": user.username,
            "success": False,
        }
    return render_template("created.tpl", **data)


# Just a listing of users
@app.route("/admin/users", methods=["GET"])
def admin_list_users():
    db_ses = SessionMaker()

    db_users = db_ses.query(User).all()
    users = []
    for db_user in db_users:
        users.append(
            {"username": db_user.username, "id": db_user.id, "role": db_user.role}
        )
    data = {"title": "User Accounts", "subtitle": "User Accounts", "users": users}

    return render_template("admin/list-users.tpl", **data)
