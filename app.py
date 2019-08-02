from flask import Flask
from flask import render_template
from flask import request
from flask import send_file

# For Captcha Generation
from PIL import Image, ImageDraw, ImageFont
import io

from con_fi import config

from con_fi.entities import User
from con_fi import setup
from con_fi import Captcha


app = Flask("ConFi")

# Try and setup the database

# Set up the database session factory
@app.before_first_request
def app_setup():
    app.logger.info("Starting App Setup...")
    setup.setup()
    config.captcha = Captcha(config.APP_KEY)


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
        "captcha": str(config.captcha.generate_text()),
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

    validchars = "abcdefghijklmnopqrstuvwxyz0123456789"
    for i in request.form["username"].lower():
        if i not in validchars:
            err_msg.append("Invalid character in username")
            break

    if request.form["password"] == "":
        err_msg.append("A password is required.")

    if request.form["verify_password"] == "":
        err_msg.append("Ensure you verify your password.")

    if request.form["verify_password"] != request.form["password"]:
        err_msg.append("Passwords didn't match.")

    if len(request.form["password"]) < 8:
        err_msg.append("Password needs to be at least 8 characters")

    # validate the captcha
    text = config.captcha.decode_text(request.form["encrypt"])
    if request.form["captcha"].upper() != text:
        err_msg.append("Captcha incorrect")

    # send back to form if errors
    if len(err_msg) != 0:
        return display_form(err_msg, request.form["username"])

    # Check to see if the user exists
    db_ses = config.SessionMaker()

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
    db_ses = config.SessionMaker()

    db_users = db_ses.query(User).all()
    users = []
    for db_user in db_users:
        users.append(
            {"username": db_user.username, "id": db_user.id, "role": db_user.role}
        )
    data = {"title": "User Accounts", "subtitle": "User Accounts", "users": users}

    return render_template("admin/list-users.tpl", **data)


@app.route("/captcha.png", methods=["GET"])
def generate_catcha():

    text = config.captcha.decode_text(request.args.get("t"))
    output = io.BytesIO()

    font = ImageFont.truetype("./broken.ttf", 110)
    img = Image.new("RGB", (400, 100), color="white")
    drawer = ImageDraw.Draw(img)
    drawer.text((45, -15), text, fill=(0, 0, 0), font=font)

    img.save(output, format="png")
    output.seek(0)

    return send_file(output, mimetype="image/png", attachment_filename="logo.png")
