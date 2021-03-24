from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from application.models import User

#class RegisterForm(FlaskForm):

   # def validate_email(self, email_to_check):
    #    email = User.query.filter_by(email=email_to_check.data).first()
     #   if email:
      #      raise ValidationError("Email already registered")

    #first_name = StringField(label="First Name", validators=[Length(min=2,max=30), DataRequired()])
    #last_name = StringField(label="Last Name", validators=[Length(min=2,max=30), DataRequired()])
    #email = StringField(label="Email Address", validators=[Email(), DataRequired()])
    #password1 = PasswordField(label="Enter Password", validators=[Length(min=8), DataRequired()])
    #password2 = PasswordField(label="Confirm Password", validators=[EqualTo("password1"), DataRequired()])
    #submit = SubmitField(label="Register")

#class LoginForm(FlaskForm):
 #   email = StringField(label="Email", validators=[DataRequired()])
  #  password = PasswordField(label="Password", validators=[DataRequired()])
   # submit = SubmitField(label="Login in")


class UserForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email_address = StringField('Email Address')
    submit = SubmitField('Add User')

class GameForm(FlaskForm):
    game_title = StringField("Game Title", validators=[Length(min=2,max=30), DataRequired()])
    owner = StringField("Name")
    submit = SubmitField("Add Game")