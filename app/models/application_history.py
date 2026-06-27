from sqlalchemy import Column, Integer, func, DateTime, Enum, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.enums.application_status import ApplicationStatus

class ApplicationHistory(Base):
    __tablename__ = 'application_history'
    id = Column(Integer, primary_key=True)
    application_id = Column(Integer, ForeignKey("applications.id"), nullable=False)
    changed_by_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    old_status = Column(Enum(ApplicationStatus), nullable=True)
    new_status = Column(Enum(ApplicationStatus), nullable=False)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    application = relationship('Application', back_populates='history')
    user = relationship('User', back_populates='application_history', foreign_keys=[changed_by_user_id])