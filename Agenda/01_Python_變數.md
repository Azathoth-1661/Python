# 變數與數據類型

* 變數是一種儲存數據的載體
* 計算機中的變數是記憶體中儲存數據的一塊記憶體空間，變數的值可以被讀取和修改，這是所有計算和控制的基礎
* 計算機能處理的數據類型有很多，以下為常見的 Python 支援的數據類型
* 可變數據
  * List（列表） ==> 序列中的每個值都有對應的位置值，稱之為索引，第一個索引是0，第二個索引是1，依此類推
  * Dictionary（字典） ==> 每一個元素都由鍵 (key) 和值 (value) 構成，結構為key: value 不同的元素之間會以逗號分隔，並且以大括號 {} 圍住
  * Set（集合） ==> 無序的不重複元素序列
  
* 不可變數據
  * Number（數字） ==> 包含int(整數)丶float(浮點數)丶bool(布林)丶complex(複數)並且支援二進位、八進位、十進位（）和十六進位的表示法
  * String（字符串）==> 用單引號 ' 或雙引號 " 括起來，同時使用反斜杠 \ 轉義特殊字元
  * Tuple（元组） ==> 元組與列表類似，不同之處在於元組的元素不能修改。元組使用小括弧 （ ），列表使用方括弧 []

### 變數命名規則
* 硬性規則
  * 變數名由字母（廣義的Unicode字元，不包括特殊字元）、數字和下劃線構成，數字不能為開頭。
  * 大小寫敏感（大寫的A和小寫a的是兩個不同的變數）。
  * 不要跟關鍵字（有特殊含義的單詞）和系統保留字（如函數、模組等的名字）衝突。
* [PEP8 要求](https://cflin.com/wordpress/603/pep8-python%E7%B7%A8%E7%A2%BC%E8%A6%8F%E7%AF%84%E6%89%8B%E5%86%8A)
  
### [運算子](https://www.runoob.com/python3/python3-basic-operators.html)
* 賦值運算子 ==> 賦值運算子的作用是將右邊的值賦給左邊的變數。

### 變數的使用與練習
* 開發環境 ==> [Google Colab](https://colab.research.google.com/?utm_source=scs-index)
* Version ==> Python 3.7.13
1. 加減乘除
```py
a = 321
b = 12
print(a + b)    
print(a - b)    
print(a * b)    
print(a / b)
```
2. 使用`type()`函數查詢變數的類型
```py
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))    
print(type(b))    
print(type(c))    
print(type(d))    
print(type(e)) 
```
3. 使用Python 內建函數進行數據類型轉換
* `int()`：將一個數值或字串轉換成整數，可以指定進位。
* `float()`：將一個字串轉換成浮點數。
* `str()`：將指定的物件轉換成字串形式，可以指定編碼。
* `chr()`：將整數轉換成該編碼對應的字串（一個字元）。
* `ord()`：將字串（一個字元）轉換成對應的編碼（整數）
```py
x = int(1)   
y = int(2.8) 
z = int("3") 
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
print("==========")
x = float(1)     
y = float(2.8)   
z = float("3")   
w = float("4.2") 
print(x)
print(y)
print(z)
print(w)
print(type(x))
print(type(y))
print(type(z))
print(type(w))
print("==========")
x = str("s1") 
y = str(2)    
z = str(3.0)  
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
```
4. 使用`input()`鍵盤輸入函數完成基礎運算
```py
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
```
5. 華氏溫度轉攝氏溫度
```py
f = float(input('華氏溫度: '))
c = (f - 32) / 1.8
print('%.1f華氏溫度 = %.1f攝氏溫度' % (f, c))
```
6. 使用圓的半徑計算周長與面積
```py
radius = float(input('圓的半徑: '))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周長: %.2f' % perimeter)
print('面積: %.2f' % area)
```
7. 判斷是否為閏年
```py
year = int(input('年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)
```
