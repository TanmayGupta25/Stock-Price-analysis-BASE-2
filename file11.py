import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Create a Streamlit app
st.title("Stock Price Analysis")

# Create a dropdown menu for selecting a stock
stock_symbols = ["AAPL", "GOOG", "MSFT", "AMZN", "FB"]
selected_stock = st.selectbox("Select a stock", stock_symbols)

# Get the historical price data for the selected stock
stock_data = yf.download(selected_stock, start="2020-01-01", end="2022-12-31")

# Create a line chart of the stock's closing prices
fig, ax = plt.subplots()
ax.plot(stock_data.index, stock_data["Close"])
ax.set_title(f"{selected_stock} Closing Prices")
ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
st.pyplot(fig)

# Run the app
if __name__ == "__main__":
    st.write("Stock Price Analysis App")
    st.write("Select a stock from the dropdown menu to view its historical price data.")