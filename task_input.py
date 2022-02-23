from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired


class TaskInput(FlaskForm):

    file = FileField('Приложите файл с решением', validators=[FileRequired()])
    submit = SubmitField('Войти')
