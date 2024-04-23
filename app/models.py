from . import db

class BoroughCount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borough = db.Column(db.String(50), nullable=False)
    total = db.Column(db.Integer, nullable=False)