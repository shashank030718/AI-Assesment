import yfinance as yf

def get_price_change(ticker: str):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="5d")
    if len(hist) >= 2:
        change = ((hist['Close'].iloc[-1] - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2]) * 100
    else:
        change = 0
    return {
        "ticker": ticker,
        "price": round(hist['Close'].iloc[-1], 2) if not hist.empty else None,
        "change_pct": round(change, 2)
    }
