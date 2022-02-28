from flask import Blueprint
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, PasswordField, SubmitField, EmailField, FileField, BooleanField
from wtforms.validators import DataRequired


form = Blueprint('form', __name__)


class LoginFrom(FlaskForm):

    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class TaskInputFile(FlaskForm):

    file = FileField('Приложите файл с решением', validators=[FileRequired()])
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):

    username = StringField('Имя', validators=[DataRequired()])
    email = EmailField("Почта")
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class RestoreAccountForm(FlaskForm):

    email = EmailField("Почта")
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')
