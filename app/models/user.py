from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.enums.user_role import UserRole

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True, index=True)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    phone_number = Column(String(20), nullable=True)
    company_id = Column(Integer,ForeignKey("companies.id"),nullable=True)
    created_at = Column(DateTime(timezone=True), server_default= func.now(),nullable=False)
    updated_at = Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now(),nullable=False)

    application_history = relationship('ApplicationHistory', back_populates='user')
    resumes = relationship('Resume', back_populates='user')
    company = relationship('Company', back_populates='users')
    student_profile = relationship('StudentProfile', back_populates='user', uselist=False)
    applications = relationship('Application', back_populates='user')
    created_jobs = relationship('Job', back_populates='created_by_hr', foreign_keys="Job.created_by_hr_id")
    approved_jobs = relationship('Job', back_populates='approved_by_tpo', foreign_keys="Job.approved_by_tpo_id")