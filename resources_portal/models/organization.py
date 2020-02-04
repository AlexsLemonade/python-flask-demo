from resources_portal.db import db
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Organization(db.Model):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True, unique=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("User", back_populates="organizations")
