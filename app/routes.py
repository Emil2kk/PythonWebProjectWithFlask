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


@app.route("/Portfolio_details/<int:id>",methods=["GET", "POST"])
def details(id):
    from models import Portfolio,Portfolio_details
    port_id=Portfolio.query.get(id)
    portfolio_details=Portfolio_details.query.all()
    return render_template('app/portfolio-details.html',port_id=port_id,portfolio_details=portfolio_details)