from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, func, DateTime
from sqlalchemy.orm import relationship
from app.database.database import Base

class Resume(Base):
    __tablename__ = 'resumes'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    title = Column(String(100), nullable=False)
    file_url = Column(String(255), nullable=False)
    is_primary = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)