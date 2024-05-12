from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
import pandas as pd
from models.db_table_model import Base, ProductMaster, Orders, OrderLines
from db.database_util import preprocess_data, new_pick_ids_for_duplicates
import logging

DATABASE_URL = "sqlite+aiosqlite:///warehouse.db"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionFactory = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def initialize_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def load_data(session, df, table_class):
    try:
        insert_stmt = insert(table_class).values(df.to_dict(orient='records'))
        await session.execute(insert_stmt)
        await session.commit()
    except Exception as e:
        await session.rollback()
        logging.error("Exception: ", e)

async def load_initial_data() -> None:
    async with AsyncSessionFactory() as session:
        product_master = preprocess_data(pd.read_csv('data/product_master.csv'), 'product_master')
        orders = preprocess_data(pd.read_csv('data/orders.csv'), 'orders')
        order_lines = preprocess_data(pd.read_csv('data/order_lines.csv'), 'order_lines')

        new_pick_ids_for_duplicates(order_lines)

        await load_data(session, product_master, ProductMaster)
        await load_data(session, orders, Orders)
        await load_data(session, order_lines, OrderLines)

async def get_session():
    async with AsyncSessionFactory() as session:
        yield session