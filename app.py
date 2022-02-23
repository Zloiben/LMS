
from flask import Flask, render_template, redirect
from login import LoginFrom

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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
def test():
    return render_template('lessons.html')


@app.route('/courses/lessons/lesson')
def test1():
    return render_template('lesson.html')


@app.route('/courses/lessons/lesson/tasks/<int:task>')
def test2(task):
    return render_template(f'/tasks/{task}.html')


if __name__ == '__main__':
    app.run()
