import yfinance as yf
import pandas as pd
from yahoofinancials import yahoofinancials

tsla_stock = yf.download('TSLA',start='2022-01-01',end='2022-03-31')
print(tsla_stock)
