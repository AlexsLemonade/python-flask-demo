from flask import jsonify, request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError
from resources_portal.db import db
from resources_portal.models import User
from resources_portal.schemas.user_schema import UserSchema
from werkzeug.exceptions import BadRequest


class UsersApi(Resource):
    def post(self, *args):
        db.session.add(User(**request.get_json()))
        db.session.commit()

        return ("User created.", 201)

    def get(self):
        users = db.session.query(User).all()
        users = [user.as_dict() for user in users]

        return jsonify(users)


class UserApi(Resource):
    def get(self, user_id: int):
        user = db.session.query(User).get_or_404(user_id)
        return UserSchema().dump(user)

    def put(self, user_id: int, *args):
        # Make sure the User exists
        db.session.query(User).get_or_404(user_id)

        user_schema = UserSchema()

        request_data = request.get_json()

        # Validate the incoming data
        try:
            user_schema.load(request_data)
        except ValidationError as error:
            raise BadRequest(error.messages)

        db.session.query(User).filter(User.id == user_id).update(request_data)
        db.session.commit()

        return ("User updated.", 200)
