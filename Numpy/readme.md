# numpy

## Agenda

* [官方網站](https://numpy.org/)
* [核心](#1)
* [常用function](#2)

<h2 id="1">核心</h2>

* ndarray（n-dimensional array，多維陣列）資料結構 ==> 表示多維度、同質並且固定大小的陣列物件

* ndarray的屬性
  * 軸(axis)  
    [參考筆記](http://changtw-blog.logdown.com/posts/895468-python-numpy-axis-concept-organize-notes)
  * 維度(dimension):ndim
    ```py
    ar2=np.array([[0,3,5],[2,8,7]]) # 產生一個 2D array
    ar2.ndim
    ```
    ```
    2
    ```
  * 秩rank 
  * 形狀(shape):shape
    ```py
    ar2=np.array([[0,3,5],[2,8,7]]) # 產生一個 2D array
    ar2.shape
    ```
    ```
    (2, 3)
    ```
  * dtype(資料型態:data type)
    ```py
    ar1=np.array([2,4,6,8])
    ar2=np.array([2,-1,6,3],dtype='float')
    ar3=np.array([2.,4,6,8])
    print(ar1.dtype)
    print(ar2.dtype)
    print(ar3.dtype)
    ```
    ```
    int64
    float64
    float64
    ```
  * 大小(元素個數):size
    ```py
    ar2=np.array([[0,3,5],[2,8,7]]) # 產生一個 2D array
    ar2.size
    ```
    ```
    6
    ```

<h2 id="2">常用function</h2>

* [numpy.linspace()](#3)
* [numpy.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)

<h2 id="3">numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)</h2>

* 必填參數
  * start : array_like
    序列的初始值
  * stop : array_like
    序列的結束值，除非endpoint參數為false，在這種情況下，序列由除最後一個等距樣本之外的所有樣本組成．
* 可選參數(不選擇時為預設值)
  * num : int  
    樣本數，預設為50
  * endpoint : bool  
    如果是true則包含最後一個項目，false則不包含最後一個項目 預設值為true
  * retstep : bool  
    如果為true，則返回(samples,step)
  * dtype : dtype  
    輸出陣列的類型，如果未給出dtype，則從開始和停止推斷數據類型，推斷的dtype永遠不會是整數，即使參數將生成整數陣列，也會選擇float
  * axis : int  
  　用於儲存樣本的軸  
* 回傳
  * samples : ndarray
    傳回等間距的樣本
  * step : float
    當endpoint為true時回傳，回傳sample的間距大小
```py
np.linspace(2.0, 3.0, num=5)
```
```
array([2.  , 2.25, 2.5 , 2.75, 3.  ])
```
```py
np.linspace(2.0, 3.0, num=5, endpoint=False)
```
```
array([2. , 2.2, 2.4, 2.6, 2.8])
```
```py
np.linspace(2.0, 3.0, num=5, retstep=True)
```
```
(array([2.  , 2.25, 2.5 , 2.75, 3.  ]), 0.25)
```

## numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)

* 創建一個陣列
