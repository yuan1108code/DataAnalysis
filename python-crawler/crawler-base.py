import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 抓取 PTT 電影版網頁原始碼 ( HTML )
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"

# 建立一個 Request 物件，附加 Request Header 的資訊
request = req.Request(url, headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# print(data)

# 解析原始碼，取得每篇文章的標題
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
# print(root.title.string)

# titles = root.find("div", class_="title") # 尋找 class = "title" 的 div 標籤
# print(titles.a.string)

titles = root.find_all("div", class_="title") # 尋找 class = "title" 的 div 標籤
for title in titles:
    if title.a != None: # 如果標題包含 a 標籤 (沒有被刪除)，印出來
        print(title.a.string)