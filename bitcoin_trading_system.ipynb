# Bitcoin Trading System: Panic Reversion Strategy
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Download BTC-USD historical data
btc = yf.download("BTC-USD", start="2018-01-01", end="2024-12-31")

# Calculate daily returns
btc['Return'] = btc['Adj Close'].pct_change()

# Define buy and sell rules
btc['Buy Signal'] = btc['Return'] < -0.05
btc['Sell Signal'] = btc['Adj Close'].rolling(5).mean()

# Backtest logic
btc['Position'] = 0  # 1 = long, 0 = no position
in_trade = False
entry_price = 0

for i in range(1, len(btc)):
    if not in_trade and btc['Buy Signal'].iloc[i]:
        btc['Position'].iloc[i] = 1
        entry_price = btc['Adj Close'].iloc[i]
        in_trade = True
    elif in_trade:
        btc['Position'].iloc[i] = 1
        # Sell if price returns to 5-day average
        if btc['Adj Close'].iloc[i] >= btc['Sell Signal'].iloc[i]:
            in_trade = False

# Calculate strategy returns
btc['Strategy Return'] = btc['Position'].shift(1) * btc['Return']
btc['Cumulative Return'] = (1 + btc['Return']).cumprod()
btc['Cumulative Strategy'] = (1 + btc['Strategy Return']).cumprod()

# Plot results
plt.figure(figsize=(14,6))
plt.plot(btc['Cumulative Return'], label='Buy & Hold', alpha=0.5)
plt.plot(btc['Cumulative Strategy'], label='Panic Reversion Strategy', color='orange')
plt.title('Bitcoin Trading System: Cumulative Returns')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
