import yfinance as yf
from datetime import datetime
from .models import OilPrice, StockMarket

def fetch_market_data():
    # Oil Price (Brent Crude)
    oil = yf.Ticker("BZ=F")
    oil_price = oil.history(period="1d")["Close"].iloc[-1]

    OilPrice.objects.create(
        price=oil_price,
        date=datetime.today()
    )

    # S&P 500
    sp500 = yf.Ticker("^GSPC")
    sp500_price = sp500.history(period="1d")["Close"].iloc[-1]

    StockMarket.objects.create(
        index_name="S&P 500",
        price=sp500_price,
        date=datetime.today()
    )

    # NASDAQ
    nasdaq = yf.Ticker("^IXIC")
    nasdaq_price = nasdaq.history(period="1d")["Close"].iloc[-1]

    StockMarket.objects.create(
        index_name="NASDAQ",
        price=nasdaq_price,
        date=datetime.today()
    )

    # NIFTY 50
    nifty = yf.Ticker("^NSEI")
    nifty_price = nifty.history(period="1d")["Close"].iloc[-1]

    StockMarket.objects.create(
        index_name="NIFTY 50",
        price=nifty_price,
        date=datetime.today()
    )

    print("Market data stored successfully")