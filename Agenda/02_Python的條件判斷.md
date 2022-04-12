# Python 的條件語句

* 是通過一條或多條語句的執行結果（True或者False）來決定執行的代碼塊
* Python 指定任何非0和非空（null）值為true，0 或者 null為false。
* Python 程式設計中 if 語句用於控制程式的執行，基本形式為：
  ```
  if 判斷條件：
     執行語句
  else：
     執行語句
  ```
### if丶elif丶else 練習

1. 簡單的輸入判斷
```py
username = input('帳號: ')
password = input('密碼: ')
if username == 'admin' and password == '123456':
    print('帳號驗證成功')
else:
    print('帳號驗證失敗')
```
2. 公分與英寸的轉換
```py
value = float(input('長度: '))
unit = input('單位: ')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f公分' % (value, value * 2.54))
elif unit == 'cm' or unit == '公分':
    print('%f公分 = %f英寸' % (value, value / 2.54))
else:
    print('單位錯誤')
```
3. 百分制成績轉換為等級制
```py
score = float(input('成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('等級是:', grade)
```
 
