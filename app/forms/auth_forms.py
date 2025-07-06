from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, validators, ValidationError
from app.models.auth_models import User

class SignupForm(FlaskForm):
    fullname = StringField('Full Name', [
        validators.DataRequired(message='Full Name is required'),
        validators.Length(min=3, max=35, message='Full Name must be between 3 and 35 characters')
    ])
    email = EmailField('Email', [
        validators.DataRequired(message='Email is required'),
        validators.Email(message='Invalid email address')
    ])
    password = PasswordField('Password', [
        validators.DataRequired(message='Password is required'),
        validators.Length(min=6, message='Password must be at least 6 characters long')
    ])
    # confirm_password = PasswordField('Confirm Password', [
    #     validators.DataRequired(message='Please confirm your password'),
    #     validators.EqualTo('password', message='Passwords must match')
    # ])
    submit = SubmitField('Sign Up')
    
    # Custom validation for fullname
    def validate_fullname(self, field):
        if not field.data.replace(" ", "").isalpha():
            raise ValidationError('Full Name must contain only letters and spaces.')
        
    def validate_email(self, field):
        existing_user = User.query.filter_by(email=field.data).first()
        if existing_user:
            raise ValidationError('Email is already registered. Please use a different email.')
        
class SigninForm(FlaskForm):
    email = EmailField('Email', [
        validators.DataRequired(message='Email is required'),
        validators.Email(message='Invalid email address')
    ])
    password = PasswordField('Password', [
        validators.DataRequired(message='Password is required'),
        validators.Length(min=6, message='Password must be at least 6 characters long')
    ])
    submit = SubmitField('Sign In')