from pydantic import BaseModel

class GetPickByIdResponseDto(BaseModel):
    location: str
    order_number: str
    pick_id: int
    pick_qty: int
    sku: int
    title: str