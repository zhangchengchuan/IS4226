import numpy as np
import pandas as pd
import yfinance as yf

def BASS(stock, benchmark, start, end):
    # Risk free
    risk_free = 0


    # Get historical data
    df = pd.DataFrame()
    df['stock'] = yf.Ticker(stock).history(start=start, end=end).Close
    df.index = df.index.tz_localize(None)
    
    df2 = pd.DataFrame()
    df2['benchmark'] = yf.Ticker(benchmark).history(start=start, end=end).Close
    df2.index = df2.index.tz_localize(None)
    df2.dropna()

    df['stock_returns'] = df['stock'].pct_change()
    df['benchmark_returns'] = df2['benchmark'].pct_change()
    df = df.dropna()
    
    # Beta
    cov = df['benchmark_returns'].cov(df['stock_returns'])
    var = df['benchmark_returns'].var()
    beta = cov/var
    beta = round(beta, 2)
  
    # Alpha
    benchmark_yearly_returns = (df['benchmark_returns'].mean())*252
    stock_yearly_returns = (df['stock_returns'].mean())*252
    # print(benchmark_yearly_returns, stock_yearly_returns)
    alpha = (stock_yearly_returns - risk_free - beta * (benchmark_yearly_returns - risk_free)) * 100
    alpha = round(alpha, 2)

    # Std_dev
    std_dev = (df['stock_returns'].std()) * 100
    std_dev = round(std_dev, 2)

    # Sharpe
    avg_returns = df['stock_returns'].mean()
    std = df['stock_returns'].std()
    daily_SR = (avg_returns - risk_free ) / std
    annual_SR = daily_SR * np.sqrt(252)
    annual_SR = round(annual_SR, 2)

    print("Beta: ", beta)
    print("Alpha: ", alpha)
    print("Sharpe: ",annual_SR)

start_date = "2022-01-01"
end_date = "2022-12-31"
answer = BASS("AAPL", "^STI", start_date, end_date)