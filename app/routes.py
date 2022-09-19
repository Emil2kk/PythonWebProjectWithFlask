from run import app
from flask import Flask,redirect,url_for,render_template,request


@app.route("/")
def portfolio():
    from models import Testimonials
    from models import Portfolio
    from models import Services
    test=Testimonials.query.all()
    port=Portfolio.query.all()
    ser=Services.query.all()
    return render_template("app/index.html", test=test,port=port,ser=ser)