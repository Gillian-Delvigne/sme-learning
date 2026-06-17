from .base import Base, TimestampMixin
from sqlalchemy import Column, ForeignKey, Uuid, String
from sqlalchemy.orm import relationship


class Question(TimestampMixin, Base):
    __tablename__ = "questions"

    id = Column(Uuid, primary_key=True)
    statement = Column(String, nullable=False)
    activity_id = Column(Uuid, ForeignKey("activities.id"), nullable=False)

    activity = relationship("Activity", back_populates="questions")
    answers = relationship("Answer", back_populates="question")