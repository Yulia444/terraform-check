from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import EmailField


class SendReview(FlaskForm):
    author = StringField('Author: ', validators=[DataRequired('Input author'),
                         Length(max=16)])
    title = StringField('Title: ', validators=[DataRequired('Input title'),
                        Length(max=60)])
    review = TextAreaField('Details: ')


class SendLetterToSubscribers(FlaskForm):
    subject = StringField(label="Subject: ")
    summernote = TextAreaField()


class Subscribe(FlaskForm):
    email = EmailField()
