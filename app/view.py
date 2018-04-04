#!/usr/bin/python3.5
from flask import render_template, request
from app import app, babel
from flask_babel import gettext
from config import Configurations
from models import Video

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        value = request.data("")
        print(value)
    video = Video.query.all().pop()
    return render_template("index.html", video = video, active = "index_active")

@app.route("/galery")
def galery():
    return render_template("galery.html", active = "galery_active")

@app.route("/galery/oblvideo")
def oblvideo():
    return render_template("oblvideo.html", active = "galery_active")

@app.route("/galery/privatvideo")
def privatvideo():
    return render_template("privatvideo.html", active = "galery_active")

@app.route("/orenda")
def orenda():
    return render_template("orenda.html", active = "orenda_active")

@app.route("/orenda/orendamest")
def orendamest():
    return render_template("orendamest.html", active = "orenda_active")

@app.route("/orenda/orendatrans")
def orendatrans():
    return render_template("orendatrans.html", active = "orenda_active")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html", active = "aboutus_active")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html", active = "contacts_active")


# babel translate
@babel.localeselector
def get_local():
    return "ru"
    # return  request.accept_languages.best_match(app.config["LANGUAGES"])



@app.route("/video")
def video():
    video = Video.query.all()
    return render_template("video.html", video = video)
