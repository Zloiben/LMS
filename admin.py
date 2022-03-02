from flask import Blueprint, render_template, redirect
from flask_login import current_user, logout_user
from werkzeug.security import generate_password_hash

from instance.function.cheking import check_email
from . import db
from .models import User
from form import SetName, SetEmail, SetPassword, SetRole
from config import ADMIN_ROLES, ALL_ROLES

admin = Blueprint('admin', __name__)


@admin.route('/admin-panel')
def admin_panel():
    if current_user.is_authenticated is False:
        return redirect('/login')
    user = current_user
    if user.role not in ADMIN_ROLES:
        # TODO: Добавить какое то сообщение
        return redirect('/courses')
    return render_template("admin/admin-panel.html", dbUsers=User.query.all())


@admin.route('/admin-panel/set-name/<int:user_id>', methods=['GET', 'POST'])
def set_name(user_id):
    form = SetName()
    user = User.query.filter_by(id=user_id).first()
    if form.validate_on_submit():
        user.name = form.name.data
        db.session.commit()
        return redirect('/admin-panel')
    return render_template("admin/function/set-name.html", form=form,
                           user_id=user_id, name=user.name, email=user.email, role=user.role)


@admin.route('/admin-panel/set-role/<int:user_id>', methods=['GET', 'POST'])
def set_role(user_id):
    form = SetRole()
    user = User.query.filter_by(id=user_id).first()
    if form.validate_on_submit():
        if form.role.data in ALL_ROLES:
            user.role = form.role.data
            db.session.commit()
            return redirect('/admin-panel')
        else:
            return render_template("admin/function/set-role.html", form=form,
                                   user_id=user_id, name=user.name, email=user.email, role=user.role, error="role")
    return render_template("admin/function/set-role.html", form=form,
                           user_id=user_id, name=user.name, email=user.email, role=user.role)


@admin.route('/admin-panel/set-password/<int:user_id>', methods=['GET', 'POST'])
def set_password(user_id):
    form = SetPassword()
    user = User.query.filter_by(id=user_id).first()
    if form.validate_on_submit():
        user.password = generate_password_hash(form.password.data, method='sha256')
        db.session.commit()
        user_session = current_user
        if user_session.name == user.name:
            logout_user()
            return redirect('/login')
        return redirect('/admin-panel')
    return render_template("admin/function/set-password.html", form=form,
                           user_id=user_id, name=user.name, email=user.email, role=user.role)


@admin.route('/admin-panel/set-email/<int:user_id>', methods=['GET', 'POST'])
def set_email(user_id):
    form = SetEmail()
    user = User.query.filter_by(id=user_id).first()
    if form.validate_on_submit():
        if check_email(form.email.data):
            user.email = form.email.data
            db.session.commit()
            return redirect('/admin-panel')
        else:
            return render_template("admin/function/set-email.html", form=form,
                                   user_id=user_id, name=user.name, email=user.email, role=user.role, error='email')
    return render_template("admin/function/set-email.html", form=form,
                           user_id=user_id, name=user.name, email=user.email, role=user.role)
