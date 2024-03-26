# 載入 numpy 套件
import numpy as np
# 準備測試資料
arr = np.array([
    [2, 4, 6, 8, 10, 12],
    [1, 3, 5, 7, 9, 11]
])

# 根據第 1 個維度切割
result1 = np.vsplit(arr, 2)
print(result1)

# 根據第 2 個維度切割
result2 = np.hsplit(arr, 2)
print(result2)

# 根據第 2 個維度切割成 3 個陣列
result3 = np.hsplit(arr, 3)
print(result3)