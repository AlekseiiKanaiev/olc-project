#!/usr/bin/python3.5
from flask import Flask, render_template, request, redirect, url_for
from flask_jsglue import JSGlue
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_mail import Mail
from flask_security import SQLAlchemyUserDatastore, Security, current_user

from config import Configurations

app = Flask(__name__)

app.config.from_object(Configurations)

JSGlue(app)

db = SQLAlchemy(app)

#setting migarate for db
migarate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

mail = Mail(app)

### ADMIN ###
from models import *

class AdminMixin():
    
    def is_accessible(self):
        return  current_user.has_role('redactor') or\
                current_user.has_role("admin") or\
                current_user.has_role("main")

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("security.login", next = request.url))

class AdminView(AdminMixin, ModelView):
    pass

class HomeAdminView(AdminMixin, AdminIndexView):
    pass

# class RedactorView(ModelView):
#     def is_accessible(self):
#         return  current_user.has_role('redactor') or\
                
#                 current_user.has_role("main")

#     def inaccessible_callback(self, name, **kwargs):
#         return redirect(url_for("security.login", next = request.url))

class MainView(ModelView):
    def is_accessible(self):
        return  current_user.has_role("admin") or\
                current_user.has_role('main')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("security.login", next = request.url))

admin = Admin(app, "Home", url = "/", index_view = HomeAdminView('Home'))
admin.add_views(AdminView(Video, db.session), AdminView(Utils, db.session), AdminView(PubInfo, db.session))
admin.add_views(MainView(Users, db.session), MainView(Roles, db.session))

### Flask-Security ###

user_datastore = SQLAlchemyUserDatastore(db, Users, Roles)
security = Security(app, user_datastore)
