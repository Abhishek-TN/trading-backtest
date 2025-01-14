# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:04:03 2025

@author: Abhishek
"""

import requests
import pandas as pd
import os

class DataFetcher:
    def __init__(self, symbols, interval, start_date, output_dir):
        self.symbols = symbols
        self.interval = interval
        self.start_date = start_date
        self.output_dir = output_dir
        self.base_url = "https://api.binance.com/api/v3/klines"

    def fetch_data(self, symbol):
        print(f"Fetching data for {symbol}...")
        params = {
            "symbol": symbol.upper(),
            "interval": self.interval,
            "limit": 1000
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data, columns=[
                "timestamp", "open", "high", "low", "close", "volume",
                "close_time", "quote_asset_volume", "num_trades", "taker_buy_base",
                "taker_buy_quote", "ignore"
            ])
            df = df[["timestamp", "open", "high", "low", "close", "volume"]]
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
            df.set_index("timestamp", inplace=True)
            return df
        else:
            print(f"Failed to fetch data for {symbol}.")
            return None

    def save_data(self):
        os.makedirs(self.output_dir, exist_ok=True)
        for symbol in self.symbols:
            df = self.fetch_data(symbol)
            if df is not None:
                df.to_csv(os.path.join(self.output_dir, f"{symbol}.csv"))
        print("Data fetching complete!")

# Example Usage
symbols = [
    "BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "XRPUSDT", "SOLUSDT", "DOGEUSDT", "DOTUSDT", 
    "MATICUSDT", "LTCUSDT", "SHIBUSDT", "TRXUSDT", "AVAXUSDT", "UNIUSDT", "LINKUSDT", "XLMUSDT", 
    "ATOMUSDT", "ALGOUSDT", "FTMUSDT", "AXSUSDT", "SANDUSDT", "AAVEUSDT", "MANAUSDT", "NEARUSDT", 
    "EGLDUSDT", "VETUSDT", "FILUSDT", "GRTUSDT", "LUNAUSDT", "THETAUSDT", "KLAYUSDT", "EOSUSDT", 
    "ICPUSDT", "FTMUSDT", "ZILUSDT", "MKRUSDT", "COMPUSDT", "ENJUSDT", "CHZUSDT", "YFIUSDT", 
    "CRVUSDT", "SNXUSDT", "RUNEUSDT", "ONEUSDT", "XTZUSDT", "CAKEUSDT", "KAVAUSDT", "ANKRUSDT", 
    "ZRXUSDT", "BATUSDT"
]
  
fetcher = DataFetcher(symbols, "1d", "2023-01-01", "./data")
fetcher.save_data()
