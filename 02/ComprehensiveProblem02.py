#%%
import numpy as np
import math
import matplotlib.pyplot as plt
%matplotlib inline

#%%
data_size = 1000000
x = np.random.uniform(0.0, 1.0, data_size)
y = np.random.uniform(0.0, 1.0, data_size)

plt.figure(figsize=(5,5))

x_in_li = []
y_in_li = []
x_out_li = []
y_out_li = []

for i in range(data_size):
    dist = math.hypot(x[i], y[i])
    if dist < 1:
        x_in_li.append(x[i])
        y_in_li.append(y[i])
    else:
        x_out_li.append(x[i])
        y_out_li.append(y[i])

plt.scatter(x_in_li, y_in_li)
plt.scatter(x_out_li, y_out_li)

# plt.xlim(-1.5, 1.5)
# plt.ylim(-1.5, 1.5)
plt.grid(True)


#%%
calc_pi = (4 * len(x_in_li)) / data_size
print(calc_pi)
# print(len(x_in_li))
# print(len(y_in_li))
# print(len(x_out_li))
# print(len(y_out_li))
