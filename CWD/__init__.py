from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt # bcrypt is being used for encrypting passwords

app = Flask(__name__)
app.config['SECRET_KEY'] = '0342cf57e6fb58ee2634f555ab2485c2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from CWD import routes
