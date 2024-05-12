from sqlalchemy import create_engine, Column, Integer, String, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from enums.status_enum import StatusEnum

Base = declarative_base()

class ProductMaster(Base):
    __tablename__ = 'product_master'
    sku = Column(Integer, primary_key=True)
    dinner_title = Column(String)
    location_id = Column(String)
    on_hand = Column(Integer)
    order_lines = relationship("OrderLines", back_populates="product_master", lazy="selectin")

class OrderLines(Base):
    __tablename__ = 'order_lines'
    pick_id = Column(Integer, primary_key=True)
    order_number = Column(String, ForeignKey('orders.order_number'))
    sku = Column(Integer, ForeignKey('product_master.sku'))
    location = Column(String)
    pick_qty = Column(Integer)
    status = Column(Enum(StatusEnum), default=StatusEnum.Pending)
    exception_details = Column(String, nullable=True)
    product_master = relationship("ProductMaster", back_populates="order_lines", lazy="selectin")
    orders = relationship("Orders", back_populates="order_lines", lazy="selectin")

class Orders(Base):
    __tablename__ = 'orders'
    order_number = Column(String, primary_key=True)
    fake_name = Column(String)
    order_date = Column(String)
    order_lines = relationship("OrderLines", back_populates="orders", lazy="selectin")
