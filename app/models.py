from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# flask db migrate -m "Modes table"
# flask db upgrade
#

#######################################
#   id -  pk
#     category
#     title
#     subtitle
#     location
#     period
#     description
#
#     comment here!
#     j = Jobs(category='',title='',subtitle='',location='',period='',description='')
#######################################
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(140))
    title = db.Column(db.String(140))
    subtitle = db.Column(db.String(140))
    location = db.Column(db.String(140))
    period = db.Column(db.String(140))
    description = db.Column(db.String(1024))

    def __repr__(self):
        return '<Job {}>'.format(self.title)

class Me(db.Model):
    Name = db.Column(db.String(140), primary_key=True)
    email = db.Column(db.String(60))
    phone = db.Column(db.String(60))

    def __repr__(self):
        return '<Me {}>'.format(self.Name)