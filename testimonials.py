from flask import Flask,redirect,url_for,render_template,request
from run import app
from models import db
import os
import datetime


@app.route("/testimonials",methods=['POST','GET'])
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
        return redirect("/testimonials")
    return render_template('testimonials.html',test=test)
db.create_all()
@app.route("/testimonials/delete/<int:id>")
def testimonials_delete(id):
        from models import Testimonials,db
        test=Testimonials.query.filter_by(id=id).first()
        db.session.delete(test)
        db.session.commit()
        return redirect('/testimonials')
    
   
@app.route("/testimonials/update/<int:id>", methods=["GET", "POST"])
def testimonials_update(id):
    from models import Testimonials,db        
    test=Testimonials.query.filter_by(id=id).first()
    if request.method=="POST":
        test=Testimonials.query.filter_by(id=id).first()
        test.name=request.form['_name']
        test.work=request.form['_work']
        test.text=request.form['_text']
        db.session.commit()
        return redirect('/testimonials')
    return render_template('testimonials_update.html',test=test)

