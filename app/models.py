from datetime import datetime
from app import db

# flask db migrate -m "Modes table"
# flask db upgrade

# A model for Positions
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String())
    title = db.Column(db.String())
    subtitle = db.Column(db.String())
    location = db.Column(db.String())

    # /!\ WARNING - Datetime Field
    period = db.Column(db.String(140))
    description = db.Column(db.String(1024))
    url = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('me.id'))

    def __repr__(self):
        return '<Job {}>'.format(self.title)

# A model for personal info
class Me(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    email = db.Column(db.String(40))
    phone = db.Column(db.String(15))

    def __repr__(self):
        return '<Me {}>'.format(self.name)

# A model for social networks
class Socialnet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    username = db.Column(db.String(60))
    url = db.Column(db.String(300))

    def __repr__(self):
        return '<SocialNet {}>'.format(self.name)
