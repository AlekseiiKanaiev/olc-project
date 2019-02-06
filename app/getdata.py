from flask import jsonify
from app import app
from models import *

# @app.route("/getData", methods = ["GET"])
# def getData():
#     video = Video.query.all().pop()
#     users = Users.query.all()
#     # return jsonify(dict(
#     #     id = video.id, 
#     #     tag = video.videotag.name, 
#     #     title = video.title, 
#     #     video_id = video.video_id, 
#     #     body = video.body,
#     #     create = video.create))
#     return jsonify([dict(
#         id = user.id, 
#         pos_ukr = user.position_ukr, 
#         pos_rus = user.position_rus, 
#         f_name_ukr = user.full_name_ukr, 
#         f_name_rus = user.full_name_rus,
#         img_name = user.img_name,
#         phone = user.phone,
#         email = user.email,
#         ) for user in users])

# # roles = [dict(name = role.name, 
# #                     desc = role.description)
# #                     for role in user.roles]

@app.route("/getMainUser", methods = ["GET"])
def getMainUser():
    main_user = Users.query.filter(Users.roles.any(Roles.name.contains('main'))).first()
    return jsonify(dict(
        id = main_user.id, 
        pos_ukr = main_user.position_ukr, 
        pos_rus = main_user.position_rus, 
        f_name_ukr = main_user.full_name_ukr, 
        f_name_rus = main_user.full_name_rus,
        img_name = main_user.img_name,
        phone = main_user.phone,
        email = main_user.email
        ))

@app.route("/getVideos", methods = ["GET"])
def getVideos():
    videos = Video.query.all()
    return jsonify([dict(
        id = video.id, 
        tag = video.videotag.name, 
        title = video.title, 
        video_id = video.video_id, 
        body = video.body,
        create = video.create)
        for video in videos])

@app.route("/getUsers", methods = ["GET"])
def getUsers():
    users = Users.query.all()
    return jsonify([dict(
        id = user.id, 
        pos_ukr = user.position_ukr, 
        pos_rus = user.position_rus, 
        f_name_ukr = user.full_name_ukr, 
        f_name_rus = user.full_name_rus,
        img_name = user.img_name,
        phone = user.phone,
        email = user.email,
        ) for user in users])

@app.route("/getServices", methods = ["GET"])
def getServices():
    services = Services.query.all()
    return jsonify([dict(
        id = service.id, 
        name_ukr = service.name_ukr, 
        name_rus = service.name_rus, 
        img_name = service.img_name, 
        type = service.servtypes.name,
        ) for service in services])
