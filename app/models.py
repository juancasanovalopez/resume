from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


#######################################
#   id
#     category
#     title
#     subtitle
#     location
#     period
#     description
#
#     comment here!
#######################################
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(140))
    title = db.Column(db.String(140))
    subtitle = db.Column(db.String(140))
    location = db.Column(db.String(140))
    period = db.Column(db.String(140))
    description = db.Column(db.String(140))

    def __repr__(self):
        return '<Job {}>'.format(self.title)