from src.order import Order, Side
from src.orderbook import OrderBook

def main():
    book = OrderBook()
    
    print("=== Adding resting orders ===")
    book.add_order(Order(id=1, price=100.00, quantity=500, side=Side.BID, timestamp=1))
    book.add_order(Order(id=2, price=101.00, quantity=300, side=Side.BID, timestamp=2))
    book.add_order(Order(id=3, price=102.50, quantity=200, side=Side.ASK, timestamp=3))
    
    print(f"Best bid: {book.get_best_bid()}")
    print(f"Best ask: {book.get_best_ask()}")
    print(f"Spread: {book.get_best_ask() - book.get_best_bid()}")
    
    print("\n=== Aggressive order that crosses ===")
    trades = book.add_order(Order(id=4, price=102.00, quantity=400, side=Side.BID, timestamp=4))
    
    print(f"Number of trades: {len(trades)}")
    for t in trades:
        print(f"  Trade {t.trade_id}: {t.quantity} shares @ ${t.price}")
        print(f"    Matched bid #{t.bid_order_id} with ask #{t.ask_order_id}")
    
    print(f"\nBest bid after match: {book.get_best_bid()}")

if __name__ == "__main__":
    main()