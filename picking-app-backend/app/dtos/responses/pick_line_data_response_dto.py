from pydantic import BaseModel
from typing import List, Optional

class OrderLineDTO(BaseModel):
    title: str
    sku: int
    location: str
    pick_qty: int
    pick_id: int
    status: str

class PickLineDataResponseDto(BaseModel):
    order_number: str
    name: str
    order_date: str
    item_names: List[OrderLineDTO]
