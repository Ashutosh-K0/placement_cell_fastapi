from sqlalchemy import Column, Integer, String, Float, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class StudentProfile(Base):
    __tablename__ = 'student_profiles'
    user_id = Column(Integer,ForeignKey("users.id"),primary_key=True)
    college_name = Column(String(200), nullable=False)
    branch = Column(String(150), nullable=False)
    cgpa = Column(Float, nullable=False)
    tenth_percentage = Column(Float, nullable=False)
    twelfth_percentage = Column(Float, nullable=False)
    backlog_count = Column(Integer, nullable=False, default=0)
    address = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate= func.now(), nullable=False)

    user = relationship('User', back_populates='student_profile')