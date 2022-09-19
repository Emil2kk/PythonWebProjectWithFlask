from flask import Flask,redirect,url_for,render_template,request
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = b'ZT\x1a>\x99\x12\xe5\x8bhs\x9e\xbc\xa8\xa3s\x86\x041\xd3\xcf\x8d\xbb1\x99'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "admin_login"
from admin.routes import *
from app.routes import *

if __name__ == '__main__':
    app.run(port=5000,debug=True)