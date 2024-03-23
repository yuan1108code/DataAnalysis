# 載入 numpy 套件
import numpy as np

# 建立一維陣列
data = np.array([3, 2, 6, 4])
print(data)

# 創造四個資料未指定的一維陣列
data = np.empty(4)
print(data)
data = np.zeros(3)
print(data)
data = np.ones(3)
print(data)
data = np.arange(5)
print(data)

# 建立二維陣列
data = np.array([
    [2, 3, 2],
    [1, 5, 2],
    [4, 2, 1]
])
print(data)
data = np.empty([3, 3])
print(data)

# 建立三維陣列
data = np.array([ # 2x2x2 的三維陣列
    [
        [3, 1], [1, 2]  
    ],
    [
        [2, 5], [10, 2]
    ],
])
print(data)

# 建立高維陣列
data = np.array([ # 1x1x2x3 的四維陣列
    [
        [3, 2, 1],[5, 5, 10]
    ]
])
print(data)