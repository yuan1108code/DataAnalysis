import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode Ms']

# 繪製一組資料點的散佈圖，呃定樣式
# plt.scatter([2, 4, 3], [4, 3, 6], c="red", s=30)

# 繪製兩組資料點的散佈圖，加上標籤與圖例
# plt.scatter([2, 4, 3], [4, 3, 6], c="orange", s=30, label = "第一組")
# plt.scatter([1, 3, 4], [2, 5, 4], c="blue", s=30, label = "第二組")
# plt.legend()

# 載入 CSV 檔案格式的資料，並繪製散佈圖
import csv

file = open("scatter-chart-data.csv", encoding="utf-8")
reader = csv.reader(file)
next(reader) # 跳過第一列
data = {
    "男":{"x":[], "y":[]},
    "女":{"x":[], "y":[]},
}
for row in reader:
    gender = row[0]
    data[gender]["x"].append(int(row[1]))
    data[gender]["y"].append(int(row[2]))
    # print(row)
plt.scatter(data["男"]["x"], data["男"]["y"], c="blue", s=30, label = "男")
plt.scatter(data["女"]["x"], data["女"]["y"], c="orange", s=30, label = "女")

plt.legend()
plt.show()
