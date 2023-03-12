import pandas as pd
from datetime import datetime, timedelta

def get_weekly_closing_prices(csv_file):
    df = pd.read_csv(csv_file, parse_dates=['date'])
    df.set_index('date', inplace=True)
    weekly_closing_prices = []
    
    for week_end in pd.date_range(start=df.index.min(), end=df.index.max(), freq='W-FRI'):
        # get the prices for the current week
        mask = (df.index >= week_end - timedelta(days=6)) & (df.index <= week_end)
        week_prices = df.loc[mask]['close'].tolist()
        
        # append to the list of weekly prices
        weekly_closing_prices.append((week_end, week_prices))
        
    return weekly_closing_prices
