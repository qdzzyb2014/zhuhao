import os

DEBUG = True
SECRET_KEY = 'zhuhaowoerzi'

LOGGER_NAME = 'zhuhao'

######################
#  Database Part #####
######################
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/zhuhao'
SQLALCHEMY_TRACK_MODIFICATIONS = False

try:
    from .locale_config import *
except ImportError:
    pass
