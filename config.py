import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # SQL Alchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # HEFENG weather API token key
    HEFENG_KEY = '761cdaa96615403e89973211848655d6'
