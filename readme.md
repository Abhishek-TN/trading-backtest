# Trading Strategy Backtesting

This project implements a backtesting logic for a trading strategy using historical data. The strategy applies Bollinger Bands to make buy/sell decisions, and the backtest results are visualized through a web application.

## Table of Contents
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Steps to Run the Code](#steps-to-run-the-code)
- [Backtesting Logic](#backtesting-logic)
- [Visualization](#visualization)
- [License](#license)

## Project Overview
This project implements a trading strategy backtesting system that utilizes Bollinger Bands to make trading decisions. The system processes historical price data, applies the strategy, and then visualizes the results.

## Prerequisites
Before running the project, ensure you have the following installed on your machine:
- Python 3.8 or higher
- Required Python libraries (listed below)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/trading-backtest.git
    cd trading-backtest
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows
    ```

3. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` file includes the following libraries:
    - pandas
    - numpy
    - matplotlib
    - dash
    - plotly
    - requests (for data ingestion)

## Steps to Run the Code

1. **Fetch Historical Data**: First, you need to fetch the historical data that will be used in the backtest. Run the following script to download the required data:
    ```bash
    python fetch_data.py
    ```
    This script will fetch the historical price data (e.g., stock or crypto data) and save it into the `data/` directory in CSV format.

2. **Run the Backtest**: Once the data is fetched, you can proceed with running the backtest:
    ```bash
    python backtest.py
    ```
    This will:
    - Process the historical data.
    - Apply the Bollinger Bands strategy.
    - Perform the backtest.
    - Save the results to a file or database.

3. **Visualize the Results**: After the backtest is complete, you can visualize the results in a web application. Run the following command:
    ```bash
    python app.py
    ```
    This will launch a local web server where you can see the backtest results:
    - Open your browser and navigate to `http://127.0.0.1:8050/` to view the visualization.

## Backtesting Logic
The backtesting logic uses the Bollinger Bands strategy:
- **Buy Signal**: When the price crosses below the lower Bollinger Band.
- **Sell Signal**: When the price crosses above the upper Bollinger Band.

The backtesting script calculates metrics like:
- Total profit/loss
- Maximum profit
- Minimum profit
- Number of trades

## Visualization
Once the backtest is complete, the results are visualized using Dash, a web framework. The visualization includes:
- A plot showing the price and Bollinger Bands.
- A table of performance statistics, such as total profit, maximum profit, and number of trades.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
