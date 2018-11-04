import requests
from bs4 import BeautifulSoup
import bs4


dic = {}
        
def getHTML(url):
        try:
                headers={'User-Agent':'Mozilla/5.0'}
                r = requests.get(url,headers = headers)
                r.raise_for_status()
                r.encoding = r.apparent_encoding
                html = r.text
                return html
        except:
                return ""
                
def getContent(html):
        soup = BeautifulSoup(html,'html.parser')
        header = soup.select('.entry-header div div h2')
        for title in header:
                print(title.string)             #爬取主题   


        meta = soup.select('.entry-meta')
        for spans in meta:
                span = spans.find("span")
                for time in span:
                        print(time.string)  #爬取时间


        summary = soup.select('.entry-summary')
        for ps in summary:
                p=ps.find("p")
                for sump in p:
                        print(sump.string)   #爬取总结

def main():
        url = "https://blog.snowstar.org/"
        html = getHTML(url)
        getContent(html)
        



#def search():#搜索功能 关键词keywod
 #       headers={'User-Agent':'Mozilla/5.0'}        
  #      kv = {'s':'an'}
   #     url = "https://blog.snowstar.org/?s={}".format(keyword)
    #    r = requests.get(url,headers=headers)
     #   print(len(r.text))
        
main()
