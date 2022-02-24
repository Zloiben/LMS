import os

from flask import Flask, render_template, redirect, url_for, make_response, request
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

from login import LoginFrom
from registstration import RegistrationForm
from task_input import TaskInputFile

from testing import Testing
from instance.function.cheking import allowed_file
from config import UPLOAD_FOLDER


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
db = SQLAlchemy(app)


class Teacher(db.Model):

    id = db.Column('teacher_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(50))
    email = db.Column(db.String(100))
    data = db.Column(db.TEXT())

    def __repr__(self):
        return '<Teacher %r>' % self.name


class Students(db.Model):

    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(50))
    email = db.Column(db.String(100))
    data = db.Column(db.TEXT())

    def __init__(self, name, password, email, data):

        self.name = name
        self.password = password
        self.email = email
        self.data = data

    def __repr__(self):
        return '<User %r>' % self.name


db.create_all()


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        return redirect('/courses')
    return render_template('verification.html', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    # TODO: Проверка почты в бд
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.password.data == form.password2.data:
            db.session.add(Students(form.username.data, form.password.data, form.email.data, '{}'))
            db.session.commit()
            return redirect('/courses')
        else:
            # TODO: Должно что то выводить
            print("ERROR")
    return render_template('registration.html', form=form)


@app.route('/courses')
def courses():
    result = make_response(render_template('courses.html'))
    result.headers.values()
    return result


@app.route('/courses/lessons')
def lessons():
    return render_template('lessons.html')


@app.route('/courses/lessons/lesson/<lesson>')
def lesson(lesson):
    return render_template(f'lessons/{lesson}/lesson-1.html')


@app.route('/courses/lessons/lesson/<lesson>/tasks/<task>',  methods=['GET', 'POST'])
def tasks(lesson, task):
    file_path = f'lessons/{str(lesson)}/tasks/{str(task)}.html'
    form = TaskInputFile()
    if form.validate_on_submit():
        f = form.file.data
        if allowed_file(f.filename):
            filename = f"test_file_{task}.py"
            filename = secure_filename(filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f'lesson_{lesson}', filename))
            result = Testing(lesson, task)
            return render_template(file_path, form=form, score=result.test())

        else:
            print("Не верный формат файла")

    return render_template(file_path, form=form)


@app.route('/courses/lessons/lesson/<lesson>/content')
def content(lesson):
    file_path = f'lessons/{lesson}/content-lesson-{lesson}.html'
    return render_template(file_path)


if __name__ == '__main__':
    app.run()
