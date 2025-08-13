import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd

st.title('Analysis')
st.divider()
col1, col2 = st.columns([1, 1.618], gap = 'small') 

# intialize session state for user input
if 'portfolio' not in st.session_state:
    st.session_state['portfolio'] = []

if 'pe_score' not in st.session_state:
    st.session_state['pe_score'] = []
   

# user input in sidebar
with st.sidebar:
    st.title('Portfolio Information 💼')
    st.write('')
    st.divider()
    ticker = st.selectbox('Select a Stock Ticker:', ('AAPL', 'MSFT', 'NVDA', 'GOOG', 'META', 'AMZN', 'NFLX', 'ORCL', 'IBM'))

    
    st.write('')
    amount = st.number_input("Amount to invest in the stock")

    if st.button('Add to Portfolio'):
        if ticker == '' or amount <= 0:
            st.error("Please fill in empty fields", icon = '❌')


        st.session_state['portfolio'].append({"ticker": ticker, "amount": amount})
        df1 = pd.DataFrame(st.session_state['portfolio'])
        fig1 = px.pie(df1, 
                      values='amount', 
                      names='ticker', 
                      title = 'Portfolio Percent Breakdown',
        )
        col1.plotly_chart(fig1)

        ratio = yf.Ticker(ticker)
        st.session_state['pe_score'].append({"ticker": ticker, "pe score": ratio.info['forwardPE']})
        df2 = pd.DataFrame(st.session_state['pe_score'])
        
        fig2 = px.bar(df2, 
                      x='ticker', 
                      y="pe score", 
                      color="ticker", 
                      text_auto=True)
        
        st.write("df2 debug:", df2)

        with col1:
            st.plotly_chart(fig2)

  