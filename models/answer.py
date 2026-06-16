from base import Base, TimestampMixin
from sqlalchemy import Column, ForeignKey, Uuid, String, Boolean
from sqlalchemy.orm import relationship


class Answer(TimestampMixin, Base):
    __tablename__ = "answers"

    id = Column(Uuid, primary_key=True)
    content = Column(String, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    question_id = Column(Uuid, ForeignKey("questions.id"), nullable=False)

    question = relationship("Question", back_populates="answers")
