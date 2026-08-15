# Limit Order Book Engine

A limit order book (LOB) matching engine built in Python, with price-time priority matching. Designed for eventual porting of performance-critical components to C and C++.

## What is a Limit Order Book?

A limit order book is the core data structure used by financial exchanges to match buy and sell orders. It stores resting orders and executes trades when a buyer's bid price meets or exceeds a seller's ask price, following **price-time priority**: the best price fills first, and at the same price, the earliest order fills first.

## Features

- [x] Order entry with price, quantity, side, and timestamp
- [ ] Price-time priority matching engine
- [ ] Partial and full fill support
- [ ] Order cancellation
- [ ] Best bid, best ask, and spread reporting
- [ ] Depth at price level
- [ ] Benchmark suite

## Architecture
