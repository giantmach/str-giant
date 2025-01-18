

#@2025.1.6에 중단한 코드
#pandas_datareader가 일몰되어서.. yfinance 기반 코드로 변환하다 실패함 
#pandas dataframe을 더 공부하고 다시 시도해 보자


# https://dacon.io/codeshare/2588  여기 코드로 다시 시작하는 게 좋을 듯






import streamlit as st

#이것도 디프리시에트 되어서.. yfinance로 수정
#import pandas_datareader.data as web 

#아래 두 줄은 약간 국룰 같은 거
import pandas as pd
from pandas import Series, DataFrame

import yfinance as yf
import datetime
import matplotlib.pyplot as plt
#최초 구글링한 코드에서 mpl_finance가 defrecated되어서 mplfinance로 바꾸었고, 캔들 차트만 뽑아서 import
from mplfinance.original_flavor import candlestick2_ohlc
import matplotlib.ticker as ticker

start = datetime.datetime(2016, 3, 1)
end = datetime.datetime(2016, 3, 31)
#skhynix = web.DataReader("000660.KS", "yahoo", start, end)

skhynix = yf.download("NVDA", start, end)


#
#skhynix = DataFrame.astype(float)
st.write(skhynix.head())
#skhynix.astype(dtype='float',errors='ignore')
#skhynix = DataFrame.astype(dtype='float',errors='coerce',)
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

day_list = []
name_list = []
for i, day in enumerate(skhynix.index):
    if day.dayofweek == 0:
        day_list.append(i)
        name_list.append(day.strftime('%Y-%m-%d') + '(Mon)')


st.write(name_list)
st.write(day_list)
#ax.xaxis.set_major_locator(ticker.FixedLocator(day_list))

#ax.xaxis.set_major_formatter(ticker.FixedFormatter(name_list))

candlestick2_ohlc(ax, skhynix['Open'], skhynix['High'], skhynix['Low'], skhynix['Close'], width=0.5, colorup='r', colordown='b')
plt.grid()
plt.show()

st.pyplot(plt)