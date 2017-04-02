# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import pymongo

#from scrapy.exceptions import DropItem
#from scrapy.conf import settings
#from scrapy import log
import sqlalchemy
#from model.config import DBSession
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, Numeric, String
from sqlalchemy.orm import sessionmaker
#class news(object):
#      def __init__(self, url, content, title):
#          self.
#Base=declarative_base()

class NewsScrapyPipeline(object):
    def open_spider(self, spider):
        self.f = open('Info.txt', 'w')
#        self.session = DBSession()
     
    def close_spider(self, spider):
        self.f.close()
#        self.session.close()
    def process_item(self, item, spider):
        #engine = create_engine("mysql+pymysql://root:plusplus@localhost/website",
                #                    encoding='utf-8', echo=True)
        engine = (create_engine("mysql+pymysql://root:plusplus@localhost:3306/wangzhan?charset=utf8", max_overflow=5, encoding="utf-8", echo=True))
        connection = engine.connect()
        metadata = MetaData()
        news = Table('news',metadata,
#        Column('序号',Integer(10),autoincrement=True,primary_key=True),
        Column('title',String(200)),
        Column('cont',String(40000)),
        Column('url',String(100))
                 )
        metadata.create_all(engine)

        session = sessionmaker(bind=engine)
#        u=dict(url=str(dict(item)['news_url']),cont=str(dict(item)['news_content']),str(title=dict(item)['news_title']))
#        ins = news.insert()
        ins="insert into news values("+"'"+dict(item)['news_title']+"'"+","+"'"+dict(item)['news_content']+"'"+","+"'"+dict(item)['news_url']+"');"
#        r1 = connection.execute(i, **u)
        print('=====================ITEM=================')
        print('==================URL======================')
#        print(str(dict(item)))
        #print(dict(item)['news_url'])
#        type((dict(item)['news_url']))==str
#        type(str((dict(item)['news_url'])))==str
        print('==================CONTENT==================')
        print(dict(item)['news_content'])
        print('==================TITLE=====================')
 #       print(dict(item)['news_title'])
#        print(item)
        print('=================ITEM END==================')
        print('=================INS========================')
        print(ins)
        print('================INS END=====================')
#        result = connection.execute(ins)
        result=engine.execute(ins)
        try:
            
            line = str(dict(item)) + '\n'
            self.f.write(line)
            #write to text file
        except:
            pass
        return item 
    # def process_item(self, item, spider):
    #    return item

'''class WebcrawlerScrapyPipeline(object):
   

    def __init__(self,dbpool):
        self.dbpool=dbpool
       
        
    @classmethod
    def from_settings(cls,settings):
       # @classmethod声明一个类方法，平常见到的叫实例方法。 
        dbparams=dict(
            host=settings['MYSQL_HOST'],#read settings information from settings.py
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',#to avoid charset error
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=False,
        )
        dbpool=adbapi.ConnectionPool('MySQLdb',**dbparams)#**表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        return cls(dbpool)#相当于dbpool付给了这个类，self中可以得到

    #pipeline默认调用
    def process_item(self, item, spider):
        query=self.dbpool.runInteraction(self._conditional_insert,item)#to insert data
        query.addErrback(self._handle_error,item,spider)#调用异常处理方法
        return item
    
    #to write data into database
    def _conditional_insert(self,tx,item):
        #print item['name']
        sql="insert into testtable(name,url) values(%s,%s)"
        params=(item["name"],item["url"])
        tx.execute(sql,params)
    
    #deal with errors
    def _handle_error(self, failue, item, spider):
        print ('--------------database operation exception!!-----------------')
        print (failue)

'''