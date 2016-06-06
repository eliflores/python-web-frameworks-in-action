from wut4lunch import db

class Lunch(db.Model):
    """A single lunch"""
    id = db.Column(db.Integer, primary_key=True)
    submitter = db.Column(db.String(63))
    food = db.Column(db.String(255))