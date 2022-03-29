- [下載excel檔案](https://github.com/PacktPublishing/Learning-Pandas-Second-Edition/blob/master/data/stocks.xlsx)
- 再upload到Google Colab
- xlsx vs xls 檔案差異
- 讀取excel [pandas.read_excel()](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
  - 熟悉各種讀取參數用法  
  - [(最新Pandas.read_excel()全参数详解（案例实操，如何利用python导入excel）)](https://zhuanlan.zhihu.com/p/142972462)
  - [[Pandas教學]5個實用的Pandas讀取Excel檔案資料技巧](https://www.learncodewithmike.com/2020/12/read-excel-file-using-pandas.html)
  - [Python pandas.ExcelWriter用法及代碼示例](https://vimsky.com/zh-tw/examples/usage/python-pandas.ExcelWriter.html)

- 寫入excel [pandas.DataFrame.to_excel()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html)
  - [Python pandas.DataFrame.to_excel用法及代碼示例](https://vimsky.com/zh-tw/examples/usage/python-pandas.DataFrame.to_excel.html)
```python
df = pd.read_excel("./stocks.xlsx")
df[:5]
```
![image](https://github.com/Azathoth-1661/Python/blob/main/pandas/20.png)
### 讀取不同試算表
```python
# read from the aapl worksheet
aapl = pd.read_excel("./stocks.xlsx", sheetname='aapl')
aapl[:5]
```

```python
# save to an .XLS file, in worksheet 'Sheet1'
df.to_excel("./stocks2.xls")
```


```python

```
