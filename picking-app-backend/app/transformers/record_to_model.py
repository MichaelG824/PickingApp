from models.pick_model import PickModel
from models.pick_list_data_model import OrderLineModel, PickListDataModel
from models.db_table_model import Orders, OrderLines

def transform_order_line_record_to_pick_model(order_line: OrderLines) -> PickModel:
    return PickModel(
       location=order_line.location,
       order_number=order_line.order_number,
       pick_id=order_line.pick_id,
       pick_qty=order_line.pick_qty,
       sku=order_line.sku,
       title=order_line.product_master.title
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