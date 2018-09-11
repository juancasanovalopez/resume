from datetime import datetime
from app import db

# flask db migrate -m "Modes table"
# flask db upgrade

# A model for Positions
# TODO: Add url field
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String())
    title = db.Column(db.String())
    subtitle = db.Column(db.String())
    location = db.Column(db.String())

    # /!\ WARNING - Datetime Field
    period = db.Column(db.String(140))
    description = db.Column(db.String(1024))

    def __repr__(self):
        return '<Job {}>'.format(self.title)

# A model for personal info
class Me(db.Model):
    Name = db.Column(db.String(140), primary_key=True)
    email = db.Column(db.String(60))
    phone = db.Column(db.String(60))

    def __repr__(self):
        return '<Me {}>'.format(self.Name)

# A model for social networks
class Social(db.Model):
    network = db.Column(db.String(140), primary_key=True)
    username = db.Column(db.String(60))
    url = db.Column(db.String(60))

    def __repr__(self):
        return '<Me {}>'.format(self.Name)