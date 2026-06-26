from sqlalchemy import Column, Integer, String, DateTime, func
from app.database.database import Base
from sqlalchemy.orm import relationship

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True, nullable=False, index=True)
    domain = Column(String(100), nullable=False)
    location = Column(String(150), nullable=False)
    website_url = Column(String(200), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate= func.now(), nullable=False)