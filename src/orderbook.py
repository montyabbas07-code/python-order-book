from src.order import Order, Side
from src.trade import Trade

class OrderBook:
    def __init__(self):
        self.bids = {}      # price -> list of orders
        self.asks = {}      # price -> list of orders
        self.orders = {}    # order_id -> (price, side) for cancellation

    def add_order(self, order: Order):
        trades = []
        
        if order.side == Side.BID:
            # Try to match against asks (lowest ask first)
            while (order.quantity > 0 and 
                   self.asks and 
                   min(self.asks.keys()) <= order.price):
                
                best_ask_price = min(self.asks.keys())
                resting_ask = self.asks[best_ask_price][0]  # FIFO within price
                
                trade_qty = min(order.quantity, resting_ask.quantity)
                trade = Trade(
                    trade_id=len(trades) + 1,
                    bid_order_id=order.id,
                    ask_order_id=resting_ask.id,
                    price=resting_ask.price,
                    quantity=trade_qty
                )
                trades.append(trade)
                
                # Update quantities
                order.quantity -= trade_qty
                resting_ask.quantity -= trade_qty
                
                # Remove filled resting order
                if resting_ask.quantity == 0:
                    self.asks[best_ask_price].pop(0)
                    if not self.asks[best_ask_price]:
                        del self.asks[best_ask_price]
                        del self.orders[resting_ask.id]
                    else:
                        del self.orders[resting_ask.id]
            
            # Add remaining quantity to book
            if order.quantity > 0:
                if order.price not in self.bids:
                    self.bids[order.price] = []
                self.bids[order.price].append(order)
                self.orders[order.id] = (order.price, order.side)
        
        else:  # ASK
            # Try to match against bids (highest bid first)
            while (order.quantity > 0 and 
                   self.bids and 
                   max(self.bids.keys()) >= order.price):
                
                best_bid_price = max(self.bids.keys())
                resting_bid = self.bids[best_bid_price][0]
                
                trade_qty = min(order.quantity, resting_bid.quantity)
                trade = Trade(
                    trade_id=len(trades) + 1,
                    bid_order_id=resting_bid.id,
                    ask_order_id=order.id,
                    price=resting_bid.price,
                    quantity=trade_qty
                )
                trades.append(trade)
                
                order.quantity -= trade_qty
                resting_bid.quantity -= trade_qty
                
                if resting_bid.quantity == 0:
                    self.bids[best_bid_price].pop(0)
                    if not self.bids[best_bid_price]:
                        del self.bids[best_bid_price]
                        del self.orders[resting_bid.id]
                    else:
                        del self.orders[resting_bid.id]
            
            if order.quantity > 0:
                if order.price not in self.asks:
                    self.asks[order.price] = []
                self.asks[order.price].append(order)
                self.orders[order.id] = (order.price, order.side)
        
        return trades

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