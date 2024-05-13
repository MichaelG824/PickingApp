from models.pick_model import PickModel
from models.pick_list_data_model import OrderLineModel, PickListDataModel
from models.db_table_model import Orders

def transform_order_line_record_to_pick_model(pick_record) -> PickModel:
    return PickModel(
       location=pick_record.location,
       order_number=pick_record.order_number,
       pick_id=pick_record.pick_id,
       pick_qty=pick_record.pick_qty,
       sku=pick_record.sku,
       title=pick_record.product_master.title
    )

def transform_order_record_to_pick_list_data_model(order: Orders) -> PickListDataModel:
    pick_list_data_model = PickListDataModel(
        order_number=order.order_number,
        name=order.name,
        order_date=order.order_date,
        order_lines=[
            OrderLineModel(
                title=line.product_master.title,
                sku=line.product_master.sku,
                location=line.location,
                pick_qty=line.pick_qty,
                pick_id=line.pick_id,
                status=line.status
            ) for line in order.order_lines
        ]
    )
    return pick_list_data_model