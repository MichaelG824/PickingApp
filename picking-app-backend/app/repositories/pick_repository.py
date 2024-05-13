from models.db_table_model import Orders, OrderLines, ProductMaster
from sqlalchemy import select
from typing import Union, Optional, List
from enums.status_enum import StatusEnum

class PickRepository:
    def __init__(self, session):
        self.session = session

    async def get_orders_with_order_lines(self) -> List[Orders]:
        result = await self.session.execute(
            select(Orders)
            .join(OrderLines)
            .order_by(Orders.order_number)
            .distinct(Orders.order_number))
        return result.scalars().all()

    async def get_pick_by_id(self, pick_id: int) -> OrderLines:
        result = await self.session.execute(
            select(OrderLines).join(ProductMaster).filter(OrderLines.pick_id == pick_id)
        )
        return result.scalars().first()

    async def get_order_line_by_pick_id(self, pick_id: int) -> OrderLines:
        result = await self.session.execute(
            select(OrderLines).filter(OrderLines.pick_id == pick_id)
        )
        return result.scalars().first()

    async def update_order_line_status_and_exception_details(self, order_line: OrderLines, status: StatusEnum, exception_details: Union[str, None]) -> None:
        order_line.status = status
        order_line.exception_details = exception_details if exception_details else order_line.exception_details
        await self.session.commit()