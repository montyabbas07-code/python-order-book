# Limit Order Book Engine

A limit order book (LOB) matching engine built in Python, with price-time priority. Designed for eventual porting of performance-critical components to C and C++.

## What is a Limit Order Book?

A limit order book is the core data structure used by financial exchanges to match buy and sell orders. It stores resting orders and executes trades when a buyer's bid price meets or exceeds a seller's ask price, following **price-time priority**: the best price fills first, and at the same price, the earliest order fills first.

## Features

- [x] Order entry with price, quantity, side, and timestamp
- [x] Price-time priority matching engine
- [x] Partial and full fill support
- [x] Order cancellation
- [x] Best bid, best ask, and spread reporting
- [ ] Depth at price level
- [x] Benchmark suite

## Architecture

```
Order (Python dataclass)
    |
    v
OrderBook (matching engine)
    |
    +---> Trades
    +---> Updated book state (bids/asks)
```

## Installation

```bash
git clone https://github.com/montyabbas07-code/python-order-book.git
cd python-order-book
pip install -r requirements.txt
```

## Testing

```bash
python -m pytest tests/
```

## Performance

| Metric | Value | Notes |
|--------|-------|-------|
| Resting order throughput | ~1,280,000 orders/sec | Python 3.13, Windows. Non-crossing workload (dictionary inserts). |
| Matching throughput | Not yet benchmarked | Requires crossing-price workload. |

## Future Work

- Port matching engine to C (FOA coursework integration)
- Port to C++ with `std::map` for price levels and `std::thread` for concurrency
- TCP socket interface for external order entry
- Lock-free queue for the matching hot path
- Realistic crossing benchmark

## Why I Built This

After taking **Principles of Finance** and **Introductory Microeconomics**, I became interested in how financial markets price and allocate risk. The most interesting part was not the theory, but the systems underneath — the matching engines that process millions of orders per second. This project is my attempt to understand and build that infrastructure from the ground up.

## License

MIT
