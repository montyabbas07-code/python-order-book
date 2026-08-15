from src.order import Order, Side
from src.orderbook import OrderBook

def test_order_creation():
    order = Order(id=1, price=10.50, quantity=100, side=Side.BID, timestamp=1)
    assert order.price == 10.50
    assert order.side == Side.BID

def test_empty_book():
    book = OrderBook()
    assert book.get_best_bid() is None
    assert book.get_best_ask() is None

def test_add_bid():
    book = OrderBook()
    order = Order(id=1, price=10.50, quantity=100, side=Side.BID, timestamp=1)
    book.add_order(order)
    assert book.get_best_bid() == 10.50

def test_add_ask():
    book = OrderBook()
    order = Order(id=2, price=11.00, quantity=50, side=Side.ASK, timestamp=2)
    book.add_order(order)
    assert book.get_best_ask() == 11.00

def test_cancel_order():
    book = OrderBook()
    order = Order(id=1, price=10.50, quantity=100, side=Side.BID, timestamp=1)
    book.add_order(order)
    assert book.cancel_order(1) is True
    assert book.get_best_bid() is None
    assert book.cancel_order(1) is False