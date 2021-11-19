import os

SECRET_KEY = 'A0Zr9kl;pj/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

# Local
#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
# Heroku
SQLALCHEMY_DATABASE_URI = 'postgresql://esuutcqyxjvwyi:a27ea3b932f83d806a10489199d9b4aec2ff081fa5b032831cfede98b321980d@ec2-54-146-82-179.compute-1.amazonaws.com:5432/db72esghmnr6pj'


SQLALCHEMY_TRACK_MODIFICATIONS = False