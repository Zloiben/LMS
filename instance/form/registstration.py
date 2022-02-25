from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):

    username = StringField('Имя', validators=[DataRequired()])
    email = EmailField("Почта")
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')
