## 專案架構
### 主分析 Notebook（Colab）
Stock_Analysis_Multi_2024.ipynb  

### 台積電股價資料
2330.TW.csv                      

### 鴻海股價資料
2317.TW.csv  

### 聯發科股價資料
2454.TW.csv        

### 專案簡介

本專案為台灣三大科技股（台積電、鴻海、聯發科）在 2024 年的股價與成交量分析，透過 Google Colab 進行資料探索與視覺化，展示資料分析師的核心技能。

### 使用工具

Python（Pandas、Matplotlib、Seaborn）

Google Colab

技術指標：移動平均線（MA5、MA20）

### 資料來源

Yahoo Finance API

### 分析流程

資料收集與清理

EDA（探索性資料分析）

技術指標計算與視覺化

趨勢與波動觀察

結論撰寫

### 成果展示

股票走勢圖與成交量視覺化

MA 線分析圖

各股特性比較與洞察

### 如何使用

1.開啟 stock_analysis.ipynb

2.選擇 Google Colab 執行環境

3.依序執行各區塊程式碼

### 技術分析與預測模型補強

多支股票資料下載與視覺化

匯入套件與設定
```py
import yfinance as yf
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
```
```py
!wget -O TaipeiSansTCBeta-Regular.ttf https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download

sns.set(style="whitegrid")
matplotlib.font_manager.fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
matplotlib.rc('font', family='Taipei Sans TC Beta')
```
股票資料下載與儲存
```py
tickers = ["2330.TW", "2317.TW", "2454.TW"]

for ticker in tickers:
    df = yf.download(ticker, start="2024-01-01", end="2024-12-31")
    df.to_csv(f"{ticker}.csv")
```
資料載入與清理
```py
def load_stock_csv(file_path):
    df = pd.read_csv(file_path, header=2)
    df.rename(columns={
        "Date": "date",
        "Unnamed: 1": "close",
        "Unnamed: 2": "high",
        "Unnamed: 3": "low",
        "Unnamed: 4": "open",
        "Unnamed: 5": "volume",
        "Adj Close": "adj_close"
    }, inplace=True)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return df
```
```py
stock_data = {}
for ticker in tickers:
    stock_data[ticker] = load_stock_csv(f"{ticker}.csv")
```
資料檢查
```py
def check_data(df):
    print("=== 資料資訊 ===")
    print(df.info())
    print("
=== 敘述統計 ===")
    print(df.describe())
    print("
=== 缺值檢查 ===")
    print(df.isnull().sum())

for ticker, df in stock_data.items():
    print(f"
>>> 檢查股票: {ticker}")
    check_data(df)
```
收盤價走勢圖
```py
plt.figure(figsize=(12, 6))
for ticker, df in stock_data.items():
    plt.plot(df['date'], df['close'], label=ticker)
plt.title("多支股票收盤價走勢 (2024)")
plt.xlabel("日期")
plt.ylabel("收盤價")
plt.legend()
plt.show()
```
成交量條形圖
```py
plt.figure(figsize=(12, 6))
for ticker, df in stock_data.items():
    plt.bar(df['date'], df['volume'], alpha=0.5, label=ticker)
plt.title("多支股票成交量 (2024)")
plt.xlabel("日期")
plt.ylabel("成交量")
plt.legend()
plt.show()
```
收盤價分布圖
```py
plt.figure(figsize=(10, 5))
for ticker, df in stock_data.items():
    sns.histplot(df['close'], bins=30, kde=True, label=ticker, alpha=0.5)
plt.title("多支股票收盤價分布")
plt.xlabel("收盤價")
plt.ylabel("頻率")
plt.legend()
plt.show()
```
移動平均線分析
```py
for ticker, df in stock_data.items():
    df['MA5'] = df['close'].rolling(5).mean()
    df['MA20'] = df['close'].rolling(20).mean()
    plt.plot(df['date'], df['MA5'], linestyle='--', label=f"{ticker} MA5")
    plt.plot(df['date'], df['MA20'], linestyle=':', label=f"{ticker} MA20")
```
RSI 與 MACD 指標分析（防呆版本）
```py
# 下載資料
ts_mc = yf.download('2330.TW', start='2024-01-01', end='2024-08-31')

# 防呆處理：確保 Close 為 Series 且無缺值
close_series = pd.Series(ts_mc['Close'].values, index=ts_mc.index).fillna(method='ffill')

# RSI 計算
rsi_indicator = ta.momentum.RSIIndicator(close=close_series)
ts_mc['RSI'] = rsi_indicator.rsi()

# MACD 計算
macd_indicator = ta.trend.MACD(close=close_series)
ts_mc['MACD'] = macd_indicator.macd()
ts_mc['MACD_signal'] = macd_indicator.macd_signal()

# 繪圖
ts_mc[['Close', 'RSI', 'MACD', 'MACD_signal']].plot(figsize=(12,6))
plt.title('TSMC RSI & MACD')
plt.grid(True)
plt.show()
```

