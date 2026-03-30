import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.sql import func

from app.db.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    goals = Column(JSONB, nullable=True)
    # "references" is reserved on SQLAlchemy Table; column name in DB stays "references"
    refs = Column("references", JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
