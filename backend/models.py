from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    brief = Column(Text, nullable=False)
    depth = Column(Integer, default=2)
    created_at = Column(DateTime, default=datetime.utcnow)

    # 1 product -> many documents
    documents = relationship(
        "Document",
        back_populates="product",
        cascade="all, delete-orphan"
    )


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    doc_type = Column(String, nullable=False)   # "PRD", "Landing Page", etc.
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product", back_populates="documents")
