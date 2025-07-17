from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from backend.databases.MSSQLServer import Base

class ProductModel(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    category = Column(String, nullable=True)
    email_contact = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
