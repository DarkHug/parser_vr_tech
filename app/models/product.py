from sqlalchemy import Column, Integer, String, Float, UUID
from .base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(UUID, primary_key=True)
    name = Column(String(length=256), nullable=False)
    category = Column(String(length=256), nullable=False)
    price = Column(String, nullable=False)
    rating = Column(Float, nullable=True)
    reviews = Column(Integer, nullable=True)
