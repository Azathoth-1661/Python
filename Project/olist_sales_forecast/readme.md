# 📈 Olist 訂單預測分析專案

## 專案簡介

本專案以巴西電商平台 Olist 的公開資料為基礎，建立每日訂單數預測模型，並進行誤差分析與模型比較。目標為模擬資料分析師在實務中處理時間序列預測任務，並透過視覺化與模組化程式碼提升專案可讀性與延伸性。

---

## 使用資料集

- `olist_orders_dataset.csv`：訂單時間與狀態資料  
- `olist_order_payments_dataset.csv`：付款方式與金額資料  
- `olist_products_dataset.csv`：商品分類資料

---

## 分析流程

1. 資料清理與時間欄位處理  
2. 建立每日訂單數時間序列  
3. 合併付款方式與商品分類資料  
4. Prophet 模型訓練與預測  
5. 加入節日特徵提升預測準確度  
6. 與 baseline 模型（移動平均）進行誤差比較  
7. 成果視覺化與報告整理

---

## 模型比較結果

| 模型類型 | MAPE | RMSE |
|----------|------|------|
| Prophet（含節日特徵） | 12.3% | 18.7 |
| Baseline（7 天移動平均） | 19.5% | 24.2 |

---

## 成果視覺化

- 📊 Prophet 預測結果與實際值比較  
- 🎯 加入節日特徵後的預測變化  
- 🔍 Baseline 與 Prophet 模型誤差比較圖

---

## 模組化程式碼

- `prophet_model.py`：Prophet 模型訓練、預測與視覺化
  
prepare_data(df)：轉換資料格式為 Prophet 所需的 ds 與 y 欄位

train_prophet(df, holidays_df=None)：訓練 Prophet 模型，支援加入節日特徵

forecast_and_plot(model, periods=60)：預測未來資料並視覺化結果

- `baseline_model.py`：移動平均預測與誤差分析

rolling_baseline(df, window=7)：計算移動平均預測值

evaluate_baseline(df)：計算 MAPE 與 RMSE 誤差指標

plot_baseline(df)：視覺化 baseline 模型預測結果與實際值

- `utils.py`：資料處理與視覺化輔助函數

---

## 執行方式
直接在 Google Colab 上開啟並執行本專案分析流程：

👉 [點此開啟 Colab 筆記本](https://colab.research.google.com/drive/15R5-Rclv37FL0fqCvERk1CBlfxX78LJ9?hl=zh-tw)

在本機執行，請參考以下模組化程式碼與資料結構

```bash
pip install -r requirements.txt
python modules/prophet_model.py
```
