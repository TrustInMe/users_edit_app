from flask import Flask
from flask import render_template, request

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from users_edit_app.config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

from users_edit_app.models import permissions, User, Permission
from users_edit_app.routes import login_page, users_list_page