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

#線形代数用のライブラリ
import scipy.linalg as linalg

#最適化計算（最小値）用の関数
from scipy.optimize import minimize_scalar

#%%
#Practice2-7
from pandas import Series, DataFrame
import pandas as pd

attri_data1 = {'ID':['1','2','3','4','5'],
                'Sex':['F','F','M','M','F'],
                'Money':[1000,2000,500,300,700],
                'Name':['Saito','Horie','Kondo','Kawada','Matsubara']}

attri_data_frame1 = DataFrame(attri_data1)

print(attri_data_frame1[attri_data_frame1['Money'] >= 500])

#%%
#Practice2-8
attri_data_frame1.groupby('Sex')['Money'].sum()

#%%
#Practice2-9
attri_data2 = {'ID':['3','4','7'],
                'Math':[60,30,40],
                'English':[80,20,30]}

attri_data_frame2 = DataFrame(attri_data2)

#%%
attri_data_frame3 = pd.merge(attri_data_frame1,attri_data_frame2)

#%%
print(attri_data_frame3['Money'].mean())
print(attri_data_frame3['Math'].mean())
print(attri_data_frame3['English'].mean())