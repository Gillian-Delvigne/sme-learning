import enum
from .base import Base, TimestampMixin
from sqlalchemy import (
    Column,
    UniqueConstraint,
    ForeignKey,
    Uuid,
    Enum as SQLA_ENUM,
    DateTime,
)
from sqlalchemy.orm import relationship


class EnrollmentStatus(enum.Enum):
    ENROLLED = "enrolled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CERTIFIED = "certified"
    EXPIRED = "expired"


class Enrollment(TimestampMixin, Base):
    __tablename__ = "enrollments"
    __table_args__ = (UniqueConstraint("employee_id", "course_id"),)

    id = Column(Uuid, primary_key=True)
    employee_id = Column(Uuid, ForeignKey("employees.id"), nullable=False)
    course_id = Column(Uuid, ForeignKey("courses.id"), nullable=False)
    status = Column(
        SQLA_ENUM(EnrollmentStatus), default=EnrollmentStatus.ENROLLED, nullable=False
    )
    certification_date = Column(DateTime)

    course = relationship("Course", back_populates="enrollments")
    employee = relationship("Employee", back_populates="enrollments")
