from re import sub
from itertools import count

def convert_to_snake_case(s: str) -> str:
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

def new_pick_ids_for_duplicates(order_lines):
    max_id = order_lines['pick_id'].max() if 'pick_id' in order_lines.columns else 0
    id_generator = count(start=max_id + 1)
    duplicate_indices = order_lines[order_lines.duplicated('pick_id', keep=False)].index
    for index in duplicate_indices:
        order_lines.at[index, 'pick_id'] = next(id_generator)