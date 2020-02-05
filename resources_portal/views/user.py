import json

from flask import Blueprint, request
from resources_portal.db import db
from resources_portal.models import User

user = Blueprint("user", __name__)


@user.route("/", methods=["POST"])
@user.route("", methods=["POST"])
def create():
    db.session.add(User(**request.json))
    db.session.commit()

    return ("User created.", 201)


@user.route("/<user_id>/", methods=["PUT"])
@user.route("/<user_id>", methods=["PUT"])
def update(user_id: int):
    # Make sure the User exists
    db.session.query(User).get_or_404(user_id)

    db.session.query(User).filter(User.id == user_id).update(request.json)
    db.session.commit()

    return ("User updated.", 200)


@user.route("/<user_id>/", methods=["GET"])
@user.route("/<user_id>", methods=["GET"])
def show(user_id: int):
    user = db.session.query(User).get_or_404(user_id)

    return (json.dumps(user.as_dict()), 200)


@user.route("/", methods=["GET"])
@user.route("", methods=["GET"])
def list():
    users = db.session.query(User).all()
    users = [user.as_dict() for user in users]

    return (json.dumps(users), 200)
