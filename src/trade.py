from dataclasses import dataclass

@dataclass
class Trade:
    trade_id: int
    bid_order_id: int
    ask_order_id: int
    price: float
    quantity: int