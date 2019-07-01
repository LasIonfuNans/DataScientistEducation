#%%
import numpy as np
import numpy.random as random
import scipy as sp
import pandas as pd
from pandas import Series,DataFrame

# 可視化ライブラリ
import matplotlib.pyplot as plt
import matplotlib as mlt
import seaborn
%matplotlib inline

# 小数第三位まで表示
%precision 3

#%%
data = np.array([9,2,3,4,10,6,7,8,1,5])
print(data)
print(data*3)
print(data**2)
print(data+data)
print(data/data)

#%%
#Practice 2-1
input_array = np.arange(50)
print(input_array.sum())

#%%
#Practice 2-2
random.seed(0)
rnd_data =random.randn(10)
print(rnd_data)
print(rnd_data.max())
print(rnd_data.min())
print(rnd_data.sum())

#%%
#Practice 2-3
input_array = np.ones((5,5),dtype = np.int64)*3
print(input_array**2)