# range() 函數
* range(101)：產生0~100範圍的整數，101無法產生
* range(1, 101)：產生1到100範圍的整數
* range(1, 101, 2)：產生1~100間的奇數，參數 2 為間隔
* range(100, 0, -2)：產生100~1間的偶數，參數 -2 為間隔

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
