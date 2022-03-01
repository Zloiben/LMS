import json

from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .form import RegistrationForm, LoginFrom, RestoreAccountForm
from .models import User
from . import db
from instance.function.cheking import check_email
from config import standard_data


auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """Регистрация"""
    if current_user.is_authenticated is False:
        form = RegistrationForm()
        if form.validate_on_submit():
            if check_email(form.email.data):
                if User.query.filter_by(email=form.email.data).first() is None:
                    if form.password.data == form.password2.data:
                        data = json.dumps(standard_data)
                        db.session.add(User(email=form.email.data,
                                            name=form.username.data,
                                            role="user",
                                            data=data,
                                            password=generate_password_hash(form.password.data, method='sha256')))
                        db.session.commit()
                        login_user(User.query.filter_by(email=form.email.data).first())
                        return redirect('courses')
                    return render_template('registration.html', form=form, error_registration="password")
                return render_template('registration.html', form=form, error_registration="emailDatabase")
            return render_template('registration.html', form=form, error_registration="email")
        return render_template('registration.html', form=RegistrationForm())
    return redirect('courses')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Авторизация"""
    if current_user.is_authenticated is False:
        form = LoginFrom()
        if form.validate_on_submit():
            if check_email(form.email.data):
                user = User.query.filter_by(email=form.email.data).first()
                if user is not None and check_password_hash(user.password, form.password.data):
                    login_user(user, remember=form.remember.data)
                    return redirect('courses')
            return render_template('verification.html', form=form, error_login='email')
        return render_template('verification.html', form=form)
    return redirect('courses')


@auth.route('/restore_account', methods=['GET', 'POST'])
def restore_account():
    """Восстановление данных"""
    form = RestoreAccountForm()
    if form.validate_on_submit():
        if check_email(form.email.data) is True:
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None:
                if form.password.data == form.password2.data:
                    user.password = generate_password_hash(form.password.data, method='sha256')
                    db.session.commit()
                    return redirect('/login')
                return render_template('restore_account.html', form=form, error_registration="password")
            return render_template('restore_account.html', form=form, error_registration="emailDatabase")
        return render_template('restore_account.html', form=form, error_registration="email")
    return render_template('restore_account.html', form=form)


@auth.route('/logout')
def logout():
    """Выход из аккаунта"""
    logout_user()
    return redirect('/')