# 🧠 Python 基礎語法 Day 1｜變數、資料型態、輸入輸出與條件邏輯

## 🎯 學習目標：

- 宣告變數並儲存各種資料型態（整數、浮點數、字串、布林值）
- 使用 `input()`、`print()` 和 `type()`
- 熟悉 Python 的輸入輸出與基本運算邏輯
- 基礎條件判斷與錯誤處理結構

---

## 📘 重點語法整理

### 🔹 變數與資料型態

```python
# 整數 int
age = 25

# 浮點數 float
height = 170.5

# 字串 str
name = "宗彥"

# 布林值 bool
is_tired = False

# 顯示資料型態
print(type(age))        # <class 'int'>
print(type(name))       # <class 'str'>
```

### 🔹 使用者輸入與輸出

```python
# 使用 input() 輸入資料（回傳為字串）
user_input = input("請輸入年齡：")
print("你輸入的是：" + user_input)
```

---

## 🧪 練習題

### 🔹 練習 1：基本變數與輸出

```python
# 建立三個變數：姓名、年齡、身高
# 並用 print() 印出一段介紹自己的話
# 範例輸出：嗨，我叫小明，今年25歲，身高170.5公分。

name = "宗彥"
age = 24
height = 175.5
print(f"大家好，我叫{name}，今年{age}歲，身高{height:.1f}公分")
```

### 🔹 練習 2：資料型態轉換與加總

```python
try:
    int_1 = int(input("請輸入第一個數字："))
    int_2 = int(input("請輸入第二個數字："))
    int_total = int_1 + int_2
    print(f"兩數加總為：{int_total}")
except ValueError:
    print("請輸入有效的整數！")
```

### 🔹 練習 3：簡單數學運算（圓面積與周長）

```python
radius = float(input("請輸入圓的半徑："))
perimeter = 2 * 3.14159 * radius
area = 3.14159 * radius * radius
print(f"圓周長為：{perimeter:.1f}")
print(f"圓面積為：{area:.1f}")
```

---

## 📌 額外挑戰：判斷奇數或偶數

```python
try:
    int_1 = int(input("請輸入整數："))
    if int_1 % 2 == 0:
        print("是偶數")
    else:
        print("是奇數")
except ValueError:
    print("請輸入有效的整數！")
```

---

## 📝 今日筆記區（可自由填寫）

### 📌 來自 Jupyter Notebook 的補充程式碼整理：

以下為補充練習與示範程式，涵蓋資料型態的基本操作、型別轉換與各進位表示方式。


```python
# 顯示 Python 版本
!python -V
import math

# 建立不同資料型態的變數
int_1 = 15
float_1 = 1.14159
str_1 = "你好"
bool_1 = True
print(int_1)
print(float_1)
print(str_1)
print(bool_1)

# 整數的進位表示法示範
print(0b100)  # 二進位
print(0o100)  # 八進位
print(100)    # 十進位
print(0x100)  # 十六進位
print(123.456)  # 一般浮點數
print(1.23456e2)  # 科學記號

a = 8
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # 除法結果為浮點數

# 資料型別顯示
print(type(int_1))
print(type(float_1))
print(type(str_1))
print(type(bool_1))  # 再次顯示型態驗證  # 顯示 bool_1 的資料型態

# 類型轉換練習：數字轉整數與浮點數
x = int(10)
y = int(5.5)
z = int(3)
print(x, type(x))
print(y, type(y))
print(z, type(z))

x = float(10)
y = float(5.5)
z = float(3)
w = float("3.14")
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(w, type(w))

# 字串轉換練習
x = str("10")
y = str("5.5")
z = str("3")
print(x, type(x))
print(y, type(y))
print(z, type(z))

a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
print(int(c, base=16))  # 將 '123' 當作十六進位數轉為十進位整數（結果為 291）  # 將字串 '123' 當成 16 進位整數轉換
```


### 📌 今日練習使用過的完整程式碼：

```python
# 練習 1：介紹自己
name = "宗彥"
age = 24
height = 175.5
print(f"大家好，我叫{name}，今年{age}歲，身高{height:.1f}公分")

# 練習 2：整數加總
try:
    int_1 = int(input("請輸入第一個數字："))
    int_2 = int(input("請輸入第二個數字："))
    int_total = int_1 + int_2
    print(f"兩數加總為：{int_total}")
except ValueError:
    print("請輸入有效的整數！")

# 練習 3：圓周長與圓面積
radius = float(input("請輸入圓的半徑："))
perimeter = 2 * 3.14159 * radius
area = 3.14159 * radius * radius
print(f"圓周長為：{perimeter:.1f}")
print(f"圓面積為：{area:.1f}")

# 額外挑戰：判斷奇數或偶數
try:
    int_1 = int(input("請輸入整數："))
    if int_1 % 2 == 0:
        print("是偶數")
    else:
        print("是奇數")
except ValueError:
    print("請輸入有效的整數！")
```


### ✏️ 我今天學到了：

- try/except 防呆
- f-string使用方式
-

### 🔍 覺得最困難的部分是：

-

### 💡 明天想多加強：

-

---

✅ 明日預告：條件判斷 if / elif / else，進階邏輯運算與比較運算子應用

