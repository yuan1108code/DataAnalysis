import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode Ms']
# x = [10, 15, 25]
# total = sum(x)
# labels = {str(100 * data / total) + "%" for data in x}

# plt.pie(x, labels = labels
#         , labeldistance = 0.5)
import csv 

file = open("pie-chart-data.csv", encoding="utf-8")
reader = csv.reader(file)
next(reader) # 讀取第一列

x = []
labels = []

for row in reader:
    x.append(int(row[1]))
    labels.append(row[0])

plt.pie(x, labels = labels, labeldistance = 1.0)

plt.title("瀏覽器的市場佔有率")
plt.legend()
plt.show()