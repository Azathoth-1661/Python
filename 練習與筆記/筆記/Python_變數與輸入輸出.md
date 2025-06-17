
# 🧠 Python 基礎語法｜變數與輸入輸出

## 🎯 學習目標：
- 學會使用 `print()` 輸出文字
- 使用 `input()` 接收使用者輸入
- 變數命名與基本型別：整數、浮點數、字串、布林值
- 學會使用 `type()`、`str()`、`int()`、`float()` 等轉換函式
- 學會字串格式化（f-string）

---

## 📘 語法重點整理

### 🔹 輸出與輸入
```python
print("Hello, Python!")
name = input("請輸入你的名字：")
print("你好，" + name)
```

### 🔹 變數與型別
```python
age = 25          # 整數 int
height = 165.5    # 浮點數 float
is_student = True # 布林值 bool
name = "Amy"      # 字串 str
```

### 🔹 型別轉換
```python
num = int("3")
pi = float("3.14")
text = str(100)
```

### 🔹 f-string 範例
```python
name = "Leo"
age = 30
print(f"{name} 明年 {age+1} 歲")
```

---

## ✅ 小挑戰練習

### 🔹 請寫一個互動式程式，接收名字與年齡，並輸出歡迎訊息
```python
name = input("請輸入你的名字：")
age = input("請輸入你的年齡：")
print(f"歡迎你，{name}，你今年 {age} 歲！")
```

### 🔹 BMI 計算挑戰
```python
height = float(input("請輸入身高（公尺）："))
weight = float(input("請輸入體重（公斤）："))
bmi = weight / (height ** 2)
print(f"你的 BMI 是 {bmi:.2f}")
```

---

## 📝 今日筆記區
### ✏️ 我今天學到了：
- 變數如何儲存資料與命名方式
- 如何讓使用者輸入資料
- 如何控制輸出與轉換資料型別

### 🔍 覺得最困難的部分是：
- 型別轉換時機與錯誤訊息處理

### 💡 明天想多加強：
- if 條件判斷邏輯
- 多條件選擇與巢狀判斷
