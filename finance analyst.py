import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Function to pull stock data and calculate indicators
def analyze_stock(ticker, start_date, end_date):
    # Download historical data
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    
    # Calculate moving averages
    stock_data['50_day_MA'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['200_day_MA'] = stock_data['Close'].rolling(window=200).mean()
    
    # Calculate daily returns and cumulative returns
    stock_data['Daily_Return'] = stock_data['Close'].pct_change()
    stock_data['Cumulative_Return'] = (1 + stock_data['Daily_Return']).cumprod()
    
    # Plot the stock's closing price and moving averages
    plt.figure(figsize=(14, 7))
    plt.plot(stock_data['Close'], label='Closing Price', color='blue')
    plt.plot(stock_data['50_day_MA'], label='50 Day MA', color='orange')
    plt.plot(stock_data['200_day_MA'], label='200 Day MA', color='green')
    plt.title(f'{ticker} Stock Analysis')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

    # Plot the cumulative returns
    plt.figure(figsize=(14, 7))
    plt.plot(stock_data['Cumulative_Return'], label='Cumulative Return', color='purple')
    plt.title(f'{ticker} Cumulative Returns')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.legend()
    plt.show()
    
    # Show summary statistics
    return stock_data.describe()

# Example usage
ticker = 'AAPL'  # You can replace with any stock ticker symbol
start_date = '2020-01-01'
end_date = '2023-01-01'
summary_stats = analyze_stock(ticker, start_date, end_date)

print("Summary Statistics:")
print(summary_stats)
