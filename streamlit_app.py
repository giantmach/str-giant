import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import OpenDartReader
import yfinance as yf
import plotly.graph_objects as go

import time


def main():
    with st.sidebar:
        with st.echo():
            st.write("This code")

        with st.spinner("Loading..."):
            time.sleep(1)
        st.success("Done!")
        
        add_radio = st.radio(
            "Choose a shipping method",
            ("Standard (5-15 days)", "Express (2-5 days)")
        )
        
        add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
    )


    st.title("🎈 My new app")
    st.write(
        "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/). 추가 텍스트 디벅모드"
    )
    
    
    #my_api = '<<<YOUR AUTHENTICATION KEY HERE>>>'
    
    dart = OpenDartReader(my_api)
    
    corp_info(dart)
    st.pyplot(matplt_obj(dart))


def corp_info(dart):
    

    dart.list('에코프로비엠').head(5)
    st.write(
            dart.list('에코프로비엠').head(5)
        )

#matplotlib 활용한 데이터와 시각화 객체 생성
def matplt_obj(dart):

    stmt_l = []
    for year in range(2015, 2023):
        stmt = dart.finstate('삼성전자', year, '11011')
        stmt = stmt.loc[stmt.fs_nm == '연결재무제표']
        stmt = stmt.loc[stmt.account_nm.isin(['매출액', '영업이익', '당기순이익'])]
        stmt = stmt[['bsns_year', 'account_nm', 'thstrm_amount']]
        stmt_l.append(stmt)
        
    _MAN = 10000
    _JO = _MAN * _MAN * _MAN

    stmt_df = pd.concat(stmt_l)
    stmt_df.set_index('bsns_year', inplace = True)
    stmt_df['thstrm_amount'] = stmt_df.thstrm_amount.str.replace(',', '').astype(int) / _JO
    stmt_df = stmt_df.pivot(columns = 'account_nm')
    stmt_df.columns = ['Net Income', 'Revenue', 'Operating Profit']

    sns.set_style('whitegrid')
    stmt_df.plot()
    plt.title('Samsung Electronics')
    plt.xlabel('Year')
    plt.ylabel('Jo Wons')
    
    return plt
    #plt.show()
    #st.pyplot(plt)


if __name__ == '__main__':
    main()
    
    
    
    
#def main():







    

    


    # #여기부터 plotly 그리기
    # #symbol = ["8058.T", "8031.T", "8053.T", "8002.T"]
    # #미쓰비시 상사, 미쓰이 물산, 스미토모 상사, 마루베니

    # # Retrieve AAPL historical data
    # #symbol = "8058.T"
    # symbol = "QQQ"
    # ticker = yf.Ticker(symbol)

    # data = ticker.history(period="3mo") #mo, wk, y

    # # Remove timezone information
    # data.index = data.index.tz_localize(None)  
    # #data.to_excel('AAPL_data_일봉.xlsx')


    # #이것도 의외로 interval="1wk"와 같은 결과가 나옴.. 단, 그주의 첫날을 일요일로 보고 당겨서 보여주는 듯
    # data = ticker.history(period="1mo") #mo, wk, y
    # data = data.resample('W').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'}) 

    # # Remove timezone information
    # data.index = data.index.tz_localize(None)  
    # #data.to_excel('AAPL_data_리샘플W.xlsx')

    # # Set interval to '1wk' for weekly data 주봉으로 표현하려면 ... 단, 그주의 첫날을 월요일로 보고 당겨서 보여주는 듯
    # data = ticker.history(period="1y", interval="1wk")  

    # # Remove timezone information
    # data.index = data.index.tz_localize(None)  
    # #data.to_excel('AAPL_data_주봉.xlsx')



    # # Create candlestick chart
    # fig = go.Figure(data=[go.Candlestick(x=data.index,
    #                                     open=data['Open'],
    #                                     high=data['High'],
    #                                     low=data['Low'],
    #                                     close=data['Close'],
    #                                     increasing_line_color='red',
    #                                     decreasing_line_color='blue')])

    # # Customize the chart layout
    # fig.update_layout(title=f"{symbol} Candlestick Chart ",
    #                 yaxis_title="Price",
    #                 xaxis_rangeslider_visible=True,
    #                 width=1200)  # Set width to 800 pixels


    # # Display the chart
    # #fig.show()

    # #컬럼 레이아웃
    # col1, col2 = st.columns(2)
    # with col1:
    #     st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    # with col2:
    #     st.pyplot(plt)


#Tab 레이아웃
# tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
# with tab1:
#     # Use the Streamlit theme.
#     # This is the default. So you can also omit the theme argument.

#     st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# with tab2:
#     # Use the native Plotly theme.
#     st.pyplot(plt)
#     #st.plotly_chart(plt, theme=None, use_container_width=True)
