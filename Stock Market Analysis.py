import yfinance as yf
from pathlib import Path
import matplotlib.pyplot as plt

# Download stock data
data = yf.download("AAPL", start="2020-01-01", end="2026-01-01")
print(data.head())

# Save data
project_folder = Path(__file__).parent
data_folder = project_folder / "data"
data_folder.mkdir(exist_ok=True)
data.to_csv(data_folder / "AAPL_stock_data.csv")

#daily return
daily_return= data["Close"]["AAPL"].pct_change()
print(daily_return.head())

#average daily return
average_return= daily_return.mean()
print("average daily return :",average_return )

#Daily volatility
daily_volatility=daily_return.std()
print("volatility:", daily_volatility)

# Moving Average close price
ma_20 = data["Close"]["AAPL"].rolling(window=20).mean()
ma_50 = data["Close"]["AAPL"].rolling(window=50).mean()
ma_200 = data["Close"]["AAPL"].rolling(window=200).mean()

# Plot close price
plt.figure(figsize=(10, 6))
plt.plot(data["Close"]["AAPL"])
plt.title("AAPL Closing Price")
plt.xlabel("Date")
plt.ylabel("Closing Price")

# Histogram Daily Return
plt.figure(figsize=(10,6))
plt.hist(daily_return.dropna(), bins=50)
plt.title("Distribution of AAPL Daily Returns")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")

# Plot Moving Average
plt.figure(figsize=(10,6))
plt.plot(data["Close"]["AAPL"], label="AAPL Closing Price")
plt.plot(ma_20, label="20-Day Moving Average")
plt.plot(ma_50, label="50-Day Moving Average")
plt.plot(ma_200, label="200-Day Moving Average")

plt.title("AAPL Closing Price and Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()

plt.show()