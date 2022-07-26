from run import app
from flask import Flask,redirect,url_for,render_template,request


@app.route("/")
def index():
    from models import Testimonials
    from models import Portfolio,PortfolioCategory
    from models import Services,Navlinks,Count,Team,Hero,Clients,Features,Contact
    test=Testimonials.query.all()
    portfolios=Portfolio.query.all()
    categories=PortfolioCategory.query.all()
    team=Team.query.all()
    ser=Services.query.all()
    nav=Navlinks.query.all()
    count=Count.query.all()
    hero=Hero.query.all()
    clients=Clients.query.all()
    features=Features.query.all()
    messages=Contact.query.all()
    
    return render_template("app/index.html",messages=messages,features=features,clients=clients,hero=hero,team=team,test=test,count=count,ser=ser,portfolios=portfolios,categories=categories,PortfolioCategory=PortfolioCategory,nav=nav)


@app.route("/Portfolio_details/<int:id>",methods=["GET", "POST"])
def details(id):
    from models import Portfolio,Portfolio_details
    
    portfolio_details=Portfolio_details.query.filter_by(portfolio_id=id).all()
    return render_template('app/portfolio-details.html',portfolio_details=portfolio_details)