from flask import Blueprint,  render_template, redirect
from flask_login import login_required, current_user
from . import db, create_app
import json
import os

from werkzeug.utils import secure_filename

from form import TaskInputFile
from instance.testing.testing import Testing

from instance.function.cheking import allowed_file, check_email
from config import standard_data, UPLOAD_FOLDER

from .models import User

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/courses')
def courses():
    if current_user.is_authenticated is False:
        return redirect('/login')

    return render_template('courses.html')


@main.route('/profile')
def profile():

    if current_user.is_authenticated is False:
        return redirect('/login')

    user = current_user
    data = json.loads(user.data)
    all_score = data['courses']['Python Basics']['profile']['all_score']
    return render_template('profile.html', name=user.name, email=user.email, all_score=all_score)


@main.route('/courses/lessons')
def lessons():

    if current_user.is_authenticated is False:
        return redirect('/login')

    return render_template('lessons.html')


@main.route('/courses/lessons/lesson/<lesson>')
def lesson(lesson):

    if current_user.is_authenticated is False:
        return redirect('/login')

    return render_template(f'courses/Python Basics/lessons/{lesson}/lesson-{lesson}.html')


@main.route('/courses/lessons/lesson/<lesson>/tasks/<task>',  methods=['GET', 'POST'])
def tasks(lesson, task):

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
            User.query.filter_by(id=user.id).first().data = data
            db.session.commit()
            return render_template(file_path, form=form, score=score, result=lesson_data['result'])
        return render_template(file_path, form=form, score=score, result="error")
    return render_template(file_path, form=form, score=score, result=lesson_data['result'])


@main.route('/courses/lessons/lesson/<lesson>/content')
def content(lesson):

    if current_user.is_authenticated is False:
        return redirect('/login')

    file_path = f'courses/Python Basics/lessons/{lesson}/content-lesson-{lesson}.html'
    return render_template(file_path)
