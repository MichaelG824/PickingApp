from enums.status_enum import StatusEnum
from pydantic import BaseModel, Field
from typing import Optional

class UpdateStatusRequestDto(BaseModel):
    pick_id: int
    status: StatusEnum
    exception_details: Optional[str]
