import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as req

def getData(url):
    # 建立一個 Request 物件，附加 Request Header 的資訊
    request = req.Request(url, headers = {
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    # 解析原始碼，取得每篇文章的標題
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title") # 尋找 class = "title" 的 div 標籤

    for title in titles:
        if title.a != None: # 如果標題包含 a 標籤 (沒有被刪除)，印出來
            print(title.a.string)

    # 抓取上一頁連結
    nextlink = root.find("a", string = "‹ 上頁") # 找到內文是 ‹ 上頁 的標籤
    return nextlink["href"]

# 抓取 PTT 八卦板網頁原始碼 ( HTML )
Pageurl = "https://www.ptt.cc/bbs/Gossiping/index.html"

# 抓取 Count 個頁面
count = 0
while count < 3:
    Pageurl = "https://www.ptt.cc/" + getData(Pageurl)
    count += 1