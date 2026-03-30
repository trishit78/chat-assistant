import uuid
from sqlalchemy import Column, ForeignKey, DateTime, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.database import Base

class Image(Base):
    __tablename__ = "images"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)

    url = Column(String, nullable=False)
    prompt = Column(Text)

    created_by = Column(String)  # user | assistant

    created_at = Column(DateTime(timezone=True), server_default=func.now())