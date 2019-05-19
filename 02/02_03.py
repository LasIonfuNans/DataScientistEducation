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
matrix = np.array([[1,-1,-1],[-1,1,-1],[-1,-1,1]])
print('行列式：',linalg.det(matrix))
print('逆行列：\n',linalg.inv(matrix))
eig_val, eig_vec = linalg.eig(matrix)
print('固有値：',eig_val)
print('固有ベクトル：\n',eig_vec)

#%%
import math
print(1/math.sqrt(3))

#%%
#関数の定義
def my_function(x):
    return (x**2+2*x+1)

#ニュートン法の読み込み
from scipy.optimize import newton

#計算の実行
print(newton(my_function,0))

#%%
#Practice2-4
A = np.array([[1,2,3],[1,3,2],[3,1,2]])
print(np.linalg.det(A))

#%%
#Practice2-5
print(np.linalg.inv(A))
print(np.linalg.eig(A))

#%%
#Practice2-6
def g(x):
    return (x**3+2*x+1)
print(newton(g,0))
