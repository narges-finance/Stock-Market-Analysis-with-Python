# Stock Market Analysis with Python

This project analyzes historical stock market data using Python.
The analysis is performed on **Apple Inc. (AAPL)** stock using daily data obtained from Yahoo Finance.

## Project Overview

The main purpose of this project is to practice basic financial data analysis and Python programming.

The project includes:

* Downloading historical stock price data
* Calculating daily returns
* Calculating average daily return
* Measuring daily volatility
* Calculating moving averages
* Visualizing stock prices and returns

## Dataset

The historical data for **AAPL** is obtained using the `yfinance` library.

* **Ticker:** AAPL
* **Company:** Apple Inc.
* **Start Date:** January 1, 2020
* **End Date:** January 1, 2026
* **Frequency:** Daily

The downloaded data is saved as:

```text
data/AAPL_stock_data.csv
```

## Analysis

### 1. Daily Return

Daily return measures the percentage change in the closing price from one trading day to the next.

The project calculates daily returns using:

```python
daily_return = data["Close"]["AAPL"].pct_change()
```

### 2. Average Daily Return

The average daily return is calculated as the mean of all daily returns:

```python
average_return = daily_return.mean()
```

This provides a simple measure of the average daily price return over the analyzed period.

### 3. Daily Volatility

Daily volatility is measured using the standard deviation of daily returns:

```python
daily_volatility = daily_return.std()
```

A higher standard deviation indicates greater variation in daily returns during the analyzed period.

### 4. Moving Averages

The project calculates three moving averages:

* **20-Day Moving Average** – short-term trend
* **50-Day Moving Average** – medium-term trend
* **200-Day Moving Average** – long-term trend

They are calculated using:

```python
ma_20 = data["Close"]["AAPL"].rolling(window=20).mean()
ma_50 = data["Close"]["AAPL"].rolling(window=50).mean()
ma_200 = data["Close"]["AAPL"].rolling(window=200).mean()
```

## Visualizations

The project generates three main visualizations:

### AAPL Closing Price

Shows the historical closing price of AAPL over the analyzed period.

### Distribution of Daily Returns

A histogram is used to visualize the distribution of AAPL's daily returns.

### Moving Averages

The closing price is plotted together with the 20-day, 50-day, and 200-day moving averages to visualize different time horizons.

## Technologies and Libraries

The project is developed using Python and the following libraries:

* Python
* `yfinance`
* `matplotlib`
* `pathlib`

## Project Structure

```text
Stock-Market-Analysis-with-Python/
│
├── Stock Market Analysis.py
├── data/
│   └── AAPL_stock_data.csv
├── README.md
└── requirements.txt
```

## How to Run

Clone the repository and install the required libraries:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python "Stock Market Analysis.py"
```

The program downloads the historical AAPL data, performs the analysis, saves the dataset, and displays the visualizations.

## Purpose

This project is part of my learning journey in **Python, financial data analysis, and quantitative finance**.

It is intended as a practical introduction to working with financial market data using Python.
