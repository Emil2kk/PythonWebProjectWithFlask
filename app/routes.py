from run import app
from flask import Flask,redirect,url_for,render_template,request


@app.route("/")
def portfolio():
    from models import Testimonials
    from models import Portfolio,PortfolioCategory
    from models import Services,Navlinks
    test=Testimonials.query.all()
    portfolios=Portfolio.query.all()
    categories=PortfolioCategory.query.all()
    ser=Services.query.all()
    nav=Navlinks.query.all()
    return render_template("app/index.html", test=test,ser=ser,portfolios=portfolios,categories=categories,PortfolioCategory=PortfolioCategory,nav=nav)