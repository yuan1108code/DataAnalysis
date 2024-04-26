import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode Ms']

# plt.bar([3, 4, 1], [8, 5, 2])

# plt.bar(["B", "A", "C"], [8, 10 ,16], width=0.5, color="red")
# plt.xlabel("測試的 x 軸")
# plt.ylabel("測試的 y 軸")

# 從 CSV 格式的檔案載入資料，並繪製長條圖
import csv
file = open("bar-chart-data.csv", encoding="utf-8")
reader = csv.reader(file)
header = next(reader)

print(header)

x = []
height = []

for row in reader:
    x.append(row[0])
    height.append(int(row[1]))
plt.bar(x, height, width = 0.3, color="green")
plt.xlabel(header[0])
plt.ylabel(header[1])

plt.show()

