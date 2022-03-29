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



## numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)

* 創建一個陣列
