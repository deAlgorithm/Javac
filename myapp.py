import pandas as pd
import yfinance as yf
import streamlit as st

st.write("""
# simple stock price app
shown are the **stock closing** closing price and **volume** of Apple!
"""
)

# https://towardsdatascience.com/how-to-stock-data-using-python-c0de1df17e75

#define the ticker symbol
tickerSymbol = 'AAPL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#het the historical prices for this ticker
tickerDf = tickerData.history(period ='1d', start = '2010-05-31', end = '2020-05-31')

# Open High Low Close Volume Dividends Stock Splits

st.write(
"""
### Closing Price 
"""
)

st.line_chart(tickerDf.Close)

st.write(
"""
### Volume Price 
"""
)
st.line_chart(tickerDf.Volume)
