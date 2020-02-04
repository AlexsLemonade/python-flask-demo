import os

import resources_portal.models  # noqa
from flask import Flask
from flask_migrate import Migrate
from resources_portal.db import db

migrate = Migrate()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://resources_portal_user:resources_portal_password@172.17.0.3/resources_portal"
    app.config.from_mapping(SECRET_KEY="dev")

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    migrate.init_app(app, db)

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    return app
