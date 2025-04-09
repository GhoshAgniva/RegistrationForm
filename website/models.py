from . import db



class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    dob = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    mobile = db.Column(db.String(15), nullable=False)


