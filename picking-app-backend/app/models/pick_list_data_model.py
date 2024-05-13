from pydantic import BaseModel
from typing import List, Optional

class OrderLineModel(BaseModel):
    title: str
    sku: int
    location: str
    pick_qty: int
    pick_id: int
    status: str

class PickListDataModel(BaseModel):
    order_number: str
    name: str
    order_date: str
    order_lines: List[OrderLineModel]
