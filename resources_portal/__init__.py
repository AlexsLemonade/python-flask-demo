import os

import resources_portal.models  # noqa
from flask import Flask
from flask_migrate import Migrate
from resources_portal.db import db
from resources_portal.views import user

migrate = Migrate()


def register_views(app: Flask):
    app.register_blueprint(user.user, url_prefix="/users")


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_envvar("RESOURCES_PORTAL_CONFIG_FILE")

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    migrate.init_app(app, db)

    register_views(app)

    return app
