from enum import Enum

class StatusEnum(str, Enum):
    Pending = "Pending"
    Picked = "Picked"
    Exception = "Exception"
