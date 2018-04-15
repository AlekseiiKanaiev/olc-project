import mysql.connector

class Configurations(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # connector = mysql.connector.connect(host = "localhost",
    #                                     # port = "3306",
    #                                     database = "test1",
    #                                     user = "root",
    #                                     password = "1")
    SQLALCHEMY_DATABASE_URI = 'sqlite:////home/family/VisualCodeProjects/New/test-project/app/test.db'
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:1@localhost/test"
    # SQLALCHEMY_DATABASE_URI = "mysql://localhost/test1"
    SECRET_KEY = 'super secret key'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'alexey.kanaev.ua@gmail.com'
    MAIL_PASSWORD = 'elylahjnvifttcjz'
    MAIL_DEFAULT_SENDER = 'alexey.kanaev.ua@gmail.com'