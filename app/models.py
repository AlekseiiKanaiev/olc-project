#!/usr/bin/python3.5
from datetime import datetime
import re
from  flask_security import UserMixin, RoleMixin

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

### Flask-Security ###

#setting many-to-many 
roles_users = db.Table("roles_users",
        db.Column("user_id", db.Integer(), db.ForeignKey("users.id")),
        db.Column("role_id", db.Integer(), db.ForeignKey("roles.id"))
)

class Users(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key = True)
    position_ukr = db.Column(db.String(140))
    position_rus = db.Column(db.String(140))
    full_name_ukr = db.Column(db.String(140))
    full_name_rus = db.Column(db.String(140))
    img_name = db.Column(db.String(140), unique = True)
    phone = db.Column(db.String(140), unique = True)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship("Roles", secondary = roles_users, backref = db.backref("users", lazy = "dynamic"))

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)

class Roles(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True)
    description = db.Column(db.String(255))

    def __init__(self, *args, **kwargs):
        super(Roles, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "{}".format(self.name)