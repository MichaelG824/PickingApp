from dtos.responses.get_pick_by_id_response_dto import GetPickByIdResponseDto
from models.pick_model import PickModel
from dtos.responses.pick_list_data_response_dto import PickListDataDto, OrderLineDto
from models.pick_list_data_model import PickListDataModel

def transform_to_get_pick_by_id_response_dto(pick: PickModel) -> GetPickByIdResponseDto:
    return GetPickByIdResponseDto(
        location=pick.location,
        order_number=pick.order_number,
        pick_id=pick.pick_id,
        pick_qty=pick.pick_qty,
        sku=pick.sku,
        title=pick.title
    )

def transform_pick_list_model_to_dto(pick_model: PickListDataModel) -> PickListDataDto:
    pick_line_data_dto = PickListDataDto(
        order_number=pick_model.order_number,
        name= pick_model.name,
        order_date= pick_model.order_date,
        order_lines=[
            OrderLineDto(
                title= line.title,
                sku= line.sku,
                location=line.location,
                pick_qty=line.pick_qty,
                pick_id=line.pick_id,
                status=line.status
            ) for line in pick_model.order_lines
        ]
    )
    return pick_line_data_dto
