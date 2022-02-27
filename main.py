from flask import Blueprint,  render_template, redirect
from flask_login import login_required, current_user
from . import db, create_app
import json
import os

from werkzeug.utils import secure_filename

from form import LoginFrom, RegistrationForm, TaskInputFile, RestoreAccountForm
from instance.testing.testing import Testing

from instance.function.cheking import allowed_file, check_email
from config import standard_data, UPLOAD_FOLDER

from .models import User

main = Blueprint('main', __name__)


# @main.route('/')
# def index():
#     return render_template('index.html')
#
#
# @main.route('/profile')
# def profile():
#     data = current_user
#     print(data)
#     return render_template('profile.html', name=current_user.name)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        if check_email(form.email.data) is True:
            if User.query.filter_by(email=form.email.data).first() is not None:
                if User.query.filter_by(email=form.email.data).first().password == form.password.data:
                    return redirect(f'/{User.query.filter_by(email=form.email.data).first().id}/courses')
            return render_template('verification.html', form=form, error_login='password')
        return render_template('verification.html', form=form, error_login='email')
    return render_template('verification.html', form=form)


@main.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        if check_email(form.email.data) is True:
            if User.query.filter_by(email=form.email.data).first() is None:
                if form.password.data == form.password2.data:
                    data = json.dumps(standard_data)
                    db.session.add(User(form.username.data, "user", form.password.data, form.email.data, data))
                    db.session.commit()
                    return redirect(f'/{User.query.filter_by(email=form.email.data).first().id}/courses')
                return render_template('registration.html', form=form, error_registration="password")
            return render_template('registration.html', form=form, error_registration="emailDatabase")
        return render_template('registration.html', form=form, error_registration="email")
    return render_template('registration.html', form=form)


@main.route('/restore_account', methods=['GET', 'POST'])
def restore_account():
    form = RestoreAccountForm()
    if form.validate_on_submit():
        if check_email(form.email.data) is True:
            if User.query.filter_by(email=form.email.data).first() is not None:
                if form.password.data == form.password2.data:
                    User.query.filter_by(email=form.email.data).first().password = form.password.data
                    db.session.commit()
                    return redirect(f'/{User.query.filter_by(email=form.email.data).first().id}/courses')
                return render_template('restore_account.html', form=form, error_registration="password")
            return render_template('restore_account.html', form=form, error_registration="emailDatabase")
        return render_template('restore_account.html', form=form, error_registration="email")
    return render_template('restore_account.html', form=form)


@main.route('/<int:id>/courses')
def courses(id):
    return render_template('courses.html', id=id)


@main.route('/<int:id>/profile')
def profile(id):
    user = User.query.filter_by(id=id).first()
    data = json.loads(user.data)
    all_score = data['courses']['Python Basics']['profile']['all_score']
    return render_template('profile.html', id=id, name=user.name, email=user.email, all_score=all_score)


@main.route('/<int:id>/courses/lessons')
def lessons(id):
    return render_template('lessons.html', id=id)


@main.route('/<int:id>/courses/lessons/lesson/<lesson>')
def lesson(id, lesson):
    return render_template(f'courses/Python Basics/lessons/{lesson}/lesson-1.html', id=id)


@main.route('/<int:id>/courses/lessons/lesson/<lesson>/tasks/<task>',  methods=['GET', 'POST'])
def tasks(id, lesson, task):

    file_path = f'courses/Python Basics/lessons/{str(lesson)}/tasks/{str(task)}.html'

    data = User.query.filter_by(id=id).first().data
    data = json.loads(data)
    lesson_data = data['courses']['Python Basics']['lessons'][lesson][f'task_{task}']
    score = lesson_data['score']

    form = TaskInputFile()
    if form.validate_on_submit():
        f = form.file.data
        if allowed_file(f.filename):

            # Сохранение отправленного файла в папку для тестов
            filename = secure_filename(f"test_file_{task}.py")
            f.save(os.path.join(UPLOAD_FOLDER, f'lesson_{lesson}\\task_{task}', filename))
            result_testing = Testing(lesson, task)
            # TODO: Trello - задача <хранение результатов тестов>
            if result_testing.test() is True:
                score = lesson_data['max_score']
                data['courses']['Python Basics']['lessons'][lesson][f'task_{task}']['score'] = lesson_data['max_score']
                data['courses']['Python Basics']["profile"]['all_score'] += 14
            else:
                score = 0
                data['courses']['Python Basics']['lessons'][lesson][f'task_{task}']['score'] = 0
                if data['courses']['Python Basics']["profile"]['all_score'] - 14 < 0:
                    data['courses']['Python Basics']["profile"]['all_score'] = 0
                else:
                    data['courses']['Python Basics']["profile"]['all_score'] -= 14
            data['courses']['Python Basics']['lessons'][lesson][f'task_{task}']['result'] = result_testing.test()
            data = json.dumps(data)
            User.query.filter_by(id=id).first().data = data
            db.session.commit()
            return render_template(file_path, form=form, score=score, id=id, result=lesson_data['result'])
        return render_template(file_path, form=form, id=id, score=score, result="error")
    return render_template(file_path, form=form, id=id, score=score, result=lesson_data['result'])


@main.route('/<int:id>/courses/lessons/lesson/<lesson>/content')
def content(id, lesson):
    file_path = f'courses/Python Basics/lessons/{lesson}/content-lesson-{lesson}.html'
    return render_template(file_path, id=id)