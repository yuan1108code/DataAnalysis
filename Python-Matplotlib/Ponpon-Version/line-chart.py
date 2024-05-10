import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode Ms']

# plt.plot([1, 2, 3], [2, 4, 6])

# plt.plot([1, 2, 3], [[2, 1], [4, 2], [6, 3]], label = ["第一組標籤", "第二組標籤"])

import csv 

file = open("data.csv", encoding="utf-8")
reader = csv.reader(file)
header = next(reader) # 讀取第一列
print("標頭", header)

x = []
y = []

for row in reader:
    print("每列的資料", row)
    x.append(int(row[0]))
    y.append([int(row[1]), int(row[2])])

plt.plot(x, y, label=header[1:3])

plt.legend() # 產生圖例
plt.xlabel(header[0])
plt.ylabel("薪資")
plt.show()
