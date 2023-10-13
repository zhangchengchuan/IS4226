from ta import add_all_ta_features
import yfinance as yf
import pandas as pd

def get_technicals(stock, start, end):
    df = pd.DataFrame()
    # print(yf.Ticker(stock).history(start=start, end=end).columns)
    df['open'] = yf.Ticker(stock).history(start=start, end=end).Open
    df['close'] = yf.Ticker(stock).history(start=start, end=end).Close
    df['high'] = yf.Ticker(stock).history(start=start, end=end).High
    df['low'] = yf.Ticker(stock).history(start=start, end=end).Low
    df['volume'] = yf.Ticker(stock).history(start=start, end=end).Volume
    df.index = df.index.tz_localize(None)

    df = add_all_ta_features(df,open='open', high='high', low='low',close='close', volume='volume')
    # RSI

    # ATR

    # SMA
    df['SMA10'] = df['close'].rolling(window=10).mean()
    df['SMA20'] = df['close'].rolling(window=20).mean()
    df['SMA50'] = df['close'].rolling(window=50).mean()
    print(df.columns)
    df.dropna()
    print(df[['volatility_atr', 'momentum_rsi', 'SMA20', 'SMA10', 'SMA50']])

start_date = "2022-01-01"
end_date = "2022-12-31"
get_technicals("AAPL", start=start_date, end=end_date)