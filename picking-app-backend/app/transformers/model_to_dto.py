from dtos.responses.get_pick_by_id_response_dto import GetPickByIdResponseDto
from models.pick_model import PickModel
from dtos.responses.pick_line_data_response_dto import PickLineDataResponseDto, OrderLineDTO

def transform_to_get_pick_by_id_response_dto(pick: PickModel) -> GetPickByIdResponseDto:
    return GetPickByIdResponseDto(
        location=pick.location,
        order_number=pick.order_number,
        pick_id=pick.pick_id,
        pick_qty=pick.pick_qty,
        sku=pick.sku,
        title=pick.title
    )

def transform_order_with_line_data_to_pick_line_data_dto(order) -> PickLineDataResponseDto:
    pick_line_data_dto = PickLineDataResponseDto(
        order_number=order.order_number,
        name=order.name,
        order_date=order.order_date,
        item_names=[
            OrderLineDTO(
                title=line.product_master.title,
                sku=line.product_master.sku,
                location=line.location,
                pick_qty=line.pick_qty,
                pick_id=line.pick_id,
                status=line.status
            ) for line in order.order_lines
        ]
    )
    return pick_line_data_dto
