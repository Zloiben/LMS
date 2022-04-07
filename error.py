
from flask_restful import abort
from models import User
from app import app


@app.errorhandler(404)
def abort_if_user_not_found(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404, message=f"User {user_id} not found")
