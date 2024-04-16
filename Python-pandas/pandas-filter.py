# 載入 pandas 模組
import pandas as pd
# 篩選練習 - Series
data = pd.Series([30, 15, 20])
# condition = [True, False, True]
# condition = data > 18
# filteredData = data[condition]
# print(filteredData)

data = pd.Series(["您好", "Python", "Pandas"])
# condition = [False, True, True]
# condition = data.str.contains("P")
# filteredData2 = data[condition]
# print(filteredData2)

# 篩選練習 - DataFrame
data = pd.DataFrame({
    "name":["Amy", "Bob", "Charles"],
    "salary":[30000, 50000, 40000]
})
print(data)
# condition = [False, True, True]
condition = data["name"] == "Amy"
# condition = data["salary"] >= 40000
filteredData3 = data[condition]
print(filteredData3)
