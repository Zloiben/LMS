import os

from flask import Flask, render_template, redirect, url_for
from werkzeug.utils import secure_filename

from login import LoginFrom
from task_input import TaskInput

UPLOAD_FOLDER = "testing/testing_file"
ALLOWED_EXTENSIONS = set('py')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        return redirect('/courses')
    return render_template('verification.html', form=form)


@app.route('/courses')
def courses():
    return render_template('courses.html')


@app.route('/courses/lessons')
def lessons():
    return render_template('lessons.html')


@app.route('/courses/lessons/lesson/<lesson>')
def lesson(lesson):
    return render_template(f'lessons/{lesson}/lesson.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/courses/lessons/lesson/<lesson>/tasks/<task>',  methods=['GET', 'POST'])
def tasks(lesson, task):
    file_path = f'lessons/{str(lesson)}/tasks/{str(task)}.html'
    form = TaskInput()
    if form.validate_on_submit():
        f = form.file.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.instance_path, filename
        ))

    return render_template(file_path, form=form)


if __name__ == '__main__':
    app.run()
