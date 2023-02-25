# 作者：Hugh
# 创建日期；2022/12/21

from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)

with open ("mybaidu.html", mode = "w",encoding="utf-8") as f:
        f.write(resp.read().decode("utf-8"))
print("over!")









