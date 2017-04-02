# -*- coding: utf-8 -*-

# Scrapy settings for News_Scrapy project
import os

BASE_DIR = os.path.split(os.path.realpath(__file__))[0]

BOT_NAME = 'News_Scrapy'

SPIDER_MODULES = ['News_Scrapy.spiders']
NEWSPIDER_MODULE = 'News_Scrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'News_Scrapy (+http://www.yourdomain.com)'

ITEM_PIPELINES={
    'News_Scrapy.pipelines.NewsScrapyPipeline':300,
   # 'News_Scrapy.pipelines.WebcrawlerScrapyPipeline':300
}

LOG_LEVEL='DEBUG'

CONCURRENT_REQUESTS=20
CONCURRENT_REQUESTS_PER_DOMAIN = 20
DEPTH_PRIORITY=0
DEPTH_STATS=True
DEPTH_STATS_VERBOSE=True
DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = False
ROBOTSTXT_OBEY = False


SAVED_URL_PATH = BASE_DIR + "/SAVED_URL.pkl"

#Mysql configuration information
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'website'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'plusplus'

MYSQL_PORT = 3306 