#!/usr/bin/python3.5
from flask import render_template, request, redirect, url_for, flash
from app import app, mail
from sqlalchemy import desc
from flask_mail import Message
import re
from config import Configurations
from models import *
from flask_security import login_required

def get_data(simple = True):
    language = request.args.get("lang")
    if language and language == "rus":
        lang = language
    else:
        lang = "ukr"
    header_class = "my-simple-header" if simple else "my-header"
    main_user = Users.query.filter(Users.roles.any(Roles.name.contains('main'))).first()
    return dict(lang = lang, header_class = header_class, main_user = main_user)

def send_email(recipient = None):
    name = request.form.get("inputName")
    email = request.form.get("inputEmail")
    phone = request.form.get("inputPhone")
    select = request.form.get("inputSelect")
    form_msg = request.form.get("inputMsg")
    pattern = r"\d{10}"
    if re.findall(pattern, phone):
        msg = Message()
        msg.subject = "ОЛЦ заказ"
        msg.body = "Имя заказчика: "+name\
                +"\n"+"E-mail заказчика: "+email\
                +"\n"+"Номер телефона заказчика: +38"+phone\
                +"\n"+"Выбранная услуга: "+select\
                +"\n"+"Дополнительная информация: "+form_msg
        # msg.sender = "oleksii.kanaiev@gmail.com"
        msg.recipients = [recipient]
        # msg.recipients = ["alexey.kanaev.ua@gmail.com" if not recipient else recipient]
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
    team = Users.query.all()
    return render_template("index.html",
        video = video, team = team, active = "index_active", lang = data["lang"],  
        main_user = data["main_user"], header_class = data["header_class"])

@app.route("/gallery")
def gallery():
    return redirect(url_for('video_gallery', video_type = "privatvideo")) 

@app.route("/gallery/<video_type>")
def video_gallery(video_type):
    data = get_data()
    print(data)
    page = request.args.get("page")
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    video = Video.query.filter(Video.videotag.has(VideoTags.name.contains(video_type))).order_by(Video.id.desc())
    pages = video.paginate(page = page, per_page = 3)
    return render_template(video_type+".html", 
            pages = pages, active = "gallery_active", lang = data["lang"],
            main_user = data["main_user"], header_class = data["header_class"])

@app.route("/orenda")
def orenda():
    return redirect(url_for('orenda_service', orenda_type = "orendatrans"))

@app.route("/orenda/<orenda_type>")
def orenda_sevice(orenda_type):
    data = get_data()
    if orenda_type == "orendatrans":
        photos = Services.query.filter(Services.servtypes.has(ServTypes.name.contains('photo-transport'))).all()
    else:
        photos = Services.query.filter(Services.servtypes.has(ServTypes.name.contains('photo-realty'))).all()
    return render_template(orenda_type+".html", active = "orenda_active", lang = data["lang"],
        main_user = data["main_user"], header_class = data["header_class"], photos = photos)

@app.route("/aboutus")
def aboutus():
    data = get_data()
    team = Users.query.all()
    pubinfo = Services.query.filter(Services.servtypes.has(ServTypes.name.contains('document'))).all()
    return render_template("aboutus.html",
        team = team, pubinfo = pubinfo, active = "aboutus_active", lang = data["lang"],
        main_user = data["main_user"], header_class = data["header_class"])

@app.route("/contacts", methods = ["POST", "GET"])
def contacts():
    data = get_data()
    error = None
    if request.method == "POST":
        error = "Неправильно заповнена форма" if data["lang"] == "ukr" else "Неправильно заполнена форма"
        if send_email(data["main_user"].email):
            error = None
            flash("Повідомлення відправленно" if data["lang"] == "ukr" else "Cooбщение отправленно") 
    services = Services.query.filter(Services.servtypes.has(ServTypes.name.contains('service'))).all()
    if error : flash(error)
    return render_template("contacts.html",
        services = services, error = error, active = "contacts_active", lang = data["lang"],
        main_user = data["main_user"], header_class = data["header_class"])
