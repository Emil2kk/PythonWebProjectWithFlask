from run import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
class Testimonials(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    work = db.Column(db.String(50))
    text = db.Column(db.String(100))