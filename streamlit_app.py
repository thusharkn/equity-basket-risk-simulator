import streamlit as st
import numpy as np
import pandas as pd
from main import fetch_data, calculate_portfolio_metrics, monte_carlo_simulation
import matplotlib.pyplot as plt

st.title("Equity Basket Risk Simulator")

tickers_input = st.text_input("Enter stock tickers (comma separated):", "AAPL,MSFT,GOOGL")
weights_input = st.text_input("Enter weights (comma separated):", "0.4,0.3,0.3")

tickers = [ticker.strip() for ticker in tickers_input.split(",")]
weights = np.array([float(w) for w in weights_input.split(",")])

data = fetch_data(tickers)

st.subheader("Portfolio Metrics")
metrics = calculate_portfolio_metrics(data, weights)
for key, value in metrics.items():
    st.write(f"{key}: {value:.4f}")

st.subheader("Monte Carlo Simulation")
simulations = monte_carlo_simulation(data, weights)
st.write("Mean Return of Simulations:", np.mean(simulations[0]))
st.write("Std Dev of Returns:", np.std(simulations[0]))

fig, ax = plt.subplots()
ax.hist(simulations[0], bins=50, alpha=0.7, color='blue')
ax.set_title("Distribution of Simulated Portfolio Returns")
st.pyplot(fig)
