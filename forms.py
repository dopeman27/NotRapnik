from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Hasło', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Potwierdź hasło', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Zarejestruj się')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj się')
