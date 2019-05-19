#%%
import math

def prime_check(i):
    if i == 1:
        print(i)
    else:
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                print(i)
                return
        print(i,":Prime")

for k in range(1,50):
    prime_check(k)
