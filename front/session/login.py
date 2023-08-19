from flask_login import LoginManager, UserMixin, login_require, logout_user, current_user
from base import app

login_manager = LoginManager()
login_manager.init_app(app)

#class Users(UserMixin)
