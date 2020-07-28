from flask import Flask
from config import Config

from flask.cli import with_appcontext, click
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_user import UserManager

import io

app = Flask(__name__)
app.config.from_object(Config)


MIGRATION_DIR = 'migrations' if app.config['MODE'] == 'production' else 'dev-migrations'

db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=MIGRATION_DIR)

Bootstrap(app)

from app import routes
# from app import routes, models

# # Setup Flask-User
# user_manager = UserManager(app, db, models.User)