from marshmallow import fields
from resources_portal.models.user import User
from resources_portal.schemas import ma


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    orcid = fields.Str(required=True)
    email_address = fields.Str(required=True)
