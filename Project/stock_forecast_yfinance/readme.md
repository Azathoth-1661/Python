# 台灣科技股預測分析專案（stock_forecast_yfinance）

本專案以台灣科技股為分析對象，透過 yfinance 抓取歷史股價資料，結合技術指標與 Prophet 時間序列模型，進行未來股價趨勢預測。

---

## 專案目標

- 建立可重複使用的股價預測流程  
- 整合技術指標模組（SMA、EMA、MACD）  
- 使用 Prophet 模型進行未來股價預測  
- 視覺化預測結果並計算誤差指標（RMSE、MAPE）

---

## 使用技術

- Python / yfinance / pandas / matplotlib  
- 技術指標計算（SMA、EMA、MACD）  
- 時間序列預測（Prophet）  
- 誤差指標分析（RMSE、MAPE）

---

## 專案結構
data # 原始資料或下載腳本

modules # 技術指標模組

forecast # 預測結果與圖表

reports #分析報告

README.md # 專案說明

colab_notebook.ipynb # 執行筆記本

---

## 圖表解讀與觀察

- `forecast_plot.png` 顯示 Prophet 模型成功捕捉股價趨勢與轉折點  
- `error_metrics.txt` 彙整誤差指標，顯示模型預測準確度穩定（MAPE 約 12.8%）  
- 技術指標如 MACD、SMA 可輔助判斷買賣時機，已整合進模組

---

## 分析報告與筆記本

- [分析報告（analysis_report.md）](reports/analysis_report.md)  
- [Colab 筆記本](colab_notebook.ipynb)
