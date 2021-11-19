import os

SECRET_KEY = 'A0Zr9kl;pj/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

# Local
#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
# Heroku
SQLALCHEMY_DATABASE_URI = 'postgresql://aawgcotyznyepz:94fc718866c22631ed23fb0785affe477969b840e7bc3296c3d23fef850748f0@ec2-3-209-38-221.compute-1.amazonaws.com:5432/d8fr8b6rmksa0k'


SQLALCHEMY_TRACK_MODIFICATIONS = False