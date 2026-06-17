import enum
from .base import Base, TimestampMixin
from sqlalchemy import Column, ForeignKey, Enum as SQLA_ENUM, Uuid, String, Integer
from sqlalchemy.orm import relationship


class ActivityType(enum.Enum):
    QUIZZ = "Quizz"
    MEDIA = "Media"
    TEXT = "Text"


class Activity(TimestampMixin, Base):
    __tablename__ = "activities"

    id = Column(Uuid, primary_key=True)
    title = Column(String, nullable=False)
    type = Column(SQLA_ENUM(ActivityType), nullable=False)
    sequence = Column(Integer, nullable=False)
    content = Column(String, nullable=False)
    pass_threshold = Column(Integer, nullable=False)
    course_id = Column(Uuid, ForeignKey("courses.id"), nullable=False)

    course = relationship("Course", back_populates="activities")
    questions = relationship("Question", back_populates="activity")