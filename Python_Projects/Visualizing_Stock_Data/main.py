# VISUALIZING STOCK DATA WITH CANDLESTICK CHARTS 

import pandas as pd
import datetime as dt
import pandas_datareader as web
import matplotlib.dates as mdates
import matplotlib.pyplot as plt 
from mplfinance.original_flavor import candlestick_ohlc


# define Time Frame

Year = int(input("Enter: "))
start = dt.datetime(Year,1,1)
end = dt.datetime.now()

# Load data for the specific stock
Company_stock_symbol = input("Enter the symbol: ")
data = web.DataReader(Company_stock_symbol, 'yahoo', start, end)


# Restructure Data     

data = data[['High','Low','Open','Close','Adj Close']]

data.reset_index(inplace = True)
data['Date'] = data['Date'].map(mdates.date2num)


# visualization 

ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title('{} Share Price'.format(Company_stock_symbol), color='white')
# ax.figure.canvas.set_window_title('Mohit Stock Visualizer v0.1 Alpha')
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.xaxis_date()

# Plot The Candlestick Chart
candlestick_ohlc(ax, data.values, width=0.5, colorup='g', colordown='r')
plt.show()


