# Python

* [官方網站](https://www.python.org/)

# Agenda

* [基本概念與功能](#1)
* [套件](#2)
* [基礎語法](#3)

<h2 id="1">基本概念與功能</h2>

1. Python 是一種易學、功能強大的程式語言
2. 它有高效能的高階資料結構，也有簡單但有效的方法去實現物件導向程式設計
3. Python優雅的語法和動態型別，結合其直譯特性，使它成為眾多領域和大多數平臺上，撰寫腳本和快速開發應用程式的理想語言。

<h2 id="2">套件</h2>

* [numpy](https://github.com/Azathoth-1661/Python/blob/main/numpy.md)

<h2 id="3">基礎語法</h2>

python可以同一行顯示多個語句，使用;分開
語句中包含[],{}等括號 則不需要使用連接符號 \
```py
print('hello');print('hello1');
total = "A" + \
        "B" + \
        "C"
print(total)
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)
x ='a'
y ='b'
#默認換行輸出
print(x)
print(y)
#不換行輸出
print(x,y)
```
結果
```
hello
hello1
ABC
['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
a
b
a b
```

python不使用{}(大括號)，取而代之使用縮排來取代大括號，因此對於縮排非常重要
```py
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
  print ("False")
```
結果
```
 File "<ipython-input-18-673371a84948>", line 6
    print ("False")
                   ^
IndentationError: unindent does not match any outer indentation level
```
正確寫法
```py
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    print ("False")
```
結果
```
Answer
True
```

