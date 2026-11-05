from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from backend.app.database import Base


class ClueDB(Base):

    __tablename__ = "clues"

    id = Column(Integer, primary_key=True, index=True)

    clue_type = Column(String(50), nullable=False)

    description = Column(Text, nullable=False)

    confidence = Column(String(50), default="vague")

    created_at = Column(DateTime, server_default=func.now())