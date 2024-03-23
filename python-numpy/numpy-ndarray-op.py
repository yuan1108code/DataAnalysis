# 載入 numpy 套件
import numpy as np

# 逐元運算 (elementwise)
data1 = np.array([3, 2, 10])
data2 = np.array([1, 3, 6])
result = data1 @ data2
print(result)

result2 = data1 > data2
print(result2)

result3 = data1 == data2
print(result3)

# 矩陣運算 (matrix)
data1 = np.array([ # matrix 1 x 2
    [1, 3]
])
data2 = np.array([ # matrix 2 x 3
    [2, -1, 3],
    [-2, 4, 1]
])

result4 = data1.dot(data2)
print("data1 Dot data2")
print(result4)

result5 = np.outer(data1, data2)
print("data1 Outer data2")
print(result5)

# 統計運算 
# 陣列 = 多維陣列
data = np.array([
    [2, 1, 7],
    [-5, 3, 8]
])
result = data.sum()
print(result)

result = data.mean()
print(result)

result = data.std()
print(result)

result = data.sum(axis = 0) # 針對 column (第1個維度) 做加法
print(result)

result = data.max(axis = 0) # 針對 column (第1個維度) 找最大值
print(result)

result = data.cumsum()
print(result)