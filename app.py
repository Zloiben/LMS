import json
import os

from flask import Flask, render_template, redirect, make_response
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

from instance.form.login import LoginFrom
from instance.form.registstration import RegistrationForm
from instance.form.task_input import TaskInputFile
from instance.testing.testing import Testing

from instance.function.cheking import allowed_file
from config import UPLOAD_FOLDER, standard_data

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Data.sqlite3'
db = SQLAlchemy(app)


class Users(db.Model):

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(50))
    role = db.Column(db.String(20))
    email = db.Column(db.String(100))
    data = db.Column(db.TEXT())

    def __init__(self, name, role, password, email, data):

        self.name = name
        self.password = password
        self.role = role
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
        if Users.query.filter_by(email=form.email.data).first() is not None:
            if Users.query.filter_by(email=form.email.data).first().password == form.password.data:
                return redirect(f'/{Users.query.filter_by(email=form.email.data).first().id}/courses')

        return render_template('verification.html', form=form, error_login=True)
    return render_template('verification.html', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if Users.query.filter_by(email=form.email.data).first() is None:
        if form.validate_on_submit():
            data = json.dumps(standard_data)
            if form.password.data == form.password2.data:
                db.session.add(Users(form.username.data, "user", form.password.data, form.email.data, data))
                db.session.commit()
                return redirect(f'/{Users.query.filter_by(email=form.email.data).first().id}/courses')
            else:
                return render_template('registration.html', form=form, error_registration="password")
    else:
        return render_template('registration.html', form=form, error_registration="email")
    return render_template('registration.html', form=form)


@app.route('/<int:id>/courses')
def courses(id):
    return render_template('courses.html', id=id)


@app.route('/<int:id>/courses/lessons')
def lessons(id):
    return render_template('lessons.html', id=id)


@app.route('/<int:id>/courses/lessons/lesson/<lesson>')
def lesson(id, lesson):
    return render_template(f'courses/Python Basics/lessons/{lesson}/lesson-1.html', id=id)


@app.route('/<int:id>/courses/lessons/lesson/<lesson>/tasks/<task>',  methods=['GET', 'POST'])
def tasks(id, lesson, task):

    data = Users.query.filter_by(id=id).first().data
    data = json.loads(data)

    result = data['courses']['Основы программирования на Python']['lessons'][lesson][f'task_{task}']['result']
    score = data['courses']['Основы программирования на Python']['lessons'][lesson][f'task_{task}']['score']
    max_score = data['courses']['Основы программирования на Python']['lessons'][lesson][f'task_{task}']['max_score']
    file_path = f'courses/Python Basics/lessons/{str(lesson)}/tasks/{str(task)}.html'

    form = TaskInputFile()
    if form.validate_on_submit():
        f = form.file.data
        if allowed_file(f.filename):
            # Сохранение отправленного файла в папку для тестов
            filename = secure_filename(f"test_file_{task}.py")
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f'lesson_{lesson}', filename))
            result = Testing(lesson, task)
            if result.test() is True:
                score = max_score
                data['courses']['Основы программирования на Python']['lessons'][lesson][f'task_{task}']['score'] = max_score
            data['courses']['Основы программирования на Python']['lessons'][lesson][f'task_{task}']['result'] = result.test()
            data = json.dumps(data)
            Users.query.filter_by(id=id).first().data = data
            db.session.commit()
            return render_template(file_path, form=form, score=score, id=id, result=result.test())

        else:
            return render_template(file_path, form=form, id=id, score=score, result="error")

    return render_template(file_path, form=form, id=id, score=score, result=result)


@app.route('/<int:id>/courses/lessons/lesson/<lesson>/content')
def content(id, lesson):
    file_path = f'courses/Python Basics/lessons/{lesson}/content-lesson-{lesson}.html'
    return render_template(file_path, id=id)


if __name__ == '__main__':
    app.run()
