from flask import Flask
from flask import render_template, url_for
app = Flask("ConFi")


@app.route('/')
def create():
    url_for("static", filename="css/tent.css")
    url_for("static", filename="btv-logo.png")
    content = render_template("create.tpl")
    data = { "title"   : "Wifi Registration",
             "subtitle": "WiFi Registration",
             "content" : render_template("create.tpl"),
           }
    return render_template("main.tpl",**data)

@app.route('/hello3/')
def hello_world2():
        return 'Hedlo, World!'
