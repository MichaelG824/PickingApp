from pydantic import BaseModel

class PickModel(BaseModel):
    location: str
    order: str
    pick_id: int
    pick_qty: int
    sku: int
    title: str
