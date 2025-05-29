from yahoo_fin import stock_info

def get_earnings_surprise(ticker: str):
    try:
        earnings = stock_info.get_earnings(ticker)
        surprise = earnings["surprise_percent"][0]
        return round(surprise, 2)
    except Exception:
        return None
