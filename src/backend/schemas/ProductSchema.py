from pydantic import BaseModel, Field, PositiveFloat
from enum import Enum
from datetime import datetime
from typing import Optional, List

class ProductBase(BaseModel):
    name: str = Field(..., description="Name of the product")
    description: Optional[str] = Field(None, description="Description of the product")
    category: str = Field(None, description="Category of the product")
    price: PositiveFloat = Field(..., description="Price of the product")
    email_contact: str = Field(True, description="Email contact for the product")

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int = Field(..., description="ID of the product")
    created_at: datetime = Field(..., description="Creation timestamp of the product")

    class Config:
        from_attributes = True

class ProductUpdate(ProductBase):
    name: Optional[str] = Field(None, description="Name of the product")
    description: Optional[str] = Field(None, description="Description of the product")
    price: Optional[PositiveFloat] = Field(None, description="Price of the product")
    category: Optional[str] = Field(None, description="Category of the product")
    email_contact: Optional[str] = Field(None, description="Email contact for the product")