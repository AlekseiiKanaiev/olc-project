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

        return "Video id: {}, title: {}".format(self.id, self.title)

class Team(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    position_ukr = db.Column(db.String(140))
    position_rus = db.Column(db.String(140))
    full_name_ukr = db.Column(db.String(140))
    full_name_rus = db.Column(db.String(140))
    img_name = db.Column(db.String(140))
    phone = db.Column(db.String(140))
    email = db.Column(db.String(140))

    def __init__(self, *args, **kwargs):
        super(Team, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "Team id: {}, full_name: {}".format(self.id, self.full_name_ukr)

class Utils(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    util_name_ukr = db.Column(db.String(140), unique = True)
    util_name_rus = db.Column(db.String(140), unique = True)

    def __init__(self, *args, **kwargs):
        super(Utils, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "Util_name: {}".format(self.util_name)

class PubInfo(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    doc_name_ukr = db.Column(db.String(140), unique = True)
    doc_name_rus = db.Column(db.String(140), unique = True)
    img_name = db.Column(db.String(140))

    def __init__(self, *args, **kwargs):
        super(PubInfo, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "PubInfo: {}".format(self.util_name)