from flask import Flask,redirect,url_for,render_template,request


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
from testimonials import *





if __name__ == '__main__':
    app.run(port=5000,debug=True)