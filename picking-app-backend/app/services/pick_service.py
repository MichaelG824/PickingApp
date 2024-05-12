from repositories.pick_repository import PickRepository
from dtos.requests.update_status_request_dto import UpdateStatusRequestDto
from dtos.responses.get_pick_by_id_response_dto import GetPickByIdResponseDto
from transformers.model_to_dto import transform_to_get_pick_by_id_response_dto, transform_order_with_line_data_to_pick_line_data_dto
class PickService:
    def __init__(self, session):
        self.pick_repository = PickRepository(session)

    async def get_pick_list_data(self):
        orders = await self.pick_repository.get_orders_with_order_lines()
        if not orders:
            return []
        pick_list_data_result = []
        for order in orders:
            pick_list_data = transform_order_with_line_data_to_pick_line_data_dto(order)
            pick_list_data_result.append(pick_list_data)
        return pick_list_data_result

    async def get_pick_by_id(self, pick_id: str) -> GetPickByIdResponseDto:
        pick = await self.pick_repository.get_pick_by_id(int(pick_id))
        if not pick:
            raise Exception("Pick not found")
        return transform_to_get_pick_by_id_response_dto(pick)

    async def update_order_line_status_and_exception_details(self, request: UpdateStatusRequestDto) -> None:
        order_line = await self.pick_repository.get_order_line_by_pick_id(request.pick_id)
        if not order_line:
            raise Exception("Order line not found")
        exception_details = request.exception_details if request.exception_details else None
        await self.pick_repository.update_order_line_status_and_exception_details(order_line, request.status, exception_details)