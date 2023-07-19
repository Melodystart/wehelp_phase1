import urllib.request as req
from bs4 import BeautifulSoup
import threading
import time

def get_article_time(article_url): #def: 取得文章的發文時間

  request=req.Request(article_url, headers={
      "User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
  })
  with req.urlopen(request) as res:
      data = res.read().decode("utf-8")
  soup = BeautifulSoup(data,"html.parser")
  article_time = soup.find_all("span", class_="article-meta-value")[3].text
  return article_time 

def get_article(url, pages): #def: 抓取指定url及指定頁數資料

  txt_list = []

  # 建立一個 Request 物件，並附加一個 Request Headers 的資訊
  request=req.Request(url, headers={
      "User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
  })

  with req.urlopen(request) as res:
      data = res.read().decode("utf-8")

  soup = BeautifulSoup(data,"html.parser")

  page = soup.find_all('a', string="‹ 上頁")[0].get("href") #取得'上頁'頁數
  final_page = int(page[page.index('index')+5:page.index('.html')]) + 1

  start = url.index('bbs')
  end = url.index('/index.html')
  board = url[(start+4):end]

  #抓取指定頁數資料
  for i in range(pages-1, -1, -1):
    page_url = 'https://www.ptt.cc/bbs/'+ board + '/index'+ str(final_page - i) +'.html'

    request=req.Request(page_url, headers={
      "User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"})

    with req.urlopen(request) as res:
      data = res.read().decode("utf-8")

    soup = BeautifulSoup(data,"html.parser")

    result = soup.find_all('div', class_="r-ent")

    for block in result:

      try:
        title_block = block.select('div.title a')
        title = title_block[0].text
      except:
        title = block.select('div.title')[0].text.strip()

      try:
        push = block.select('span')[0].text
      except (IndexError):
        push = 0
      
      try:
        article_url = "https://www.ptt.cc"+title_block[0].get("href")
        time = get_article_time(article_url)
      except:
        time = ""

      txt_list.append([title, push, time])
        

  f = open( board+".txt", "w", encoding='UTF-8')
  for article in txt_list:
      for item in article:
              f.write(str(item))
              if item != article[len(article)-1]:
                f.write(",")
              else:
                pass
      f.write("\n")
  f.close()

T1 = time.perf_counter()

board = ['https://www.ptt.cc/bbs/movie/index.html','https://www.ptt.cc/bbs/Food/index.html','https://www.ptt.cc/bbs/Japan_Travel/index.html','https://www.ptt.cc/bbs/CVS/index.html']

threads = []

for i in range(len(board)):
  threads.append(threading.Thread(target = get_article, args = (board[i],3)))
  threads[i].start()

for i in range(len(board)):
  threads[i].join()

T2 =time.perf_counter()

print('%s毫秒' % ((T2 - T1)*1000))