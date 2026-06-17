from .base import Base, TimestampMixin
from .associations import employee_skill, course_skill, role_skill
from sqlalchemy import Column, Uuid, String
from sqlalchemy.orm import relationship


class Skill(TimestampMixin, Base):
    __tablename__ = "skills"

    id = Column(Uuid, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    employees = relationship(
        "Employee", secondary=employee_skill, back_populates="skills"
    )
    courses = relationship("Course", secondary=course_skill, back_populates="skills")
    roles = relationship("Role", secondary=role_skill, back_populates="skills")
