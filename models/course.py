from .base import Base, TimestampMixin
from .associations import course_prerequisite, course_skill
from sqlalchemy import Column, Uuid, String, Integer
from sqlalchemy.orm import relationship


class Course(TimestampMixin, Base):
    __tablename__ = "courses"

    id = Column(Uuid, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    theme = Column(String)
    validity_months = Column(Integer)

    activities = relationship("Activity", back_populates="course")
    skills = relationship("Skill", secondary=course_skill, back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")
    prerequisites = relationship(
        "Course",
        secondary=course_prerequisite,
        primaryjoin=id == course_prerequisite.c.course_id_1,
        secondaryjoin=id == course_prerequisite.c.course_id_2,
        back_populates="required_by",
    )
    required_by = relationship(
        "Course",
        secondary=course_prerequisite,
        primaryjoin=id == course_prerequisite.c.course_id_2,
        secondaryjoin=id == course_prerequisite.c.course_id_1,
        back_populates="prerequisites",
    )

