"""
create by 维尼的小熊 on 2018/7/25

"""
__autor__ = 'yasin'

from selenium import webdriver
from scrapy.selector import Selector
import pandas as pd


browser = webdriver.Chrome(executable_path="/Users/yiyang/Desktop/chromedriver")
browser.get("http://s.weibo.com/top/summary?cate=realtimehot")


t_selector = Selector(text=browser.page_source)
print(t_selector.css(".rank_content .star_name a::text").extract())
print(t_selector.css(".star_num span::text").extract())

def convertToHtml(result,title):
    #将数据转换为html的table
    #result是list[list1,list2]这样的结构
    #title是list结构；和result一一对应。titleList[0]对应resultList[0]这样的一条数据对应html表格中的一列
    d = {}
    index = 0
    for t in title:
        d[t]=result[index]
        index = index+1
    df = pd.DataFrame(d)
    df = df[title]
    h = df.to_html(index=False)
    return h

str =t_selector.css(".rank_content .star_name a::text").extract()
num = t_selector.css(".star_num span::text").extract()
num.insert(0,'最高')
fh = open("32111.html", 'w')

fh.write(convertToHtml([str,num],['热点名称','搜索热度']))
fh.close()
browser.quit()

