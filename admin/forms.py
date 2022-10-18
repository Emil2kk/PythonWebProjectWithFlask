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
    
class Portfolio_detailsForm(FlaskForm):
    category=StringField('category')
    client=StringField('client')
    img=FileField('Img')
    date=StringField('Date')
    url=StringField('url')
    name=StringField('name')
    detail=StringField('detail')
    submit=SubmitField('Add details')
    
class NavlinkForm(FlaskForm):
    name=StringField("name")
    url=StringField("url")
    submit=SubmitField('Add Nav')
    
class CountForm(FlaskForm):
    count=StringField("count")
    name=StringField("name")
    about=StringField("about")
    submit=SubmitField('Add Count')
    
class TeamForm(FlaskForm):
    img=FileField("img")
    name=StringField("name")
    position=StringField("Position")
    submit=SubmitField("add Team")
    
    
class HeroForm(FlaskForm):
    name=StringField("name")
    link=StringField("Link")
    icon=StringField("Icon name")
    submit=SubmitField("add Hero")
    
class ClientForm(FlaskForm):
     img=FileField("img")
     submit=SubmitField("add Client")
     