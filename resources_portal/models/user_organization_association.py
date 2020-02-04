from resources_portal.db import db
from resources_portal.models.userorganization_grant_association import (  # noqa
    userorganization_grant_associations,
)
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class UserOrganizationAssociation(db.Model):
    __tablename__ = "user_organization_associations"
    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), primary_key=True)
    user = relationship("User", back_populates="organizations")
    organization = relationship("Organization", back_populates="users")
    user_organizations = relationship(
        "Grant", secondary=userorganization_grant_associations, back_populates="user_organizations",
    )
