# range() 函數
* range(101)：產生0~100範圍的整數，101無法產生
* range(1, 101)：產生1到100範圍的整數
* range(1, 101, 2)：產生1~100間的奇數，參數 2 為間隔
* range(100, 0, -2)：產生100~1間的偶數，參數 -2 為間隔

* break 語句	==> 在語句執行過程中終止迴圈，並且跳出整個迴圈
* continue 語句	==> 在語句塊執行過程中終止當前迴圈，跳出該次迴圈，執行下一次迴圈。
* pass 語句	==> pass是空語句，是為了保持程序結構的完整性。

# for-in 循環
* 使用在明確知道循環次數的情況下

1. 使用for-in 循環求1~100的總和
```py
sum = 0
for x in range(101):
    sum += x
print(sum)
```
2. 使用for-in 循環求1~100間偶數總和
```py
sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)
```
# while 循環
* 使用於無法確定循環次數的情況下

1. 猜數字
```py
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('輸入數字: '))
    if number < answer:
        print('太小了')
    elif number > answer:
        print('太大了')
    else:
        print('猜對了')
        break
print('總共猜了%d次' % counter)
```
2. 九九乘法表
```py
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
```
3. 判斷是否為質數
* `質數`為只能被1與自身整除的數字
```py
from math import sqrt

num = int(input('輸入一個正整數: '))
end = int(sqrt(num)) #平方根
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是質數' % num)
else:
    print('%d不是質數' % num)
```
4. 最大公約數與最小公倍數
```py
x = int(input('x = '))
y = int(input('y = '))

if x > y: #x大於y 則交換兩者的值
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公約數是%d' % (x, y, factor))
        print('%d和%d的最小公倍數是%d' % (x, y, x * y // factor))
        break
```
