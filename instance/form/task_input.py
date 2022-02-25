from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import SubmitField, FileField


class TaskInputFile(FlaskForm):

    file = FileField('Приложите файл с решением', validators=[FileRequired()])
    submit = SubmitField('Войти')
