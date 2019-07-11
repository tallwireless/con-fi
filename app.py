from flask import Flask
from flask import render_template, url_for
app = Flask("ConFi")


@app.route('/')
def create():
    data = { "title"   : "Wifi Registration",
             "subtitle": "WiFi Registration",
             "content" : render_template("create.tpl"),
           }
    return render_template("main.tpl",**data)

@app.route('/configure')
def configure():
    data = { "title"   : "Configuration",
             "subtitle": "WiFi Configuration",
             "content" : render_template("configure.tpl"),
           }
    return render_template("main.tpl",**data)
