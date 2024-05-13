from repositories.pick_repository import PickRepository
from dtos.requests.update_status_request_dto import UpdateStatusRequestDto
from dtos.responses.get_pick_by_id_response_dto import GetPickByIdResponseDto
from transformers.model_to_dto import transform_to_get_pick_by_id_response_dto, transform_pick_list_model_to_dto
from transformers.record_to_model import transform_pick_record_to_model, transform_order_record_to_pick_list_data_model
from dtos.responses.pick_list_data_response_dto import PickListDataResponseDto

class PickService:
    def __init__(self, session):
        self.pick_repository = PickRepository(session)

    async def get_pick_list_data(self) -> PickListDataResponseDto:
        orders = await self.pick_repository.get_orders_with_order_lines()
        if not orders:
            return []
        pick_list_data_result = []
        for order in orders:
            pick_list_model = transform_order_record_to_pick_list_data_model(order)
            pick_list_data_dto = transform_pick_list_model_to_dto(pick_list_model)
            pick_list_data_result.append(pick_list_data_dto)
        return { "pick_list_data": pick_list_data_result }

    async def get_pick_by_id(self, pick_id: str) -> GetPickByIdResponseDto:
        pick_record = await self.pick_repository.get_order_line_by_pick_id(int(pick_id))
        pick_model = transform_pick_record_to_model(pick_record)
        if not pick_model:
            raise Exception("Pick Model not found")
        return transform_to_get_pick_by_id_response_dto(pick_model)

    async def update_order_line_status_and_exception_details(self, request: UpdateStatusRequestDto) -> None:
        order_line_record = await self.pick_repository.get_order_line_by_pick_id(request.pick_id)
        if not order_line_record:
            raise Exception("Order line record not found")
        exception_details = request.exception_details if request.exception_details else None
        await self.pick_repository.update_order_line_status_and_exception_details(order_line_record, request.status, exception_details)