from enum import Enum as PyEnum

class StatusEnum(str, PyEnum):
    Pending = "Pending"
    Picked = "Picked"
    Exception = "Exception"
