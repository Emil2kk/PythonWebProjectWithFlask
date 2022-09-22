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
    
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    member_img=db.Column(db.String(200))
    member_social_link=db.Column(db.String(200))
    member_social_icon=db.Column(db.String(200))
    member_name= db.Column(db.String(200))
    member_job= db.Column(db.String(250))
    
class About(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    about_icon=db.Column(db.String(200))
    about_work=db.Column(db.String(200))
    about_quickread=db.Column(db.String(200))
    
class NavBar(db.Model):
    id =db.Column(db.Integer, primary_key=True, autoincrement=True)
    navbar_item=db.Column(db.String(200))
    navbar_item_link=db.Column(db.String(200))

class Login(UserMixin ,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    admin_username = db.Column(db.String(50))
    admin_password = db.Column(db.String(50))
    log_bool = db.Column(db.Boolean)
    
class Portfolio(db.Model):
    id =db.Column(db.Integer, primary_key=True, autoincrement=True)
    port_img=db.Column(db.String(200))
    port_name=db.Column(db.String(200))
    port_mname=db.Column(db.String(200))
    
# class Portfolio_details(db.Model):
     
    
