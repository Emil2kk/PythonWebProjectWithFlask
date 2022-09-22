from flask_wtf import FlaskForm
from wtforms import StringField , TextAreaField,PasswordField,SubmitField,FileField
class ServicesForm(FlaskForm):
    img=FileField("Img")
    name_link=StringField("namelink")
    about=TextAreaField("about")
    submit=SubmitField('Add Services')

class TestimonialForm(FlaskForm):
    img=FileField("Img")
    name=StringField("name")
    work=StringField("Work")
    text=TextAreaField("text")
    submit=SubmitField('Add Testimonials')
