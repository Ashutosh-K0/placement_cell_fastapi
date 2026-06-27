from sqlalchemy import Column, Integer, String, DateTime, Enum, func, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.enums.job_status import JobStatus
from app.enums.job_type import JobType

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    created_by_hr_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    approved_by_tpo_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=False)
    job_type = Column(Enum(JobType), nullable=False)
    status = Column(Enum(JobStatus), nullable=False, default=JobStatus.PENDING, index=True)
    ctc = Column(Float, nullable=False)
    minimum_cgpa = Column(Float, nullable=False)
    maximum_backlogs = Column(Integer, nullable= False, default=0)
    opening_count = Column(Integer, nullable=False)
    application_deadline = Column(DateTime(timezone=True), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate= func.now(), nullable=False)

    applications = relationship('Application', back_populates='job')
    company = relationship('Company', back_populates='jobs')
    created_by_hr = relationship('User', back_populates="created_jobs", foreign_keys=[created_by_hr_id])
    approved_by_tpo = relationship('User', back_populates="approved_jobs", foreign_keys=[approved_by_tpo_id])