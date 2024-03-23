# 載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 設定 Chrome Driver 的執行檔路徑
options = Options()
options.chrome_executable_path = "/Users/zhuboyuan/Library/CloudStorage/OneDrive-NationalPingtungUniversity/NPTU - 國立屏東大學/NPTU - Programming/Program - Python/Python - DataAnalysics/chromedriver"

# 建立 Driver 物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options = options)

# 連線到 LeetCode 登入頁面
driver.get("https://elearning.nptu.edu.tw/mooc/login.php")

# 輸入帳號密碼，按下登陸按鈕
usernameInput = driver.find_element(By.ID, "username")
passwordInput = driver.find_element(By.ID, "password")
usernameInput.send_keys("CBB109218")
passwordInput.send_keys("S125489370")


signinBtn = driver.find_element(By.ID, "btnSignIn")
signinBtn.send_keys(Keys.ENTER)

# 等待登入完成
time.sleep(5)  # 單位為秒，這裡等待5秒

# 連線到登入後才能取得資料的頁面，並取得想要的資料
stateElement = driver.find_element(By.CSS_SELECTOR, "[class=paginate-number-after]")
print(stateElement.text)



driver.quit()