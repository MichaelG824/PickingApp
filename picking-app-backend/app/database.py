from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
import pandas as pd
import asyncio
from itertools import count
from humps import camelize
from models.db_table_model import Base, ProductMaster, Orders, OrderLines
from re import sub

DATABASE_URL = "sqlite+aiosqlite:///warehouse.db"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionFactory = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def initialize_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

def convert_to_snake_case(s):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
        sub('([A-Z]+)', r' \1',
        s.replace('-', ' '))).split()).lower()

def preprocess_data(df, table_name):
    df.columns = [convert_to_snake_case(col) for col in df.columns]
    if table_name == 'orders':
        df = df.rename(columns={'fake_name': 'name'})
    elif table_name == 'product_master':
        df = df.rename(columns={'dinner_title': 'title'})
    return df

async def load_data(session, df, table_class):
    try:
        insert_stmt = insert(table_class).values(df.to_dict(orient='records'))
        await session.execute(insert_stmt)
        await session.commit()
    except Exception as e:
        await session.rollback()
        print(f"Error loading data: ", e)

async def load_initial_data():
    async with AsyncSessionFactory() as session:
        product_master = preprocess_data(pd.read_csv('data/product_master.csv'), 'product_master')
        orders = preprocess_data(pd.read_csv('data/orders.csv'), 'orders')
        order_lines = preprocess_data(pd.read_csv('data/order_lines.csv'), 'order_lines')

        max_id = order_lines['pick_id'].max() if 'pick_id' in order_lines.columns else 0
        id_generator = count(start=max_id + 1)
        duplicate_indices = order_lines[order_lines.duplicated('pick_id', keep=False)].index

        for index in duplicate_indices:
            order_lines.at[index, 'pick_id'] = next(id_generator)

        await load_data(session, product_master, ProductMaster)
        await load_data(session, orders, Orders)
        await load_data(session, order_lines, OrderLines)

async def get_session():
    async with AsyncSessionFactory() as session:
        yield session