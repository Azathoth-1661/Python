#  台灣科技股技術分析報告（stock_forecast_yfinance）

## 一、專案背景與目標

本專案以台灣科技股為分析對象，透過 yfinance 抓取歷史股價資料，結合技術指標計算流程與多股視覺化分析，探索股價趨勢與交易訊號。目標為建立可重複執行的分析架構，並輔助投資判斷。

---

## 二、資料來源與處理

- 使用 `yfinance` 套件擷取台灣科技股（如台積電、聯發科、鴻海）之歷史股價資料（收盤價、成交量等）  
- 資料期間涵蓋近一年，頻率為每日  
- 清理缺漏值並轉換為分析所需格式  
- 資料筆數約 250 筆，涵蓋 2024 年度交易日  

---

## 三、技術指標計算流程

- 計算 SMA（簡單移動平均）、EMA（指數移動平均）、MACD（移動平均收斂擴散指標）  
- 分析流程設計可套用於任意股價資料，具備良好擴充性  
- 技術指標可視覺化並輔助判斷買賣時機  
- MACD 金叉／死叉訊號與 SMA 趨勢線可交叉驗證股價走勢  
- 技術指標程式碼已整理為 `modules/` 資料夾，可獨立匯入使用：  
  - `sma.py`  
  - `ema.py`  
  - `macd.py`  

### 📦 技術指標匯入與使用範例

```python
from modules.sma import calculate_sma
from modules.ema import calculate_ema
from modules.macd import calculate_macd

df['SMA_20'] = calculate_sma(df['Close'], window=20)
df['EMA_20'] = calculate_ema(df['Close'], span=20)
macd_df = calculate_macd(df['Close'])
df = pd.concat([df, macd_df], axis=1)
```

---

## 四、探索性分析與視覺化成果

本專案亦進行多股資料的探索性分析與視覺化，包含收盤價分佈、走勢、成交量與均線交叉等，輔助理解各股特性與市場動態。

- 收盤價分佈圖
```python
plt.figure(figsize=(10, 5))
for ticker, df in stock_data.items():
    sns.histplot(df['close'], bins=30, kde=True, label=ticker, alpha=0.5)
plt.title("多支股票收盤價分佈")
plt.xlabel("收盤價")
plt.ylabel("頻率")
plt.legend()
plt.show()
```

- 收盤價走勢圖
```python
plt.figure(figsize=(12, 6))
for ticker, df in stock_data.items():
    plt.plot(df['date'], df['close'], label=ticker)
plt.title("多支股票收盤價走勢（2024）")
plt.xlabel("日期")
plt.ylabel("收盤價")
plt.legend()
plt.show()
```

- 成交量長條圖
```python
plt.figure(figsize=(12, 6))
for ticker, df in stock_data.items():
    plt.bar(df['date'], df['volume'], alpha=0.5, label=ticker)
plt.title("多支股票成交量（2024）")
plt.xlabel("日期")
plt.ylabel("成交量")
plt.legend()
plt.show()
```

- 均線交叉圖（MA5 / MA20）
```python
for ticker, df in stock_data.items():
    df["MA5"] = df["close"].rolling(5).mean()
    df["MA20"] = df["close"].rolling(20).mean()
    plt.plot(df["date"], df["MA5"], linestyle='--', label=f'{ticker} MA5')
    plt.plot(df["date"], df["MA20"], linestyle='-', label=f'{ticker} MA20')
plt.title("多支股票移動平均線分析")
plt.xlabel("日期")
plt.ylabel("股價")
plt.legend()
plt.show()
```
- RSI 與 MACD 指標圖（以台積電為例）
```python
plt.plot(df['date'], df['close'], label='Close, 2330.TW')
plt.plot(df['date'], df['RSI'], label='RSI, J')
plt.plot(df['date'], df['MACD'], label='MACD, J')
plt.plot(df['date'], df['MACD_signal'], label='MACD_signal, J')
plt.title("TSMC RSI & MACD")
plt.xlabel("日期")
plt.ylabel("指標值")
plt.legend()
plt.show()
```

---

## 五、forecast 資料夾內容補充

forecast 資料夾包含以下成果圖表

- sma_plot.png：SMA 技術指標圖，顯示短期與長期均線交叉情形

- macd_plot.png：MACD 技術指標圖，展示金叉／死叉訊號與趨勢變化

- rsi_macd_plot.png：RSI 與 MACD 指標圖，輔助判斷超買／超賣與趨勢反轉

- price_distribution.png：收盤價分佈圖，展示多股價格分佈與密度曲線

- price_trend.png：多股收盤價走勢圖，呈現年度股價變化

- volume_bar.png：多股成交量長條圖，觀察交易活躍度

- ma_cross.png：MA5 / MA20 均線交叉圖，輔助判斷短期與長期趨勢

## 六、結論與延伸應用

技術指標計算流程具備良好擴充性，適用於多股分析、自動化策略或回測系統

多股視覺化成果可輔助理解市場動態與個股特性

未來可整合 Streamlit 建立互動式儀表板，支援多股切換與即時更新

專案架構:

- data：三個使用的資料集

- modules：技術指標程式碼（sma.py、ema.py、macd.py）

- forecast：技術指標成果圖表

- report：分析報告

---

## 附件與連結

* [Colab](https://colab.research.google.com/drive/1D_E5-LHiF8N56ebqG5IYL2bQkjCicj6N)

---

##  本專案用途

本專案為個人資料分析作品集之一，已同步整理至履歷平台（104 / Cake ）
