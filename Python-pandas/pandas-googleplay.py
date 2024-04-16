# 載入 pandas 模組
import pandas as pd

# 讀取資料
data = pd.read_csv("GooglePlayStore.csv")
# 觀察資料
print("資料數量", data.shape)
print("資料欄位", data.columns)
print("################################")
# 分析資料 : 評分的各種統計數據
# condition = data["Rating"] <= 5
# data = data[condition]

# print("平均數: ", data["Rating"].mean())
# print("中位數: ", data["Rating"].median())
# print("前一名應用程式的平均數: ", data["Rating"].nlargest(100).mean())

# 分析資料 : 安裝數量的各種統計數據
# print(data["Installs"][10472])
data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]", "", regex=True).replace("Free", "")) # 把 字串 轉換成 數字 ，和刪除 + 字元
print("平均數: ", data["Installs"].mean())
condition = data["Installs"] > 100000
print("安裝數量大於 100000 的應用程式個數: ", data[condition].shape[0])

# 基於資料的應用 : 關鍵字搜尋應用程式名稱
keyword = input("請輸入關鍵字: ")
condition = data["App"].str.contains(keyword, case=False) # case = False 來忽略大小寫
print("關鍵字應用程式的名稱: ", data["App"][condition])
print("關鍵字應用程式的數量: ", data[condition].shape[0])
