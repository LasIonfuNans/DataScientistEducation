# %%
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random

%matplotlib inline

# %%
#散布図
random.seed(0)

x = np.random.random(30)
y = np.sin(x) + np.random.random(30)

plt.figure(figsize=(10,3))

#plt.plot(x,y,'o')
plt.scatter(x,y)

plt.title("Title Name")
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

#%%
#曲線
random.seed(0)

np_data_x = np.arange(1000)
np_data_y = np.random.randn(1000).cumsum()

plt.figure(figsize=(10,3))

plt.plot(np_data_x,np_data_y,label='Label')
plt.legend()

plt.title("Title Name")
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

#%%
#グラフの分割
plt.figure(figsize=(10, 3))

plt.subplot(2, 1, 1)
x = np.linspace(-10, 10, 100)
plt.plot(x, np.sin(x))

plt.subplot(2, 1, 2)
y = np.linspace(-10, 10, 100)
plt.plot(y, np.sin(2*y))

#%%
#関数グラフの描画
def my_function(x):
    return x**2 + 2*x + x + 1

x = np.linspace(-10, 10)
plt.figure(figsize=(10,3))
plt.plot(x, my_function(x))
plt.grid(True)

#%%
#ヒストグラムの描画
random.seed(0)
plt.figure(figsize=(10,3))
plt.hist(np.random.randn(10 ** 5) * 10 + 50, bins = 60, range = (20, 80))
plt.grid(True)

#%%
#Practice2-10
x = np.linspace(-10,10)
plt.figure(figsize=(10,3))
plt.plot(x, 5 * x + 3)
plt.grid(True)

#%%
#Practice2-11
x = np.linspace(-10,10)
plt.figure(figsize=(10,3))
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.grid(True)

#%%
#Practice2-12
data_size = 1000000
x = np.random.uniform(0.0, 1.0, data_size)
y = np.random.uniform(0.0, 1.0, data_size)
k = int(np.log2(data_size) + 1)

plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.hist(x, bins = k)
plt.grid(True)

plt.subplot(2, 1, 2)
plt.hist(y, bins = k)
plt.grid(True)
