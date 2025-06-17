# 🧠 Python 基礎語法｜條件判斷與邏輯運算

## 🎯 學習目標
- 學會使用 if / elif / else 進行條件判斷
- 熟悉邏輯運算子：and、or、not
- 能根據不同條件執行對應程式區塊
- 實作基本的輸入判斷與流程控制

---

## 📘 重點語法整理

### 比較運算子（用於條件判斷）
| 運算子 | 說明     | 範例       |
|--------|----------|------------|
| ==     | 等於     | a == b     |
| !=     | 不等於   | a != b     |
| >      | 大於     | a > b      |
| <      | 小於     | a < b      |
| >=     | 大於等於 | a >= b     |
| <=     | 小於等於 | a <= b     |

### 邏輯運算子（用於複合條件）
| 運算子 | 說明             | 範例                  |
|--------|------------------|-----------------------|
| and    | 且，兩者皆為真   | a > 0 and b < 10      |
| or     | 或，任一為真     | a > 0 or b < 10       |
| not    | 反向布林值       | not (a > 0)           |

---

## 🧪 練習題與挑戰題

### 練習 1：簡單成績判斷

輸入一個成績（整數），若成績 ≥ 60，印出「及格」，否則印出「不及格」。

提示：使用 if / else 條件判斷。

---

### 練習 2：分級成績顯示

請使用者輸入一個成績，並依照下列區間顯示等級：

- 90 分以上：A
- 80~89 分：B
- 70~79 分：C
- 60~69 分：D
- 60 以下：F

提示：可用 if/elif/else 多重條件配合整數區間判斷。

---

### 練習 3：登入系統驗證

預設帳號為 admin，密碼為 1234，請使用者輸入帳號與密碼，並驗證是否正確。

輸出「登入成功」或「帳號或密碼錯誤」。

---

### 挑戰題：判斷是否為閏年

輸入一個年份，判斷是否為閏年。判斷條件如下：

- 可以被 4 整除且不能被 100 整除，或
- 可以被 400 整除

輸出：「是閏年」或「不是閏年」

---

## ✅ 程式碼練習紀錄

以下為當天實作的程式範例：

🔹 練習 1：簡單成績判斷

```python
score = input("請輸入你的成績：")
if score.isdigit():
    score = int(score)
    print("及格" if score >= 60 else "不及格")
else:
    print("請輸入整數")
```

🔹 練習 2：分級成績顯示

```python
score = input("請輸入你的成績：")
if score.isdigit():
    score = int(score)
    if 0 <= score <= 100:
        if score >= 90:
            print("A")
        elif score >= 80:
            print("B")
        elif score >= 70:
            print("C")
        elif score >= 60:
            print("D")
        else:
            print("F")
    else:
        print("請輸入 0~100 之間的數字")
else:
    print("請輸入整數")
```

🔹 練習 3：登入系統驗證

```python
username = input("請輸入帳號：")
password = input("請輸入密碼：")

if username == "admin" and password == "1234":
    print("登入成功")
else:
    print("帳號或密碼錯誤")
```

🔹 挑戰題：閏年判斷

```python
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

try:
    year = int(input("請輸入年份："))
    print("是閏年" if is_leap(year) else "不是閏年")
except ValueError:
    print("請輸入正確的年份")
```
