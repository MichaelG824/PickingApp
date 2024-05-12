from repositories.pick_repository import PickRepository
import logging

class PickService:
    def __init__(self, db):
        self.pick_repository = PickRepository(db)

    async def get_pick_list_data(self):
        orders = await self.pick_repository.get_orders_with_order_lines()
        if not orders:
            logging.error("Could not find any orders with order_lines")
            raise Exception("No orders found within the database")

        pick_list_data = []
        for order in orders:
            order_lines = await self.pick_repository.get_order_lines(order.order_number)
            if not order_lines:
                continue
            order_data = {
                'order_number': order.order_number,
                'name': order.name,
                'order_date': order.order_date,
                'item_names': [
                    {
                        'title': line.product_master.title,
                        'sku': line.product_master.sku,
                        'location': line.location,
                        'pick_qty': line.pick_qty,
                        'pick_id': line.pick_id,
                        'status': line.status
                    } for line in order_lines
                ]
            }
            pick_list_data.append(order_data)
        return pick_list_data

    async def get_pick_by_id(self, pick_id: str):
        pick = await self.pick_repository.get_pick_by_id(pick_id)
        if not pick:
            raise Exception("Pick not found")
        pickDto = {
            'location': pick.location,
            'order': pick.order_number,
            'pick_id': pick.pick_id,
            'pick_qty': pick.pick_qty,
            'sku': pick.sku,
            'title': pick.product_master.title
        }
        return pickDto

    async def update_pick_status(self, request):
        order_line = await self.pick_repository.get_order_line_by_pick_id(request.pick_id)
        if not order_line:
            raise Exception("Order line not found")
        await self.pick_repository.update_order_line_status(order_line, request.status)