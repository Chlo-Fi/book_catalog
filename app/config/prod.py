import os

DEBUG = False
SECRET_KEY='topsecret'
SQLALCHEMY_DATABASE_URI = os.eviron['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS=False