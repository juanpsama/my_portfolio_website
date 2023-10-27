from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField

class ContactForm(FlaskForm):
    name = StringField('Your name', validators=[DataRequired()])
    email = StringField('Your mail', validators=[DataRequired(), Email()])
    phone = StringField('Phone')
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField('Send Message')