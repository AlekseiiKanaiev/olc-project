#!/usr/bin/python3.5
from flask import Flask, render_template, request
from flask_jsglue import JSGlue
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_babel import Babel

from config import Configurations

app = Flask(__name__)


app.config.from_object(Configurations)

JSGlue(app)

db = SQLAlchemy(app)

babel = Babel(app)


### ADMIN ###
admin = Admin(app)
from models import Video
admin.add_view(ModelView(Video, db.session))
