from flask import Flask,redirect,url_for,render_template,request,render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
db.create_all()
f = open('templates/example.html', 'w')
  

html_template = """<html>
<head>
<title>Title</title>
</head>
<body>
    <form action="/contact" method="POST">
        <input type="text" placeholder="Your Name" name="u_name"><br>
        <input type="text" placeholder="Your Pasword" name="u_pass"><br>
        <input type="submit" value="Register">
    </form>
  
</body>
</html>
"""
f.write(html_template)
f.close()

@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=="POST":
        name=request.form['u_name']
        password=request.form['u_pass']
        msj=Password(name=name,password=password)
        db.session.add(msj)
        db.session.commit()
        
    
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(port=5000,debug=True)