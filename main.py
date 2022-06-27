import yfinance as yf
import pandas as pd
from pathlib import Path
# from yahoofinancials import yahoofinancials

stock = 'TSLA'
output_file = '{}.csv'.format(stock)
output_dir = Path('stock_csv')
output_dir.mkdir(parents=True, exist_ok=True)
tsla_stock = yf.download(stock,start='2022-01-01',end='2022-03-31')
tsla_stock.to_csv(output_dir/output_file, encoding='utf-8')
