# 作者：Hugh
# 创建日期；2022/12/26

#拿到页面源代码
#使用bs4进行解析,拿到数据

import  requests, bs4

url = "http://xinfadi.com.cn/getPriceData.html"

resp = requests.post(url)

# 解析数据
## 把页面源代码交给BeautifulSoup处理,生成bs对象
page = bs4.BeautifulSoup(resp.text,"html.parser")   #指定html解析器
#























