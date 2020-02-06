from flask import Blueprint, jsonify, request
from flask_request_validator import JSON, PATH, MaxLength, MinLength, Param, validate_params
from resources_portal.db import db
from resources_portal.models import User

user = Blueprint("user", __name__)

str_one_to_hundred_validator = [MinLength(1), MaxLength(100)]

user_validator = [
    Param("first_name", JSON, str, rules=str_one_to_hundred_validator),
    Param("last_name", JSON, str, rules=str_one_to_hundred_validator),
    Param("orcid", JSON, str, rules=str_one_to_hundred_validator),
    Param("email_address", JSON, str, rules=str_one_to_hundred_validator),
]


@user.route("/", methods=["POST"])
@user.route("", methods=["POST"])
@validate_params(*user_validator)
def create(*args):
    db.session.add(User(**request.get_json()))
    db.session.commit()

    return ("User created.", 201)


@user.route("/<user_id>/", methods=["PUT"])
@user.route("/<user_id>", methods=["PUT"])
@validate_params(Param("user_id", PATH, int), *user_validator)
def update(user_id: int, *args):
    # Make sure the User exists
    db.session.query(User).get_or_404(user_id)

    db.session.query(User).filter(User.id == user_id).update(request.get_json())
    db.session.commit()

    return ("User updated.", 200)


@user.route("/<user_id>/", methods=["GET"])
@user.route("/<user_id>", methods=["GET"])
@validate_params(Param("user_id", PATH, int))
def show(user_id: int):
    user = db.session.query(User).get_or_404(user_id)

    return jsonify(user.as_dict())


@user.route("/", methods=["GET"])
@user.route("", methods=["GET"])
def list():
    users = db.session.query(User).all()
    users = [user.as_dict() for user in users]

    return jsonify(users)
