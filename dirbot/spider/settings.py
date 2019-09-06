# -*- coding: utf-8 -*-

# Scrapy settings for spider_learn project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spider'

SPIDER_MODULES = ['spider.spiders']
NEWSPIDER_MODULE = 'spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spider_learn (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 0.5

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

ITEM_PIPELINES = {
   'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 10,
}

ELASTICSEARCH_SERVERS = ['localhost']
ELASTICSEARCH_INDEX = 'douban'
ELASTICSEARCH_TYPE = 'movies'