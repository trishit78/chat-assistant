import uuid
from sqlalchemy import Column, ForeignKey, DateTime, String, Text, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.database import Base

class Memory(Base):
    __tablename__ = "memories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)

    type = Column(String, nullable=False)  # fact | decision | summary | constraint
    content = Column(Text, nullable=False)

    source = Column(String, nullable=False)  # chat | agent
    relevance_score = Column(Float, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())