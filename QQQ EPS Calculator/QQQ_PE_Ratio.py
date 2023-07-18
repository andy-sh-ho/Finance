import pandas as pd
import yfinance as yf

qqqHolding = pd.read_csv("https://www.invesco.com/us/financial-products/etfs/holdings/main/holdings/0?audienceType=Investor&action=download&ticker=QQQ")
qqqHolding['Date'] = pd.to_datetime(qqqHolding['Date']) # convert to datetime
qqqHolding.set_index('Date', inplace=True) # set the index; inplace bool, default False Whether to modify the DataFrame rather than creating a new one.

def get_trailing_eps(symbol):
    symbol = symbol.strip()
    stock = yf.Ticker(symbol)
    try:
        eps = stock.info['trailingEps'] # try to get the trailing EPS from the info dictionary
    except Exception as e: # catch any exception that may occur
        print(f"{symbol}: {e}") # print the symbol and the error
        eps = None # assign None as the EPS value
    return eps

qqqHolding['EPS'] = qqqHolding['Holding Ticker'].apply(get_trailing_eps) # apply the function to get the trailing EPS for each symbol

qqqHolding['EPS'] = pd.to_numeric(qqqHolding['EPS']) # convert the EPS column to a numeric type

qqqHolding['Earning'] = qqqHolding['Shares/Par Value'].str.replace(',', '', regex=True).astype(float) * qqqHolding['EPS'].astype(float)

Earning_QQQ = qqqHolding['Earning'].sum()
MarketCap_QQQ = qqqHolding['MarketValue'].str.replace(',', '', regex=True).astype(float).sum()

print("QQQ PE based on trailing EPS:", MarketCap_QQQ / Earning_QQQ)

print(qqqHolding)