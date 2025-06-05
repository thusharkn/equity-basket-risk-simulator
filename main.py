import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import datetime

def fetch_data(tickers, start="2022-01-01", end="2024-12-31"):
    start_dt = datetime.datetime.strptime(start, "%Y-%m-%d")
    end_dt = datetime.datetime.strptime(end, "%Y-%m-%d")

    all_data = {}
    for ticker in tickers:
        try:
            df = pdr.DataReader(ticker, 'yahoo', start_dt, end_dt)
            all_data[ticker] = df['Adj Close']
        except Exception as e:
            print(f"Error fetching {ticker}: {e}")
    
    return pd.DataFrame(all_data)

def calculate_portfolio_metrics(data, weights):
    returns = data.pct_change().dropna()
    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    portfolio_return = np.sum(mean_returns * weights) * 252
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
    sharpe_ratio = portfolio_return / portfolio_volatility

    return {
        "Expected Return": portfolio_return,
        "Volatility": portfolio_volatility,
        "Sharpe Ratio": sharpe_ratio
    }

def monte_carlo_simulation(data, weights, num_simulations=1000, num_days=252):
    returns = data.pct_change().dropna()
    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    portfolio_results = np.zeros((3, num_simulations))

    for i in range(num_simulations):
        simulated_returns = np.random.multivariate_normal(mean_returns, cov_matrix, num_days)
        portfolio_return = np.sum(np.dot(simulated_returns, weights))
        portfolio_volatility = np.std(np.dot(simulated_returns, weights))
        portfolio_results[0, i] = portfolio_return
        portfolio_results[1, i] = portfolio_volatility
        portfolio_results[2, i] = portfolio_return / portfolio_volatility

    return portfolio_results
