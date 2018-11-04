from flask import Flask,abort,request,jsonify
import requests
from bs4 import BeautifulSoup



app = Flask(__name__)
@app.route('/getpara',methods=['GET'])
def getPara():
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
                for i,title in enumerate(header):
                        dic['title{}'.format(i)] = title.string
                        
                        


                meta = soup.select('.entry-meta')
                for spans in meta:
                        span = spans.find("span")
                        for j,time in enumerate(span):
                                dic['time'.format(j)] = time.string  #爬取时间


                summary = soup.select('.entry-summary')
                for ps in summary:
                        p=ps.find("p")
                        for t,sump in enumerate(p):
                                dic['summary{t}'.format(t)] = sump.string
                                   #爬取总结

        def main():
                url = "https://blog.snowstar.org/"
                html = getHTML(url)
                getContent(html)
                return jsonify(dic)

        main()                                  #woc 这样数据渲染好乱

        
@app.route('/search',methods=['GET'])
def search():#搜索功能 关键词keywod
        headers={'User-Agent':'Mozilla/5.0'}        
        kv = {'s':'an'}
        url = "https://blog.snowstar.org/?s={}".format(keyword)
        r = requests.get(url,headers=headers)
        print(len(r.text))
        

if __name__ == '__main__':
    app.run()








                        
        

  

