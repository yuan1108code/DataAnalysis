# 載入 Selenuim 相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 設定 Chrome Driver 的執行檔路徑
options = Options()
options.chrome_executable_path = "/Users/zhuboyuan/Library/CloudStorage/OneDrive-NationalPingtungUniversity/NPTU - 國立屏東大學/NPTU - Programming/Program - Python/Python - DataAnalysics/chromedriver"

# 建立 Driver 物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options = options)
driver.maximize_window() # 視窗最大化
driver.get("https://www.google.com/")
driver.save_screenshot("screen_google.png") # 螢幕截圖

driver.get("https://www.ntu.edu.tw/")
driver.save_screenshot("screen_ntu.png")
driver.close()
