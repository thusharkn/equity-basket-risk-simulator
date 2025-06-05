# Equity Basket Risk Simulator

A Python-based analytical tool that simulates portfolio metrics for custom equity baskets.

## Features
- Fetches historical stock price data
- Computes expected return, volatility, Sharpe ratio
- Performs Monte Carlo simulations on portfolio returns
- Streamlit UI for easy interaction

## To Run
1. Install requirements:
```
pip install -r requirements.txt
```
2. Start the app:
```
streamlit run streamlit_app.py
```

## Inputs
- Tickers: Comma-separated (e.g., AAPL,MSFT,GOOGL)
- Weights: Comma-separated, must sum to 1 (e.g., 0.4,0.3,0.3)
