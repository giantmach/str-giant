# 캔들 스틱으로 보여주는 모범 코드 @2024.11.8 기준

import yfinance as yf
import plotly.graph_objects as go


#symbol = ["8058.T", "8031.T", "8053.T", "8002.T"]
#미쓰비시 상사, 미쓰이 물산, 스미토모 상사, 마루베니

# Retrieve AAPL historical data
#symbol = "8058.T"
symbol = "QQQ"
ticker = yf.Ticker(symbol)

data = ticker.history(period="3mo") #mo, wk, y

# Remove timezone information
data.index = data.index.tz_localize(None)  
#data.to_excel('AAPL_data_일봉.xlsx')


#이것도 의외로 interval="1wk"와 같은 결과가 나옴.. 단, 그주의 첫날을 일요일로 보고 당겨서 보여주는 듯
data = ticker.history(period="1mo") #mo, wk, y
data = data.resample('W').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'}) 

# Remove timezone information
data.index = data.index.tz_localize(None)  
#data.to_excel('AAPL_data_리샘플W.xlsx')

# Set interval to '1wk' for weekly data 주봉으로 표현하려면 ... 단, 그주의 첫날을 월요일로 보고 당겨서 보여주는 듯
data = ticker.history(period="1y", interval="1wk")  

# Remove timezone information
data.index = data.index.tz_localize(None)  
#data.to_excel('AAPL_data_주봉.xlsx')



# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(x=data.index,
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close'],
                                     increasing_line_color='red',
                                     decreasing_line_color='blue')])

# Customize the chart layout
fig.update_layout(title=f"{symbol} Candlestick Chart ",
                  yaxis_title="Price",
                  xaxis_rangeslider_visible=True,
                  width=1200)  # Set width to 800 pixels


# Display the chart
fig.show()