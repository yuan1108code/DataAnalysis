# 載入 Selenuim 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 設定 Chrome Driver 的執行檔路徑
options = Options()
options.chrome_executable_path = "/Users/zhuboyuan/Library/CloudStorage/OneDrive-NationalPingtungUniversity/NPTU - 國立屏東大學/NPTU - Programming/Program - Python/Python - DataAnalysics/chromedriver"

# 建立 Driver 物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options = options)

# 連線到 PTT 股票版

driver.get("https://www.ptt.cc/bbs/Stock/index.html")
# print(driver.page_source) # 取得網頁原始碼
tags = driver.find_elements(By.CLASS_NAME, "title") # 搜尋 class 屬性是 title 的所有標籤
for tag in tags:
    print(tag.text)

# 取得上一頁文章標題
link = driver.find_element(By.LINK_TEXT, "‹ 上頁")
link.click() # 模擬使用者點擊連結標籤
tags = driver.find_elements(By.CLASS_NAME, "title") # 搜尋 class 屬性是 title 的所有標籤
for tag in tags:
    print(tag.text)

# driver.close()