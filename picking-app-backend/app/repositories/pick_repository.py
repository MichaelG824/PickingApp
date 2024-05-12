from models.db_table_model import Orders, OrderLines, ProductMaster
from sqlalchemy import select
from models.pick_model import PickModel
from typing import Union
from enums.status_enum import StatusEnum

class PickRepository:
    def __init__(self, session):
        self.session = session

    async def get_orders_with_order_lines(self):
        result = await self.session.execute(
            select(Orders)
            .join(OrderLines)
            .order_by(Orders.order_number)
            .distinct(Orders.order_number))
        return result.scalars().all()

    async def get_pick_by_id(self, pick_id: int) -> PickModel:
        result = await self.session.execute(
            select(OrderLines).join(ProductMaster).filter(OrderLines.pick_id == pick_id)
        )
        pick = result.scalars().first()
        return PickModel(
            location=pick.location,
            order_number=pick.order_number,
            pick_id=pick.pick_id,
            pick_qty=pick.pick_qty,
            sku=pick.sku,
            title=pick.product_master.title
        )

    async def get_order_line_by_pick_id(self, pick_id: int) -> OrderLines:
        result = await self.session.execute(
            select(OrderLines).filter(OrderLines.pick_id == pick_id)
        )
        return result.scalars().first()

    async def update_order_line_status_and_exception_details(self, order_line: OrderLines, status: StatusEnum, exception_details: Union[str, None]) -> None:
        order_line.status = status
        order_line.exception_details = exception_details if exception_details else order_line.exception_details
        await self.session.commit()