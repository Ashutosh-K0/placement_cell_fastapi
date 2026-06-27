from sqlalchemy import Column, Integer, ForeignKey, func, DateTime, Enum
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.enums.application_status import ApplicationStatus

class Application(Base):
    __tablename__ = 'applications'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False, index=True)
    resume_id = Column(Integer, ForeignKey("resumes.id"), nullable=False)
    status = Column(Enum(ApplicationStatus), default=ApplicationStatus.APPLIED, index=True, nullable=False)
    applied_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)