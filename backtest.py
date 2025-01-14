import pandas as pd
import numpy as np
import os


class Trade:
    def __init__(self, token, date_in, buy_price, date_out, sell_price):
        self.token = token
        self.date_in = date_in
        self.buy_price = buy_price
        self.date_out = date_out
        self.sell_price = sell_price
        self.profit_percentage = self.calculate_profit()

    def calculate_profit(self):
        return ((self.sell_price - self.buy_price) / self.buy_price) * 100

class Backtest:
    def __init__(self, data_dir, capital_per_trade=100):
        self.data_dir = data_dir
        self.capital_per_trade = capital_per_trade
        self.trades = []

    def calculate_bollinger_bands(self, df, window=20, multiplier=2):
        df["sma"] = df["close"].rolling(window=window).mean()
        df["std"] = df["close"].rolling(window=window).std()
        df["upper_band"] = df["sma"] + (df["std"] * multiplier)
        df["lower_band"] = df["sma"] - (df["std"] * multiplier)
        return df

    def run_strategy(self):
        for file in os.listdir(self.data_dir):
            token = file.replace(".csv", "")
            df = pd.read_csv(os.path.join(self.data_dir, file), index_col="timestamp", parse_dates=True)
            df = self.calculate_bollinger_bands(df)
            in_position = False
            buy_price = 0
            buy_date = None

            for i in range(len(df)):
                if not in_position and df["close"].iloc[i] < df["lower_band"].iloc[i] * 0.97:
                    # Buy condition
                    in_position = True
                    buy_price = df["close"].iloc[i]
                    buy_date = df.index[i]
                elif in_position and df["close"].iloc[i] >= df["upper_band"].iloc[i]:
                    # Sell condition
                    sell_price = df["close"].iloc[i]
                    sell_date = df.index[i]
                    self.trades.append(Trade(token, buy_date, buy_price, sell_date, sell_price))
                    in_position = False

            # End-of-period sell
            if in_position:
                sell_price = df["close"].iloc[-1]
                sell_date = df.index[-1]
                self.trades.append(Trade(token, buy_date, buy_price, sell_date, sell_price))

    def save_results(self, output_file):
        results = pd.DataFrame([{
            "token": trade.token,
            "date_in": trade.date_in,
            "buy_price": trade.buy_price,
            "date_out": trade.date_out,
            "sell_price": trade.sell_price,
            "profit_percentage": trade.profit_percentage
        } for trade in self.trades])
        results.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")

# Example Usage
backtest = Backtest("./data")
backtest.run_strategy()
backtest.save_results("results.csv")
