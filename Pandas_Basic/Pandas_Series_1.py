# Python Pandas Module Basic - Series 1
import numpy as np
import pandas as pd
from pandas.core import series
series_example = pd.Series([-0.5,0.75,1.0,-2])
print(series_example.index) # default index begins from 0
print(series_example)

numberList = [-0.5,0.75,1.0,-2]
series_example_2 = pd.Series(numberList,index=['a','b','c','d']) # list + index -> Series
ind = series_example_2.index

# get part of the Series
print(series_example_2['b'])
print(series_example_2[0:2])

# Series addition and fill the null value
series1 = pd.Series([25,10,50],index=[0,1,2])
series2 = pd.Series([5,70,40],index=[1,2,3])
series3 = series1 + series2
series3_good = series1.add(series2,fill_value=0)





