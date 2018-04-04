#!/usr/bin/python3.5
from datetime import datetime
import re

from app import db

# def slugify(s):

#     pattern = r"[^\w+]"
#     return re.sub(pattern, "-", s)

class Video(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(140))
    # slug = db.Column(db.String(140), unique = True)
    video_id = db.Column(db.String(140))
    body = db.Column(db.Text)
    create = db.Column(db.DateTime, default = datetime.now())

    def __init__(self, *args, **kwargs):

        super(Video, self).__init__(*args, **kwargs)
        # self.generate_slug()

    # def generate_slug(self):

    #     if self.title:
    #         self.slug = slugify(self.title)

    def __repr__(self):

        return "Video id: {}, title: {}, slug: {}".format(self.id, self.title, self.slug)


def add_video(title, body):
    new_video = Video(title = title, body = body)
    db.session.add(new_video)
    db.session.commit()

def del_video(title):
    video = Video.query.filter_by(title = title).first()
    db.session.delete(video)
    db.session.commit()

# all_video = Video.query.filter_by(slug = None).all()
# # print(all_video)
# for video in all_video:
#     video.generate_slug()
# # print(all_video)
# db.session.commit()

# db.create_all()
# del_post("The first video")
# del_video("The second video")
# 
# add_video(title = "The first video",
#         body = "UGUUhXKZ8Vk")
# add_post("First post!", "This is first post")


# for video in Video.query.all():
#     print(video.title, video.body)    