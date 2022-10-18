from run import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Column, DateTime, String
import datetime
from flask_login.mixins import UserMixin
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Testimonials(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img=db.Column(db.String(200))
    name = db.Column(db.String(50))
    work = db.Column(db.String(50))
    text = db.Column(db.String(100))
    test_date = db.Column(DateTime(timezone=True), server_default=str(datetime.datetime.now()))
    
    
class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ser_img=db.Column(db.String(200))
    ser_namelink = db.Column(db.String(200))
    ser_about=db.Column(db.String(200))
    

    
class About(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    about_icon=db.Column(db.String(200))
    about_work=db.Column(db.String(200))
    about_quickread=db.Column(db.String(200))
    
class Navlinks(db.Model):
    id =db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(200))
    url=db.Column(db.String(200))

class Login(UserMixin ,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    admin_username = db.Column(db.String(50))
    admin_password = db.Column(db.String(50))
    log_bool = db.Column(db.Boolean)
    
class PortfolioCategory(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(80))
    portfolios = db.relationship('Portfolio', backref='portfolio_category', lazy=True)
    
    
class Portfolio(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(80))
    category_id=db.Column(db.Integer,db.ForeignKey('portfolio_category.id'))
    img=db.Column(db.String(80))
    info=db.Column(db.String(200))
    portfo = db.relationship('Portfolio_details', backref='portfolio', lazy=True)
    
    
class Portfolio_details(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    category=db.Column(db.String(80))
    client=db.Column(db.String(200))
    date=db.Column(db.String(100))
    url=db.Column(db.String(200))
    img=db.Column(db.String(80))
    name=db.Column(db.String(80))
    detail=db.Column(db.String(120))
    portfolio_id=db.Column(db.Integer,db.ForeignKey('portfolio.id'))

    
class Count(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    count=db.Column(db.String(20))
    name=db.Column(db.String(200))
    about=db.Column(db.String(200))
    
    
class Team(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    img=db.Column(db.String(80))
    name=db.Column(db.String(80))
    position=db.Column(db.String(80))
    
class Hero(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(80))
    link=db.Column(db.String(80))
    icon=db.Column(db.String(80))
    
    
class Clients(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    img=db.Column(db.String(80))