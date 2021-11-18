import os

SECRET_KEY = 'A0Zr9kl;pj/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

# Local
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)

SQLALCHEMY_TRACK_MODIFICATIONS = False