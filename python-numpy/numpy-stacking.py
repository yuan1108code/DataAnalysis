import numpy as np
# 準備測試資料
arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
arr2 = np.array([
    [7, 8, 9],
    [10, 11, 12]
])
arr3 = np.array([
    [13, 14],
    [15, 16]
])

# 合併第一個維度
result1 = np.vstack((arr1, arr2))
print(result1)

# 合併第二個維度
result2 = np.hstack((arr1, arr2, arr3))
print(result2)