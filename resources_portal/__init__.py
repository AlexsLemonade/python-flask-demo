import os

import resources_portal.models  # noqa
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from resources_portal.db import db
from resources_portal.views import user

migrate = Migrate()


def initialize_routes(api: Api):
    api.add_resource(user.UsersApi, "/users")
    api.add_resource(user.UserApi, "/users/<user_id>")


def set_database_URI(app: Flask):
    database_URI_template = "postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    app.config["SQLALCHEMY_DATABASE_URI"] = database_URI_template.format(
        DB_USER=app.config["DB_USER"],
        DB_PASSWORD=app.config["DB_PASSWORD"],
        DB_HOST=os.environ["DB_HOST"],
        DB_PORT=app.config["DB_PORT"],
        DB_NAME=app.config["DB_NAME"],
    )


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_envvar("RESOURCES_PORTAL_CONFIG_FILE")
    set_database_URI(app)

    api = Api(app)
    initialize_routes(api)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    migrate.init_app(app, db)

    from resources_portal.schemas import ma

    ma.init_app(app)

    return app
