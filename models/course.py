from base import Base, TimestampMixin
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
