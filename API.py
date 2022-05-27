import json
from flask_restful import reqparse, abort, Api, Resource
import flask
from flask import jsonify

from . import db
from .models import User

API = flask.Blueprint(
    'API',
    __name__,
    template_folder='templates'
)


@API.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return


@API.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('id', 'name', 'role', 'data')) for item in users]
        }
    )


@API.route('/api/user/<int:user_id>/courses/<string:courses>/lesson/<string:lesson>', methods=['GET'])
def get_user_lesson(user_id: int, courses: str, lesson: str):
    user = User.query.filter_by(id=user_id).first()
    data = json.loads(user.data)
    lesson_data = data['courses'][courses]["lessons"][lesson]
    return jsonify(
        {
            f'user_{user_id}': lesson_data
        }
    )
