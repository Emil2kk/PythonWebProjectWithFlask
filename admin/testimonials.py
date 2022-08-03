from flask import Flask,redirect,url_for,render_template,request
from run import app
from models import db
import os
import datetime
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user
from run import login_manager



@login_manager.user_loader
def load_user(user_id):
    from models import Login
    return Login.query.get(int(user_id))

@app.route("/login",methods=["GET","POST"])
def admin_login():
    from models import Login,db
  
    login = Login(
        admin_username = "admin",
        admin_password = "admin",
        log_bool = False
    )
    db.session.add(login)
    db.session.commit()
    
    if request.method == "POST":
        if login.admin_username == request.form["admin_username"] and login.admin_password == request.form["admin_password"]:
            login_user(login, remember=login.log_bool)
            return redirect ("/admin/testimonials")

        else:
            flash ("Username or password is wrong!")
            return redirect ("/admin/login")

    return render_template("admin/login.html", login = login)


@app.route("/logout")
@login_required
def admin_logout():
    logout_user()
    return redirect ("/login")



@app.route("/admin/testimonials",methods=['POST','GET'])
@login_required
def Add_():
    from models import Testimonials
    test=Testimonials.query.all()
    if request.method=="POST":
        name=request.form['_name']
        work=request.form['_work']
        text=request.form['_text']
        test=Testimonials(name=name,work=work,text=text,test_date=datetime.datetime.now())
        db.session.add(test)
        db.session.commit()
        return redirect("/admin/testimonials")
    return render_template('admin/testimonials.html',test=test)
db.create_all()
@app.route("/admin/testimonials/delete/<int:id>")
def testimonials_delete(id):
        from models import Testimonials,db
        test=Testimonials.query.filter_by(id=id).first()
        db.session.delete(test)
        db.session.commit()
        return redirect('/testimonials')

   
@app.route("/admin/testimonials/update/<int:id>", methods=["GET", "POST"])
def testimonials_update(id):
    from models import Testimonials,db        
    test=Testimonials.query.filter_by(id=id).first()
    if request.method=="POST":
        test=Testimonials.query.filter_by(id=id).first()
        test.name=request.form['_name']
        test.work=request.form['_work']
        test.text=request.form['_text']
        db.session.commit()
        return redirect('admin/testimonials')
    return render_template('admin/testimonials_update.html',test=test)

