from models.models import Orders, OrderLines, ProductMaster
from database import get_session
from sqlalchemy import select, exists

class PickRepository:
    def __init__(self, db):
        self.db = db

    async def get_orders_with_order_lines(self):
        query = (
            select(Orders)
        )
        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_order_lines(self, order_number):
        result = await self.db.execute(
            select(OrderLines).join(ProductMaster).filter(OrderLines.order_number == order_number)
        )
        return result.scalars().all()

    async def get_pick_by_id(self, pick_id):
        result = await self.db.execute(
            select(OrderLines).join(ProductMaster).filter(OrderLines.pick_id == pick_id)
        )
        return result.scalars().first()

    async def get_order_line_by_pick_id(self, pick_id):
        result = await self.db.execute(
            select(OrderLines).filter(OrderLines.pick_id == pick_id)
        )
        return result.scalars().first()

    async def update_order_line_status(self, order_line, status):
        order_line.status = status
        await self.db.commit()