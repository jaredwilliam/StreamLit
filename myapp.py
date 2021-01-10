import yfinance as yf
import streamlit as st
import pandas as pd

# To run this file:
# Open command prompt, cd to file
# > streamlit run filename.py

# This write fucntion allows us to write in markdown
st.write("""
## Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

# Define ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open  High    Low Close   Volume  Dividends   Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
