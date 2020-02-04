from resources_portal.db import db
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    orcid = Column(String(100))
    email_address = Column(String(100))
    organizations = relationship("Organization", back_populates="users")


class Organization(db.Model):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("User", back_populates="organizations")


userorganization_grant_associations = Table(
    "userorganization_grant_associations",
    db.Model.metadata,
    Column("user_organization_id", Integer, ForeignKey("user_organization_associations.id")),
    Column("grant_id", Integer, ForeignKey("grants.id")),
)


class Grant(db.Model):
    __tablename__ = "grants"
    id = Column(Integer, primary_key=True)
    alexs_id = Column(String(100), primary_key=True)
    user_organizations = relationship(
        "UserOrganizationAssociation",
        secondary=userorganization_grant_associations,
        back_populates="grants",
    )


class UserOrganizationAssociation(db.Model):
    __tablename__ = "user_organization_associations"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), primary_key=True)
    user = relationship("User", back_populates="organizations")
    organization = relationship("Organization", back_populates="users")
    user_organizations = relationship(
        "Grant", secondary=userorganization_grant_associations, back_populates="user_organizations",
    )
