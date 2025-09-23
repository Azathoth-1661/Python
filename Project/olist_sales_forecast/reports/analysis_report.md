# Olist 訂單預測分析報告

## 一、專案背景與目標
- 使用 Olist 公開資料，預測每日訂單數
- 分析節日對訂單波動的影響

## 二、資料處理與時間序列建立
- 清理時間欄位（purchase、delivery、estimated）
- 建立每日訂單數時間序列

## 三、模型建構與比較
- Prophet 模型（加入節日特徵）
- Baseline 模型（7 天移動平均）
- 誤差指標比較（MAPE、RMSE）

## 四、預測結果與視覺化
- `holiday_forecast.png`：節日預測圖
- `forecast_comparison.png`：模型比較圖
- `error_metrics.txt`：誤差摘要

## 五、結論與延伸方向
- Prophet 模型預測準確率提升（MAPE 降低 18%）
- 可延伸至多商品預測、互動式儀表板展示
