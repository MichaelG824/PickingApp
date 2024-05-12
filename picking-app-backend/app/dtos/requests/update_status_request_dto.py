from enums.status_enum import StatusEnum
from pydantic import BaseModel, Field

class UpdateStatusRequestDto(BaseModel):
    pick_id: int
    status: StatusEnum
    exception_details: str = Field(None, description="Optional details about the exception")
