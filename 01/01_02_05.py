#%%
#01_02_05_01

counter = 0

#再帰関数の例
def calc_fib(n):
    global counter
    counter += 1
    if n in [1,2]:
        return 1
    else:
        return calc_fib(n-1) + calc_fib(n-2)

print('フィボナッチ数：',calc_fib(25))
print(counter, "回の関数呼び出し")
# フィボナッチ数：75025
# 150049 回の関数呼び出し

from functools import lru_cache
counter = 0
@lru_cache(maxsize=1024)
def fib2(n):
    global counter
    counter += 1
    if n in [1, 2]:
        return 1
    return fib2(n - 1) + fib2(n - 2)

print('フィボナッチ数：',fib2(25))
print(counter, "回の関数呼び出し")
# フィボナッチ数：75025
# 25 回の関数呼び出し

#%%
#01_02_05_02

print((lambda a,b:a*b)(3,10))

def calc_double(x):
    return x**2

for num in [1,2,3,4]:
    print(calc_double(num))

print(list(map(calc_double,[1,2,3,4])))

print(list(map(lambda x:x**2,[1,2,3,4])))

#%%
#01_02_05_Practice_01_01

input_str = "data Science"

for str_index in range(len(input_str)):
    print(input_str[str_index])

#%%
#01_02_05_Practice_01_02
maxN = 55
def sumfromone(N):
    return int((N*(N+1))/2)
print(sumfromone(maxN))


