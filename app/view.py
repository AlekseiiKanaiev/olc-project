#!/usr/bin/python3.5
from flask import render_template, request, redirect, url_for
from app import app
from sqlalchemy import desc
# from flask_babel import gettext
from config import Configurations
from models import Video, Team

# # babel translate
# @babel.localeselector
# def get_local():
#     return "ru"
# #     return "uk"
#     # return  request.accept_languages.best_match(app.config["LANGUAGES"])

def get_data(simple = True):
    language = request.args.get("lang")
    if language and language == "rus":
        lang = language
    else:
        lang = "ukr"
    url = request.path
    header_class = "my-simple-header" if simple else "my-header"
    main_team = Team.query.filter_by(position_ukr="Директор").first()
    return dict(lang = lang, url = url, header_class = header_class, main_team = main_team)

@app.route("/", methods = ["GET", "POST"])
def index():
    return redirect(url_for('main'))

@app.route("/golovna", methods = ["GET", "POST"])
def main():
    data = get_data(simple=False)
    video = Video.query.all().pop()
    team = Team.query.all()
    return render_template("index.html",
        video = video, team = team, active = "index_active", lang = data["lang"],  
        main_team = data["main_team"], url = data["url"], header_class = data["header_class"])

@app.route("/galery")
def galery():
    return render_template("galery.html", active = "galery_active")

@app.route("/galery/oblvideo")
def oblvideo():
    data = get_data()
    page = request.args.get("page")
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    video = Video.query.filter(Video.title.contains("oblvideo")).order_by(Video.id.desc())
    pages = video.paginate(page = page, per_page = 3)
    return render_template("oblvideo.html", 
        video = video, pages = pages, active = "galery_active", lang = data["lang"],
        main_team = data["main_team"], url = data["url"], header_class = data["header_class"])

@app.route("/galery/privatvideo")
def privatvideo():
    data = get_data()
    page = request.args.get("page")
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    video = Video.query.filter(Video.title.contains("privatvideo")).order_by(Video.id.desc())
    pages = video.paginate(page = page, per_page = 3)
    return render_template("privatvideo.html", 
        video = video, pages = pages, active = "galery_active", lang = data["lang"],
        main_team = data["main_team"], url = data["url"], header_class = data["header_class"])

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
    data = get_data()

    return render_template("contacts.html", active = "contacts_active", lang = data["lang"],
        main_team = data["main_team"], url = data["url"], header_class = data["header_class"])
