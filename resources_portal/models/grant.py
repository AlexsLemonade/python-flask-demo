from resources_portal.db import db
from resources_portal.models.user_organization_association import (  # noqa
    UserOrganizationAssociation,
)
from resources_portal.models.userorganization_grant_association import (  # noqa
    userorganization_grant_associations,
)
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Grant(db.Model):
    __tablename__ = "grants"
    id = Column(Integer, primary_key=True, unique=True)
    alexs_id = Column(String(100), primary_key=True)
    user_organizations = relationship(
        "UserOrganizationAssociation",
        secondary=userorganization_grant_associations,
        back_populates="grants",
    )
