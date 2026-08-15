from src.order import Order, Side

def test_order_creation():
    order = Order(id=1, price=10.50, quantity=100, side=Side.BID, timestamp=1)
    assert order.price == 10.50
    assert order.side == Side.BID