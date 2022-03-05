from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import UPLOAD_FOLDER, API_KEYS
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.config['SECRET_KEY'] = API_KEYS
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Data.sqlite3'

    db.init_app(app)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)
    return app
