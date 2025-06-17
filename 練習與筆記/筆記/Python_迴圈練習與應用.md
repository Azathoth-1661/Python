
# 🔁 Python 迴圈基礎與應用練習

## 🎯 學習目標
- 熟悉 `for` 迴圈與 `range()` 的使用方法
- 理解 `while` 迴圈的基本結構與流程控制
- 實作 `break` 與 `continue` 控制流程
- 能撰寫簡單邏輯的迴圈練習題

---

## 🔹 for 迴圈與 range() 用法

### ➤ 輸出 0~9
```python
for i in range(10):
    print(i)
```

### ➤ 輸出 2~20（每次+2）
```python
for i in range(2, 21, 2):
    print(i)
```

### ➤ 倒數 10~1
```python
for i in range(10, 0, -1):
    print(i)
```

### ➤ 1~100 中 7 的倍數
```python
for i in range(1, 100):
    if i % 7 == 0:
        print(i)
```

---

## 🔹 while 迴圈基礎

### ➤ 倒數 5~1
```python
i = 5
while i > 0:
    print(i)
    i -= 1
```

### ➤ while True 基本密碼驗證
```python
while True:
    password = input("請輸入密碼：")
    if password == "pass123":
        break
    else:
        print("請輸入正確的密碼")
```

### ➤ 進階密碼驗證（限 3 次）
```python
password = "pass123"
attempts = 3
while True:
    password_1 = input("請輸入密碼：")
    if password_1 == password:
        print("密碼正確，登入成功！")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"密碼錯誤，你還剩下 {attempts} 次機會")
        else:
            print("帳號鎖定，請聯絡管理員。")
            break
```

---

## 🔹 實作練習整理

### ✅ 加總 1~100
```python
i_number = 1
i_total = 0
while i_number < 101:
    i_total += i_number
    i_number += 1
print(f"總和為 {i_total}，加總到第 {i_number - 1} 個數字")
```

### ✅ 加總 1~100 偶數總和
```python
i_number = 1
i_total = 0
i_count = 0
while i_number < 101:
    if i_number % 2 == 0:
        i_total += i_number
        i_count += 1
    i_number += 1
print(f"總和為 {i_total}，加總了 {i_count} 個偶數")
```

### ✅ 倒扣挑戰（從 100 開始，每次減掉遞增的數字）
```python
score = 100
step = 1
while score > 0:
    score -= step
    step += 1
print(f"扣了 {step - 1} 次後變為負數")
```

---

## 📝 今日練習回顧

- 熟悉 `for` + `range()` 三參數形式的控制
- 熟悉 `while` 的流程與終止條件
- 實作 while True 密碼驗證邏輯（含錯誤次數）
- 練習變數控制與條件判斷的整合運用

---
