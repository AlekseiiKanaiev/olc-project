#!/usr/bin/python3.5
from flask import render_template, request, redirect, url_for, flash
from app import app, mail
from sqlalchemy import desc
from flask_mail import Message
import re
from config import Configurations
from models import Video, Team, Utils


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

def send_email():
    name = request.form.get("inputName")
    email = request.form.get("inputEmail")
    phone = request.form.get("inputPhone")
    select = request.form.get("inputSelect")
    form_msg = request.form.get("inputMsg")
    pattern = r"\d{10}"
    if len(name.split())>1 and phone.isdigit() and re.findall(pattern, phone):
        msg = Message()
        msg.body = "Имя заказчика: "+name\
                +"\n"+"E-mail заказчика: "+email\
                +"\n"+"Номер телефона заказчика: +38"+phone\
                +"\n"+"Выбранная услуга: "+select\
                +"\n"+"Дополнительная информация: "+form_msg
        # msg.sender = "oleksii.kanaiev@gmail.com"
        msg.recipients = ["alexey.kanaev.ua@gmail.com"]
        mail.send(msg)
        return True
    return False

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
    return redirect(url_for('privatvideo'))

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
    return redirect(url_for('orendatrans'))

@app.route("/orenda/orendamest")
def orendamest():
    return render_template("orendamest.html", active = "orenda_active")

@app.route("/orenda/orendatrans")
def orendatrans():
    return render_template("orendatrans.html", active = "orenda_active")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html", active = "aboutus_active")

@app.route("/contacts", methods = ["POST", "GET"])
def contacts():
    data = get_data()
    error = None
    
    if request.method == "POST":
        error = "Не вірно заповнена форма" if data["lang"] == "ukr" else "Не правильно заполнена форма"
        if send_email():
            error = None
            flash("Повідомлення відправленно" if data["lang"] == "ukr" else "Cooбщение отправленно") 
    utils = Utils.query.all()
    if error : flash(error)
    return render_template("contacts.html",
        utils = utils, error = error, active = "contacts_active", lang = data["lang"],
        main_team = data["main_team"], url = data["url"], header_class = data["header_class"])
