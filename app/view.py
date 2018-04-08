#!/usr/bin/python3.5
from flask import render_template, request, redirect, url_for
from app import app, babel
from flask_babel import gettext
from config import Configurations
from models import Video

# # babel translate
# @babel.localeselector
# def get_local():
#     return "ru"
# #     return "uk"
#     # return  request.accept_languages.best_match(app.config["LANGUAGES"])

def get_data(simple = True):
    if request.args.get("lang"):
        language = request.args.get("lang")
    else:
        language = "ukr"
    url = request.path
    header_class = "my-simple-header" if simple else "my-header"
    return dict(lang = language, url = url, header_class = header_class)

@app.route("/", methods = ["GET", "POST"])
def index():
    return redirect(url_for('main'))

@app.route("/golovna", methods = ["GET", "POST"])
def main():
    data = get_data(simple=False)
    video = Video.query.all().pop()
    return render_template("index.html",
        video = video, active = "index_active", lang = data["lang"], 
        url = data["url"], header_class = data["header_class"])

@app.route("/galery")
def galery():
    return render_template("galery.html", active = "galery_active")

@app.route("/galery/oblvideo")
def oblvideo():
    data = get_data()
    return render_template("oblvideo.html", 
        active = "galery_active", lang = data["lang"], url = data["url"], header_class = data["header_class"])

@app.route("/galery/privatvideo")
def privatvideo():
    data = get_data()
    return render_template("privatvideo.html", 
        active = "galery_active", lang = data["lang"], url = data["url"], header_class = data["header_class"])

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


@app.route("/video")
def video():
    video = Video.query.all()
    return render_template("video.html", video = video)
