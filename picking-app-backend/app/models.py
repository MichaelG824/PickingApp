from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship  # Ensure relationship is imported
from pydantic import BaseModel, Field
from enum import Enum as PyEnum
from typing import Optional

engine = create_engine('sqlite:///warehouse.db')
Base = declarative_base()

class StatusEnum(str, PyEnum):
    Pending = "Pending"
    Picked = "Picked"
    Exception = "Exception"

class ProductMaster(Base):
    __tablename__ = 'product_master'
    sku = Column(Integer, primary_key=True)
    dinner_title = Column(String)
    location_id = Column(String)
    on_hand = Column(Integer)
    order_lines = relationship("OrderLines", back_populates="product_master")

class OrderLines(Base):
    __tablename__ = 'order_lines'
    pick_id = Column(Integer, primary_key=True)
    order_number = Column(String, ForeignKey('orders.order_number'))
    sku = Column(Integer, ForeignKey('product_master.sku'))
    location = Column(String)
    pick_qty = Column(Integer)
    status = Column(Enum(StatusEnum), default=StatusEnum.Pending)
    exception_details = Column(String, nullable=True)
    product_master = relationship("ProductMaster", back_populates="order_lines")
    orders = relationship("Orders", back_populates="order_lines")

class Orders(Base):
    __tablename__ = 'orders'
    order_number = Column(String, primary_key=True)
    fake_name = Column(String)
    order_date = Column(String)
    order_lines = relationship("OrderLines", back_populates="orders")

class UpdateStatusRequestDto(BaseModel):
    pick_id: int
    status: StatusEnum
    exception_details: str = Field(None, description="Optional details about the exception")
Session = sessionmaker(bind=engine)
session = Session()
