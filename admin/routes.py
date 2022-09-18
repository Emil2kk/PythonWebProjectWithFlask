from flask import Flask,redirect,url_for,render_template,request
from run import app
from models import db
import os
import datetime
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user
from run import login_manager
from admin.forms import ServicesForm



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
        return redirect('admin/testimonials')

   
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

@app.route("/admin/Portfolio",methods=['POST','GET'])
@login_required
def Portfolio_Add():
    from models import Portfolio
    import os
    from werkzeug.utils import secure_filename
    port=Portfolio.query.all()
    if request.method=="POST":
        file = request.files['port_img']
        filename = secure_filename(file.filename)
        file.save(os.path.join('static/assets/uploads', filename))
        port_name=request.form['port_name']
        port_mname=request.form['port_mname']
        port=Portfolio(port_img=os.path.join('static/assets/uploads', filename),port_name=port_name,port_mname=port_mname)
        db.session.add(port)
        db.session.commit()
        return redirect("/admin/Portfolio")
    return render_template('admin/portfolio.html',port=port)

@app.route("/admin/Portfolio/delete/<int:id>")
def portfolio_delete(id):
        from models import Portfolio
        port=Portfolio.query.filter_by(id=id).first()
        db.session.delete(port)
        db.session.commit()
        return redirect('/Portfolio')

   
@app.route("/admin/Portfolio/update/<int:id>", methods=["GET", "POST"])
def Portfolio_update(id):
    from models import Portfolio,db        
    port=Portfolio.query.filter_by(id=id).first()
    if request.method=="POST":
        port=Portfolio.query.filter_by(id=id).first()
        port.port_name=request.form['port_name']
        port.port_mname=request.form['port_mname']
    
        db.session.commit()
        return redirect('admin/Portfolio')
    return render_template('admin/Portfolio_update.html',port=port)



@app.route("/admin/Services",methods=['POST','GET'])
def Add_services():
        servicesForm=ServicesForm()
        from models import db
        from models import Services
        ser=Services.query.all()
        if request.method=="POST":

            services=Services(
            ser_img=servicesForm.img.data,
            ser_namelink=servicesForm.name_link.data,
            ser_about=servicesForm.about.data,
            )
            db.session.add(services)
            db.session.commit()
            return redirect('/admin/Services')
        return render_template('admin/Services.html',servicesForm=servicesForm,ser=ser)
    
@app.route("/admin/Services/delete/<int:id>")
def services_delete(id):
        from models import Services
        ser=Services.query.filter_by(id=id).first()
        db.session.delete(ser)
        db.session.commit()
        return redirect('/admin/Services')
    
@app.route("/admin/Services/update/<int:id>", methods=["GET", "POST"])
def update_services(id):
    
        
        from models import db
        from models import Services
        ser=Services.query.filter_by(id=id).first()
        servicesForm=ServicesForm()
        if request.method=="POST":
            ser.ser_img=servicesForm.img.data,
            ser.ser_namelink=servicesForm.name_link.data,
            ser.ser_about=servicesForm.about.data
            db.session.commit()
            return redirect('/admin/Services')
        return render_template('admin/Services_update.html',servicesForm=servicesForm,ser=ser)