from models.db_table_model import Orders, OrderLines, ProductMaster
from database import get_session
from sqlalchemy import select, exists, text, distinct
from sqlalchemy.orm import joinedload
from models.pick_model import PickModel

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
            order=pick.order_number,
            pick_id=pick.pick_id,
            pick_qty=pick.pick_qty,
            sku=pick.sku,
            title=pick.product_master.title
        )

    async def get_order_line_by_pick_id(self, pick_id) -> OrderLines:
        result = await self.session.execute(
            select(OrderLines).filter(OrderLines.pick_id == pick_id)
        )
        return result.scalars().first()

    async def update_order_line_status(self, order_line, status) -> None:
        order_line.status = status
        await self.session.commit()