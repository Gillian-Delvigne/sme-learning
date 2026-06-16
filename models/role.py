from base import Base, TimestampMixin
from associations import role_requires
from sqlalchemy import Column, Uuid, String
from sqlalchemy.orm import relationship


class Role(TimestampMixin, Base):
    __tablename__ = "roles"

    id = Column(Uuid, primary_key=True)
    title = Column(String, nullable=False)

    employees = relationship("Employee", back_populates="roles")
    skills = relationship("Skill", secondary=role_requires, back_populates="roles")
