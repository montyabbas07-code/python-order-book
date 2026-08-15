from dataclasses import dataclass
from enum import Enum, auto

class Side(Enum):
    BID = auto()
    ASK = auto()

@dataclass
class Order:
    id: int
    price: float
    quantity: int
    side: Side
    timestamp: int