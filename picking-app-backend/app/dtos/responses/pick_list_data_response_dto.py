from pydantic import BaseModel
from typing import List, Optional

class OrderLineDto(BaseModel):
    title: str
    sku: int
    location: str
    pick_qty: int
    pick_id: int
    status: str

class PickListDataDto(BaseModel):
    order_number: str
    name: str
    order_date: str
    order_lines: List[OrderLineDto]

class PickListDataResponseDto(BaseModel):
    pick_list_data: List[PickListDataDto]
