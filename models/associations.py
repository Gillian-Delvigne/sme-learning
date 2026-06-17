from .base import Base
from sqlalchemy import Table, Column, ForeignKey, Uuid, DateTime

role_skill = Table(
    "role_skill",
    Base.metadata,
    Column("role_id", Uuid, ForeignKey("roles.id")),
    Column("skill_id", Uuid, ForeignKey("skills.id")),
)

employee_skill = Table(
    "employee_skill",
    Base.metadata,
    Column("employee_id", Uuid, ForeignKey("employees.id")),
    Column("skill_id", Uuid, ForeignKey("skills.id")),
)

course_skill = Table(
    "course_skill",
    Base.metadata,
    Column("course_id", Uuid, ForeignKey("courses.id")),
    Column("skill_id", Uuid, ForeignKey("skills.id")),
)

employee_activity = Table(
    "employee_activity",
    Base.metadata,
    Column("employee_id", Uuid, ForeignKey("employees.id")),
    Column("activity_id", Uuid, ForeignKey("activities.id")),
    Column("completed_at", DateTime, nullable=True),
)

course_prerequisite = Table(
    "course_prerequisite",
    Base.metadata,
    Column("course_id_1", Uuid, ForeignKey("courses.id")),
    Column("course_id_2", Uuid, ForeignKey("courses.id")),
)
