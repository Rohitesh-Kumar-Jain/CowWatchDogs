from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt  # bcrypt is being used for encrypting passwords
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '0342cf57e6fb58ee2634f555ab2485c2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# By default, when a user attempts to access a login_required view without being logged in, Flask-Login will flash a
# message and redirect them to the log in view. The name of the log in view can be set as LoginManager.login_view.

login_manager.login_view = 'login'
login_manager.login_message_category = 'info'  # in bootstrap info is nicely colored blue class

from CWD import routes
