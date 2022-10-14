from flask import Flask,redirect,url_for,render_template,request,abort,flash
from run import app
from models import db
import os
import datetime
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user
from run import login_manager
from admin.forms import ServicesForm,CountForm,TeamForm,TestimonialForm,PortfolioCategoryForm,PortfolioForm,NavlinkForm,Portfolio_detailsForm
from werkzeug.utils import secure_filename
import random




@login_manager.user_loader
def load_user(user_id):
    from models import Login
    return Login.query.get(int(user_id))

@app.route("/admin/login",methods=["GET","POST"])
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
            return redirect (url_for("Admin"))

        else:
            flash ("Username or password is wrong!")
            return redirect ("/admin/login")

    return render_template("admin/login.html", login = login)

@app.route("/logout")
@login_required
def admin_logout():
    logout_user()
    return redirect ("/admin/login")

@app.route("/admin")
def Admin():
    return render_template("admin/base.html")

@app.route("/admin/testimonials",methods=['POST','GET'])
@login_required
def Add_():
    from models import Testimonials
    test=Testimonials.query.all()
    testimonialForm=TestimonialForm()
    if request.method=="POST":
            file=request.files['img']
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[0]
            new_filename=f"count{random.randint(1,500)}.{extension}"
            file.save(os.path.join('static/assets/uploads',new_filename))
            name=testimonialForm.name.data
            text=testimonialForm.text.data
            img=new_filename
            work=testimonialForm.work.data
            testimonial=Testimonials(name=name,img=img,text=text,work=work)
            db.session.add(testimonial)
            db.session.commit()
            return redirect('/admin/testimonials')      
    return render_template('admin/testimonials.html',testimonialForm=testimonialForm,test=test)

@app.route("/admin/testimonials/delete/<int:id>")
def testimonial_delete(id):
        from models import Testimonials
        test=Testimonials.query.filter_by(id=id).first()
        db.session.delete(test)
        db.session.commit()
        return redirect('/admin/testimonials')


@app.route("/admin/testimonials/update/<int:id>", methods=["GET", "POST"])
def testimonials_update(id):
    from models import Testimonials,db        
    test=Testimonials.query.filter_by(id=id).first()
    testimonialForm=TestimonialForm()
    if request.method=="POST":
        test.name=testimonialForm.name.data
        test.text=testimonialForm.text.data
        test.img=testimonialForm.img.data
        test.work=testimonialForm.work.data
        db.session.add(test)
        db.session.commit()
        return redirect("/admin/testimonials")
    return render_template('admin/testimonials_update.html',testimonialForm=testimonialForm,test=test)


@app.route("/admin/Portfolio_category", methods=["GET", "POST"])
def admin_portfolio_category():
    
    from models import PortfolioCategory,db
    categories=PortfolioCategory.query.all()
    categoryForm=PortfolioCategoryForm()
    if request.method=="POST":
            name=categoryForm.name.data
            portfolio_category=PortfolioCategory(name=name)
            db.session.add(portfolio_category)
            db.session.commit()
            return redirect('/admin/Portfolio_category')
    return render_template('admin/portfolio_category.html',categoryForm=categoryForm,categories=categories)

    
@app.route("/admin/Portfolio", methods=["GET", "POST"])
def admin_portfolio():
    from models import Portfolio,PortfolioCategory,db
    portfolios=Portfolio.query.all()
    categories=PortfolioCategory.query.all()
    portfolioForm=PortfolioForm()
    if request.method=="POST":
            file=request.files['img']
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[0]
            new_filename=f"Portfolio{random.randint(1,1000)}.{extension}"
            file.save(os.path.join('static/assets/uploads',new_filename))
            name=portfolioForm.name.data
            info=portfolioForm.info.data
            img=new_filename
            category=request.form['category']
            portfolio=Portfolio(name=name,info=info,img=img,category_id=category)
            db.session.add(portfolio)
            db.session.commit()
            return redirect('/admin/Portfolio')
    return render_template('admin/portfolio.html',portfolioForm=portfolioForm,portfolios=portfolios,categories=categories,PortfolioCategory=PortfolioCategory)

@app.route("/admin/Portfolio/delete/<int:id>")
def admin_port_delete(id):
    from models import Portfolio,db
    categories=Portfolio.query.filter_by(id=id).first() 
    db.session.delete(categories)
    db.session.commit()
    return redirect('/admin/Portfolio')

@app.route("/admin/Portfolio/edit/<int:id>" ,methods=["GET", "POST"])
def admin_port_update(id):
    from models import db,Portfolio,PortfolioCategory
    portfolios=Portfolio.query.get_or_404(id)
    categories=PortfolioCategory.query.get_or_404(id)
    portfolioForm=PortfolioForm()
    if request.method=="POST":
        portfolios.category_id=request.form['category']
        portfolios.name=portfolioForm.name.data
        portfolios.info=portfolioForm.info.data
        portfolios.img=portfolioForm.img.data
        db.session.add(portfolios)
        db.session.commit()
        return redirect('/admin/Portfolio')
    return render_template('admin/portfolio_update.html',portfolioForm=portfolioForm,portfolios=portfolios,categories=categories)


@app.route("/admin/Services",methods=['POST','GET'])
def Add_services():
        servicesForm=ServicesForm()
        from models import db
        from models import Services
        ser=Services.query.all()
        if request.method=="POST":
            file=request.files['img']
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[0]
            new_filename=f"count{random.randint(1,500)}.{extension}"
            file.save(os.path.join('static/assets/uploads',new_filename))
            services=Services(
            ser_img=new_filename,
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
        ser=Services.query.get_or_404(id)
        servicesForm=ServicesForm()
        if request.method=="POST":
            ser.ser_img=servicesForm.img.data
            ser.ser_namelink=servicesForm.name_link.data
            ser.ser_about=servicesForm.about.data
            db.session.add(ser)
            db.session.commit()
            return redirect('/admin/Services')
        return render_template('admin/Services_update.html',servicesForm=servicesForm,ser=ser)
@app.route("/admin/Navlinks",methods=["GET","POST"])
def add_nav():
    from models import db,Navlinks
    nav=Navlinks.query.all()
    navlinkForm=NavlinkForm()
    if request.method=="POST":
        name=navlinkForm.name.data
        url=navlinkForm.url.data
        nav=Navlinks(name=name,url=url)
        db.session.add(nav)
        db.session.commit()
        return redirect("/admin/Navlinks")
    return render_template("admin/Navlinks.html",navlinkForm=navlinkForm,nav=nav)
@app.route("/admin/Navlinks/delete/<int:id>")
def navlinks_delete(id):
        from models import Navlinks
        nav=Navlinks.query.filter_by(id=id).first() 
        db.session.delete(nav)
        db.session.commit()
        return redirect('/admin/Navlinks')
    
@app.route("/admin/Navlinks/update/<int:id>", methods=["GET", "POST"])
def navlinks_update(id):
    from models import db,Navlinks
    nav=Navlinks.query.get_or_404(id)
    navlinkForm=NavlinkForm()
    if request.method=="POST":
            nav.name=navlinkForm.name.data
            nav.url=navlinkForm.url.data
            db.session.add(nav)
            db.session.commit()
            return redirect('/admin/Navlinks')
    return render_template('admin/Navlinks_update.html',navlinkForm=navlinkForm,nav=nav)

@app.route("/admin/Portfolio_details", methods=["GET", "POST"])
def admin_portfolio_details():
    from models import Portfolio_details,db
    portfolio_details=Portfolio_details.query.all()
    portfolio_detailsForm=Portfolio_detailsForm()
    if request.method=="POST":
            file=request.files['img']
            filename=secure_filename(file.filename)
            extension=filename.rsplit('.',1)[0]
            new_filename=f"Portfolio{random.randint(1,1000)}.{extension}"
            file.save(os.path.join('static/assets/uploads',new_filename))
            category=portfolio_detailsForm.category.data
            client=portfolio_detailsForm.client.data
            date=portfolio_detailsForm.date.data
            url=portfolio_detailsForm.url.data
            name=portfolio_detailsForm.name.data
            detail=portfolio_detailsForm.detail.data
            img=new_filename
            
            portfolio_details=Portfolio_details(category=category,client=client,date=date,name=name,url=url,img=img,detail=detail)
            db.session.add(portfolio_details)
            db.session.commit()
            return redirect('/admin/Portfolio_details')
    return render_template('admin/portfolio_details.html',portfolio_detailsForm=portfolio_detailsForm,portfolio_details=portfolio_details)


@app.route("/admin/Count",methods=["GET","POST"])
def add_count():
    from models import db,Count
    count=Count.query.all()
    countForm=CountForm()
    if request.method=="POST":
        name=countForm.name.data
        count=countForm.count.data
        about=countForm.about.data
        count=Count(name=name,count=count,about=about)
        db.session.add(count)
        db.session.commit()
        return redirect("/admin/Count")
    return render_template("admin/Count.html",countForm=countForm,count=count)
@app.route("/admin/Count/delete/<int:id>")
def count_delete(id):
        from models import Count
        count=Count.query.filter_by(id=id).first() 
        db.session.delete(count)
        db.session.commit()
        return redirect('/admin/Count')
    
@app.route("/admin/Count/update/<int:id>", methods=["GET", "POST"])
def count_update(id):
    from models import db,Count
    count=Count.query.get_or_404(id)
    countForm=CountForm()
    if request.method=="POST":
            count.name=countForm.name.data
            count.count=countForm.count.data
            db.session.add(count)
            db.session.commit()
            return redirect('/admin/Count')
    return render_template('admin/count_update.html',countForm=countForm,count=count)

@app.route("/admin/Team",methods=["GET","POST"])
def add_team():
    from models import Team
    team=Team.query.all()
    teamForm=TeamForm()
    if request.method=="POST":
        file=request.files['img']
        filename=secure_filename(file.filename)
        extension=filename.rsplit('.',1)[0]
        new_filename=f"Team{random.randint(1,500)}.{extension}"
        file.save(os.path.join('static/assets/uploads',new_filename))
        name=teamForm.name.data
        position=teamForm.position.data
        img=new_filename
        team=Team(name=name,img=img,position=position)
        db.session.add(team)
        db.session.commit()
        return redirect("/admin/Team")
    return render_template("admin/team.html",teamForm=teamForm,team=team)
@app.route("/admin/Team/delete/<int:id>")
def delete_team(id):
    from models import Team
    team=Team.query.filter_by(id=id).first() 
    db.session.delete(team)
    db.session.commit()
    return redirect('/admin/Team')
@app.route("/admin/Team/update/<int:id>")
def update_team(id):
    from models import Team
    team=Team.query.get_or_404(id)
    teamForm=TeamForm()
    if request.method=="POST":
            team.img=teamForm.img.data
            team.name=teamForm.name.data
            team.position=teamForm.position.data
            db.session.add(team)
            db.session.commit()
            return redirect('/admin/Team')
    return render_template('admin/team_update.html',teamForm=teamForm,team=team)
db.create_all()
