from flask_wtf import FlaskForm
from wtforms import StringField , TextAreaField,PasswordField,SubmitField,FileField,IntegerField
from flask_wtf.file import FileField, FileAllowed, FileRequired
class ServicesForm(FlaskForm):
    img=FileField("Img")
    name_link=StringField("namelink")
    about=TextAreaField("about")
    submit=SubmitField('Add Services')

class TestimonialForm(FlaskForm):
    img=FileField("Img",validators=[FileAllowed(['jpg','jpeg','png'])])
    name=StringField("name")
    work=StringField("Work")
    text=TextAreaField("text")
    submit=SubmitField('Add Testimonials')
class PortfolioCategoryForm(FlaskForm):
    name=StringField('Name')
    submit=SubmitField('Add Portfolio Category')
    
class PortfolioForm(FlaskForm):
    name=StringField('Name')
    category_id=IntegerField('Category Id')
    img=FileField('Img')
    info=StringField('Info')
    submit=SubmitField('Add Portfolio')
    
class NavlinkForm(FlaskForm):
    name=StringField("name")
    url=StringField("url")
    submit=SubmitField('Add Nav')
    