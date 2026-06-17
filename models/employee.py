from .base import Base, TimestampMixin
from .associations import employee_skill
from sqlalchemy import Column, Uuid, String, ForeignKey
from sqlalchemy.orm import relationship


class Employee(TimestampMixin, Base):
    __tablename__ = "employees"

    id = Column(Uuid, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    role_id = Column(Uuid, ForeignKey("roles.id"), nullable=False)

    role = relationship("Role", back_populates="employees")
    skills = relationship("Skill", secondary=employee_skill, back_populates="employees")
    enrollments = relationship("Enrollment", back_populates="employee")