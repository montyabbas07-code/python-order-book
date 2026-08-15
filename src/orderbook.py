from src.order import Order, Side

class OrderBook:
    def __init__(self):
        self.bids = {}      # price -> list of orders
        self.asks = {}      # price -> list of orders
        self.orders = {}    # order_id -> (price, side) for cancellation

    def add_order(self, order: Order):
        # TODO: implement matching next week
        if order.side == Side.BID:
            if order.price not in self.bids:
                self.bids[order.price] = []
            self.bids[order.price].append(order)
        else:
            if order.price not in self.asks:
                self.asks[order.price] = []
            self.asks[order.price].append(order)
        
        self.orders[order.id] = (order.price, order.side)

    def cancel_order(self, order_id: int) -> bool:
        if order_id not in self.orders:
            return False
        
        price, side = self.orders[order_id]
        del self.orders[order_id]
        
        if side == Side.BID:
            self.bids[price] = [o for o in self.bids[price] if o.id != order_id]
            if not self.bids[price]:
                del self.bids[price]
        else:
            self.asks[price] = [o for o in self.asks[price] if o.id != order_id]
            if not self.asks[price]:
                del self.asks[price]
        
        return True

    def get_best_bid(self):
        if not self.bids:
            return None
        return max(self.bids.keys())

    def get_best_ask(self):
        if not self.asks:
            return None
        return min(self.asks.keys())