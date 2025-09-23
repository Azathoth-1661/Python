# 📄 台灣科技股預測分析報告（stock_forecast_yfinance）

## 一、專案背景與目標

本專案以台灣科技股為分析對象，透過 yfinance 抓取歷史股價資料，結合技術指標與 Prophet 時間序列模型，進行未來股價趨勢預測。目標為建立可重複使用的預測流程，並輔助投資判斷。

---

## 二、資料來源與處理

* 使用 `yfinance` 套件擷取台灣科技股（如台積電、聯發科）之歷史股價資料（收盤價、成交量等）
* 資料期間涵蓋近一年，頻率為每日
* 清理缺漏值並轉換為 Prophet 所需格式（ds, y）
* 資料筆數約 250 筆，涵蓋 2024 年度交易日

---

## 三、技術指標模組

* 計算 SMA（簡單移動平均）、EMA（指數移動平均）、MACD（移動平均收斂擴散指標）
* 模組化設計，可套用於任意股價資料
* 技術指標可視覺化並輔助判斷買賣時機
* MACD 金叉／死叉訊號與 SMA 趨勢線可交叉驗證 Prophet 預測結果
* 模組程式碼已整理為 `modules/` 資料夾，可獨立匯入使用：
  * `sma.py`
  * `ema.py`
  * `macd.py`

---

## 四、預測模型與誤差分析

* 使用 Prophet 模型進行未來 30 天股價預測
* 模型設定包含：週期性、假日效應、`changepoint_prior_scale=0.5`
* 預測區間為 2025 年 1 月至 2 月，以 2024 年資料為訓練基礎
* 預測成果儲存於 `forecast/forecast_plot.png`
* 誤差指標如下，已彙整於 `forecast/error_metrics.txt`：

| 模型 | MAPE | RMSE |
|------|------|------|
| Prophet | 12.8% | 15.3 |

---

## 五、成果視覺化與解讀

* `forecast_plot.png` 顯示 Prophet 模型成功捕捉股價趨勢與轉折點
* 技術指標圖如 `macd_plot.png`、`sma_plot.png` 展示買賣訊號與趨勢線
* `error_metrics.txt` 彙整誤差指標，顯示模型穩定性佳
* 預測結果與技術指標可交叉驗證，提升判斷精度

---

## 六、結論與延伸應用

* Prophet 模型具備良好預測能力，適用於台股短期趨勢分析
* 技術指標模組可延伸至多股同時分析、自動化交易策略或回測系統
* 未來可整合 Streamlit 建立互動式儀表板，支援多股切換與即時更新
* 專案架構已補齊：
  * `data/`：三個使用的資料集
  * `modules/`：技術指標模組程式碼
  * `forecast/`：預測圖表與誤差指標
  * `report/`：分析報告

---

## 🔗 附件與連結

* [Colab](https://colab.research.google.com/drive/1D_E5-LHiF8N56ebqG5IYL2bQkjCicj6N)
