from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username=StringField("username",validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField("email",validators=[DataRequired(),Email()])
    password=PasswordField("password",validators=[DataRequired()])
    confirm_password=PasswordField("confirm password",validators=[DataRequired(),EqualTo("password")])
    submit=SubmitField("Sign Up")

        
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("The Username is alreasy taken. Please choose a different one")

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("The email is alreasy taken. Please choose a different one")
        

class LoginForm(FlaskForm):
    email=StringField("email",validators=[DataRequired(),Email()])
    password=PasswordField("password",validators=[DataRequired()])
    remember=BooleanField("Remember Me")
    submit=SubmitField("Login")


class UpdateAccountForm(FlaskForm):
    username=StringField("username",validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField("email",validators=[DataRequired(),Email()])
    picture=FileField("Update Profile Picture",validators=[FileAllowed(["jpg", "png"])])
    submit=SubmitField("Update")

        
    def validate_username(self,username):
        if username.data != current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("The Username is alreasy taken. Please choose a different one")

    def validate_email(self,email):
        if email.data != current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("The email is alreasy taken. Please choose a different one")
            

class RequestResetForm(FlaskForm):
    email=StringField("email",validators=[DataRequired(),Email()])
    submit=SubmitField("Request Password")
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError("There is no account for that Email. You must register first.")
        

class ResetPasswordForm(FlaskForm):
    password=PasswordField("password",validators=[DataRequired()])
    confirm_password=PasswordField("confirm password",validators=[DataRequired(),EqualTo("password")])
    submit=SubmitField("Reset Password")