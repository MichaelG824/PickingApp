from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, ProductMaster, Orders, OrderLines
import pandas as pd
import uuid
from itertools import count

DATABASE_URL = "sqlite:///warehouse.db"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

def initialize_database():
    Base.metadata.create_all(engine)

def load_data(session, df, table_class):
    try:
        df.columns = df.columns.str.strip()  # Strip spaces from column headers
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)  # Strip spaces from string values
        print(df)
        session.bulk_insert_mappings(table_class, df.to_dict(orient='records'))
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error loading data into {table_class.__tablename__}: {e}")

def load_initial_data():
    with Session() as session:
        # Load CSV data into DataFrames
        product_master = pd.read_csv('data/product_master.csv')
        orders = pd.read_csv('data/orders.csv')
        order_lines = pd.read_csv('data/order_lines.csv')

        max_id = order_lines['pick_id'].max()

        id_generator = count(start=max_id + 1)

        duplicate_indices = order_lines[order_lines.duplicated('pick_id', keep=False)].index

        # Assign new IDs to duplicates
        for index in duplicate_indices:
            order_lines.at[index, 'pick_id'] = next(id_generator)

        # Load data into the database
        load_data(session, product_master, ProductMaster)
        load_data(session, orders, Orders)
        load_data(session, order_lines, OrderLines)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

if __name__ == '__main__':
    initialize_database()
    load_initial_data()
