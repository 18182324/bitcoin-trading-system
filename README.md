# Bitcoin Panic Reversion Trading System

This repository contains a simple mean-reversion trading strategy for Bitcoin (BTC-USD), based on detecting short-term panic sell-offs followed by price recovery.

## 📈 Strategy Overview

- **Buy Signal**: Triggered when Bitcoin drops more than -5% in a single day.
- **Sell Signal**: Exit when price recovers to its 5-day average.
- **Backtest Period**: 2018 – 2024

## 🧪 Files

- `bitcoin_trading_system.ipynb`: Full Jupyter Notebook with strategy code and backtest.
- `requirements.txt`: Python dependencies.

## 🛠️ Setup Instructions

```bash
pip install -r requirements.txt
