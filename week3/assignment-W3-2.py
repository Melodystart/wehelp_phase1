def get_article_time(article_url): #def: 取得文章的發文時間

  request=req.Request(article_url, headers={
      "User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
  })
  with req.urlopen(request) as res:
      data = res.read().decode("utf-8")
  soup = BeautifulSoup(data,"html.parser")
  article_time = soup.find_all("span", class_="article-meta-value")[3].text
  return article_time 

import urllib.request as req
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'

txt_list = []

# 建立一個 Request 物件，並附加一個 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})

with req.urlopen(request) as res:
    data = res.read().decode("utf-8")

soup = BeautifulSoup(data,"html.parser")

page = soup.find_all('a', string="‹ 上頁")[0].get("href") #取得'上頁'的頁數
final_page = int(page[page.index('index')+5:page.index('.html')]) + 1

#抓取最新頁-2頁~最新頁的資料
for i in range(2, -1, -1):

  page_url = 'https://www.ptt.cc/bbs/movie/index' + str(final_page - i) +'.html'

  request=req.Request(page_url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
})

  with req.urlopen(request) as res:
    data = res.read().decode("utf-8")

  soup = BeautifulSoup(data,"html.parser")

  result = soup.find_all('div', class_="r-ent")

  for block in result:
    try:
      title = block.select('div.title a')
      push = block.select('span')
      article_url = "https://www.ptt.cc"+title[0].get("href")

      txt_list.append([title[0].text, push[0].text, get_article_time(article_url)])
      
    except (IndexError):
      pass

f = open("movie.txt", "w")
for article in txt_list:
    for item in article:
            f.write(str(item))
            if item != article[len(article)-1]:
              f.write(",")
            else:
              pass
    f.write("\n")
f.close()