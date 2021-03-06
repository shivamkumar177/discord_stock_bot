from tracemalloc import start
import yfinance as yf
import pandas as pd
from pathlib import Path
pd.options.plotting.backend = "plotly"
# from yahoofinancials import yahoofinancials

def download_file(stock, start_date, end_date):
    return yf.download(stock,start=start_date,end=end_date)

stock = 'TSLA'
output_file = '{}.csv'.format(stock)
csv_output_dir = Path('stock_csv')
csv_output_dir.mkdir(parents=True, exist_ok=True)
tsla_stock = download_file(stock, start_date='2022-06-18', end_date='2022-06-28')
# plot graph
fig = tsla_stock.plot()
fig.show()
png_output_dir = Path("stock_png")
png_output_dir.mkdir(parents=True, exist_ok=True)
png_output_file = "{}.png".format(stock)
fig.write_image(png_output_dir/png_output_file)
tsla_stock.to_csv(csv_output_dir/output_file, encoding='utf-8')
