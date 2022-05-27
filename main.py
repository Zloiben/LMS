from flask import Blueprint, render_template, redirect, send_file
from flask_login import login_required, current_user
from . import db, create_app
import json
import os

from werkzeug.utils import secure_filename

from form import TaskInputFile
from instance.testing.testing import Testing

from instance.function.cheking import allowed_file
from config import UPLOAD_FOLDER

from .models import User

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Главная страница"""
    return render_template('index.html', user_auth=current_user.is_authenticated)


@main.route('/courses')
def courses():
    """Курсы"""
    if current_user.is_authenticated is False:
        return redirect('/login')
    return render_template('courses.html', user_auth=current_user.is_authenticated)


@main.route('/profile')
def profile():
    """Профиль"""
    if current_user.is_authenticated is False:
        return redirect('/login')

    user = current_user
    data = json.loads(user.data)
    all_score = data['courses']['Python Basics']['profile']['all_score']
    return render_template('profile.html', name=user.name, email=user.email,
                           all_score=all_score, user_auth=current_user.is_authenticated)


@main.route('/courses/lessons')
def lessons():
    """Уроки"""
    if current_user.is_authenticated is False:
        return redirect('/login')

    return render_template('lessons.html', user_auth=current_user.is_authenticated)


@main.route('/courses/lessons/lesson/<lesson>')
def lesson(lesson):
    """Выбранный урок"""
    if current_user.is_authenticated is False:
        return redirect('/login')

    return render_template(f'courses/Python Basics/lessons/{lesson}/lesson-{lesson}.html',
                           user_auth=current_user.is_authenticated)


@main.route('/courses/lessons/lesson/<lesson>/tasks/<task>',  methods=['GET', 'POST'])
def tasks(lesson, task):
    """ВЫбранное задание"""

    if current_user.is_authenticated is False:
        return redirect('/login')

    file_path = f'courses/Python Basics/lessons/{lesson}/tasks/{task}.html'

    user = current_user
    data = json.loads(user.data)
    lesson_data = data['courses']['Python Basics']['lessons'][lesson][f'task_{task}']
    score = lesson_data['score']
    form = TaskInputFile()
    if form.validate_on_submit():
        f = form.file.data
        if allowed_file(f.filename):

            # Сохранение отправленного файла в папку для тестов
            filename = secure_filename(f"test_file_{task}.py")
            f.save(os.path.join(UPLOAD_FOLDER, f'lesson_{lesson}\\task_{task}', filename))
            Test = Testing(lesson, task)
            max_score = lesson_data['max_score']
            result_testing = Test.test()

            if result_testing is True:
                data['courses']['Python Basics']['lessons'][lesson][f'task_{task}']['score'] = score
                data['courses']['Python Basics']["profile"]['all_score'] += score

            data['courses']['Python Basics']['lessons'][lesson][f'task_{task}']['result'] = result_testing
            data = json.dumps(data)
            User.query.filter_by(id=user.id).first().data = data
            db.session.commit()
            return render_template(file_path, form=form, score=score, result=lesson_data['result'],
                                   user_auth=current_user.is_authenticated)
        return render_template(file_path, form=form, score=score, result="error",
                               user_auth=current_user.is_authenticated)
    return render_template(file_path, form=form, score=score, result=lesson_data['result'],
                           user_auth=current_user.is_authenticated)


@main.route('/courses/lessons/lesson/<lesson>/content')
def content(lesson):
    """Методичка"""
    if current_user.is_authenticated is False:
        return redirect('/login')

    file_path = f'courses/Python Basics/lessons/{lesson}/content-lesson-{lesson}.html'
    return render_template(file_path, user_auth=current_user.is_authenticated)


@main.route('/test_download')
def test_download():
    # TODO: Испомощью этого реализовать скачку с Яндекс диска и генерировать код HTML па
    return send_file('instance/testing/lesson_1/task_5/test_file_5.py',
                     mimetype='text/py',
                     attachment_filename='test_file_5.py',
                     as_attachment=True)
