from resources_portal.db import db
from sqlalchemy import Column, ForeignKey, Integer, Table

userorganization_grant_associations = Table(
    "userorganization_grant_associations",
    db.Model.metadata,
    Column("user_organization_id", Integer, ForeignKey("user_organization_associations.id")),
    Column("grant_id", Integer, ForeignKey("grants.id")),
)
