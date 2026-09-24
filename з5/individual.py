import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = pd.read_csv('з5/SPFB.RTS.csv')
data['date_time'] = pd.to_datetime(data['<DATE>'].astype(str) + ' ' + data['<TIME>'].astype(str))
data = data.set_index('date_time')
data_hourly = data.resample('h').sum()
# data_hourly = data_hourly.reset_index()

candels_data = data_hourly[(data_hourly.index.month == 9) & (data_hourly.index.day == 17)]

candels_data = candels_data.rename({'<OPEN>' : "Open", '<HIGH>':"High" , "<LOW>" : "Low", "<CLOSE>" :"Close", "<VOL>" : "Volume"}, axis=1)


mpf.plot(candels_data,  type='candle', style='charles', volume=True)
mpf.show()