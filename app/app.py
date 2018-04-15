#!/usr/bin/python3.5
from flask import Flask, render_template, request
from flask_jsglue import JSGlue
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_mail import Mail

from config import Configurations

app = Flask(__name__)

app.config.from_object(Configurations)

JSGlue(app)

db = SQLAlchemy(app)

#setting migarate for db
migarate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

### ADMIN ###
admin = Admin(app)
from models import Video, Team, Utils
admin.add_views(ModelView(Video, db.session), ModelView(Team, db.session), ModelView(Utils, db.session))

mail = Mail(app)