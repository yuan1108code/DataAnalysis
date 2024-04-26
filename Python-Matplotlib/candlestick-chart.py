import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode Ms']

# plt.bar("11/01", 15, bottom = 80, color = "green", width = 0.5)
# plt.bar("11/01", 25, bottom = 75, color = "green", width = 0.1)

# plt.bar("11/02", 7, bottom = 75, color = "green", width = 0.5)
# plt.bar("11/02", 18, bottom = 65, color = "green", width = 0.1)

# plt.bar("11/03", 12, bottom = 73, color = "red", width = 0.5)
# plt.bar("11/03", 20, bottom = 70, color = "red", width = 0.1)

# 從 CSV 格式的檔案載入資料，並繪製 K 線圖
import csv
file = open("candelstick-chart-data.csv", encoding="utf-8")
reader = csv.reader(file)
header = next(reader)

for row in reader:
    date = row[0]
    open_price = int(row[1])
    close_price = int(row[2])
    highest = int(row[3])
    lowest = int(row[4])
    
    color = "green"
    
    if open_price > close_price:
        color = "red"
    
    plt.bar(date, abs(open_price - close_price)
            , bottom = min(open_price, close_price)
            , color = color
            , width = 0.5)  # 繪製陽線

    plt.bar(date, highest - lowest
            , bottom = lowest
            , color = color
            , width = 0.1)
    
plt.show()