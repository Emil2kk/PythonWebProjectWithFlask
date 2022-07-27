from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
class Testimonials(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # img = db.Column(db.String(200))
    name = db.Column(db.String(50))
    work = db.Column(db.String(50))
    text = db.Column(db.String(100))
# db.create_all()

@app.route('/',methods=['GET','POST'])
def demo():
    test=Testimonials.query.all()
    return render_template('index.html',test=test)


    
@app.route("/testimonials",methods=['POST','GET'])
def Add_():
    if request.method=="POST":
        # file=request.files['_img']
        # filename=file.filename
        # file.save(os.path.join('static/uploads/',filename))
        name=request.form['_name']
        work=request.form['_work']
        text=request.form['_text']
        test=Testimonials(name=name,work=work,text=text)
        db.session.add(test)
        db.session.commit()
        return render_template('testimonials.html',test=test)
    return render_template('testimonials.html')
if __name__ == '__main__':
    app.run(port=5000,debug=True)