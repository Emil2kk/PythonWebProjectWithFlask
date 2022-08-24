from flask_wtf import FlaskForm
from wtforms import StringField , TextAreaField,PasswordField,SubmitField
class ServicesForm(FlaskForm):
    img=StringField("Img")
    name_link=StringField("namelink")
    about=TextAreaField("about")
    submit=SubmitField('Add Services')