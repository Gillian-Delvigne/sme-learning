from .base import Base, TimestampMixin
from .associations import role_skill
from sqlalchemy import Column, Uuid, String
from sqlalchemy.orm import relationship


class Role(TimestampMixin, Base):
    __tablename__ = "roles"

    id = Column(Uuid, primary_key=True)
    title = Column(String, nullable=False)

    employees = relationship("Employee", back_populates="role")
    skills = relationship("Skill", secondary=role_skill, back_populates="roles")
