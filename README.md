# hakuna电影搜索引擎（mini）
> scrapy+elasticsearch+flask+vue

just for fun,for learn.

![search](search.png)

![search_result](searchresult.png)
## how to run？
```
# 安装中文分词插件el
> elasticsearch-plugin install <>
# 启动elasticsearch
> bin/elasticsearch

# server
> python -m venv env
> source env/bin/activate
> pip install -r requirements.txt
> python app.py

# client
> npm install
> npm run serve

```