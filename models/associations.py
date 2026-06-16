from base import Base
from sqlalchemy import Table, Column, ForeignKey, Uuid

role_requires = Table(
    "role_requires",
    Base.metadata,
    Column("role_id", Uuid, ForeignKey("roles.id")),
    Column("skill_id", Uuid, ForeignKey("skills.id")),
)
