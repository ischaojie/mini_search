# hakuna电影搜索引擎（mini）
> scrapy+elasticsearch+flask+vue

just for fun,for learn.

![hakuna](hakuna.gif)
## how to run？
```
# 安装中文分词插件el
#
> elasticsearch-plugin install <>
# 启动elasticsearch
> bin/elasticsearch

# 设置虚拟环境
> python -m venv env
> source env/bin/activate
> pip install -r requirements.txt

# 启动爬虫
# 数据自动送入elasticsearch
scrapy crawl douban

# server
> python app.py

# client
> npm install
> npm run serve

# localhost:8080
```