# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 15:31:47 2024

@author: bextr

"""

import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and **volume** of Google!

""")

# define the ticker symbol
tickerSymbol = 'GOOGL'
# get the data on this ticker
tickerData = yf.Ticker(tickerSymbol)   
#get historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2013-1-31', end='2023-1-31')
# Open  High    Low     Close   Volume  Dividends   Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
                              
                              
