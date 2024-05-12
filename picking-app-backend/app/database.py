from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import pandas as pd
import asyncio
from itertools import count
from sqlalchemy import insert
from models.models import Base, ProductMaster, Orders, OrderLines

DATABASE_URL = "sqlite+aiosqlite:///warehouse.db"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionFactory = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def initialize_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def load_data(session, df, table_class):
    try:
        df.columns = df.columns.str.strip()
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

        insert_stmt = insert(table_class).values(df.to_dict(orient='records'))

        await session.execute(insert_stmt)
        await session.commit()
    except Exception as e:
        await session.rollback()
        print(f"Error loading data into {table_class.__tablename__}: {e}")

async def load_initial_data():
    async with AsyncSessionFactory() as session:
        product_master = pd.read_csv('data/product_master.csv')
        orders = pd.read_csv('data/orders.csv')
        order_lines = pd.read_csv('data/order_lines.csv')

        max_id = order_lines['pick_id'].max()
        id_generator = count(start=max_id + 1)
        duplicate_indices = order_lines[order_lines.duplicated('pick_id', keep=False)].index

        for index in duplicate_indices:
            order_lines.at[index, 'pick_id'] = next(id_generator)

        await load_data(session, product_master, ProductMaster)
        await load_data(session, orders, Orders)
        await load_data(session, order_lines, OrderLines)

async def get_async_db():
    async with AsyncSessionFactory() as session:
        yield session

if __name__ == '__main__':
    asyncio.run(initialize_database())
    asyncio.run(load_initial_data())
