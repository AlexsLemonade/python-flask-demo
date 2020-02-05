from resources_portal.db import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    orcid = Column(String(100), unique=True)
    email_address = Column(String(100))
    organizations = relationship("Organization", back_populates="users")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
