from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///warehouse.db')
Base = declarative_base()

class ProductMaster(Base):
    __tablename__ = 'product_master'
    sku = Column(Integer, primary_key=True)
    dinner_title = Column(String)
    location_id = Column(String)
    on_hand = Column(Integer)
    order_lines = relationship("OrderLines", back_populates="product_master")  # Define the reverse relationship

class OrderLines(Base):
    __tablename__ = 'order_lines'
    pick_id = Column(Integer, primary_key=True)
    order_number = Column(String, ForeignKey('orders.order_number'))
    sku = Column(Integer, ForeignKey('product_master.sku'))
    location = Column(String)
    pick_qty = Column(Integer)
    product_master = relationship("ProductMaster", back_populates="order_lines")
    orders = relationship("Orders", back_populates="order_lines")  # Corrected relationship reference

class Orders(Base):
    __tablename__ = 'orders'
    order_number = Column(String, primary_key=True)
    fake_name = Column(String)
    order_date = Column(String)
    order_lines = relationship("OrderLines", back_populates="orders")

# Create tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
