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

def test_full_match():
    book = OrderBook()
    bid = Order(id=1, price=10.50, quantity=100, side=Side.BID, timestamp=1)
    ask = Order(id=2, price=10.50, quantity=100, side=Side.ASK, timestamp=2)
    
    book.add_order(bid)
    trades = book.add_order(ask)
    
    assert len(trades) == 1
    assert trades[0].quantity == 100
    assert trades[0].price == 10.50
    assert book.get_best_bid() is None
    assert book.get_best_ask() is None

def test_partial_fill():
    book = OrderBook()
    bid = Order(id=1, price=10.50, quantity=100, side=Side.BID, timestamp=1)
    ask = Order(id=2, price=10.50, quantity=40, side=Side.ASK, timestamp=2)
    
    book.add_order(bid)
    trades = book.add_order(ask)
    
    assert len(trades) == 1
    assert trades[0].quantity == 40
    assert book.get_best_bid() == 10.50  # Remaining 60 still resting

def test_price_priority():
    book = OrderBook()
    # Two asks at different prices
    ask1 = Order(id=1, price=10.50, quantity=100, side=Side.ASK, timestamp=1)
    ask2 = Order(id=2, price=10.40, quantity=100, side=Side.ASK, timestamp=2)
    bid = Order(id=3, price=10.60, quantity=100, side=Side.BID, timestamp=3)
    
    book.add_order(ask1)
    book.add_order(ask2)
    trades = book.add_order(bid)
    
    # Should match with cheaper ask (10.40), not 10.50
    assert trades[0].price == 10.40

def test_time_priority():
    book = OrderBook()
    # Two asks at same price, different times
    ask1 = Order(id=1, price=10.50, quantity=60, side=Side.ASK, timestamp=1)
    ask2 = Order(id=2, price=10.50, quantity=60, side=Side.ASK, timestamp=2)
    bid = Order(id=3, price=10.60, quantity=100, side=Side.BID, timestamp=3)
    
    book.add_order(ask1)
    book.add_order(ask2)
    trades = book.add_order(bid)
    
    # Should fill ask1 first (60), then ask2 (40 remaining)
    assert trades[0].quantity == 60
    assert trades[1].quantity == 40