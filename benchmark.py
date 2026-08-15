import time
from src.orderbook import OrderBook, Order, Side

def benchmark():
    book = OrderBook()
    
    # Generate 100,000 random orders
    orders = []
    for i in range(100_000):
        side = Side.BID if i % 2 == 0 else Side.ASK
        price = 100.0 + (i % 100) * 0.01  # Prices from 100.00 to 100.99
        orders.append(Order(
            id=i,
            price=price,
            quantity=100,
            side=side,
            timestamp=i
        ))
    
    start = time.perf_counter()
    for order in orders:
        book.add_order(order)
    elapsed = time.perf_counter() - start
    
    throughput = len(orders) / elapsed
    
    print(f"Processed {len(orders):,} orders in {elapsed:.4f} seconds")
    print(f"Throughput: {throughput:,.0f} orders/second")

if __name__ == "__main__":
    benchmark()