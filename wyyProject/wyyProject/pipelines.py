# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql

class WyyprojectPipeline(object):

    def open_spider(self, spider):
        self.fp = open('data.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        obj = dict(item)
        string = json.dumps(obj,ensure_ascii=False)
        self.fp.write(string + '\n')
        return item

    def close_spider(self, spider):
        self.fp.close()


class MysqlPipeline(object):

    def open_spider(self, spider):
        # 连接数据库
        self.conn = pymysql.Connect(host='192.168.99.1',port=3306,user='root',password='123456',db='spiders',charset='utf8')
        # 获取游标
        self.cursor = self.conn.cursor()
        # 捕获异常并写入文本
        self.f = open('WYY_ERROR_IO.txt','a',encoding='utf-8')

    def process_item(self,item,spider):
        # 拼接sql语句
        sql = 'insert into wangyiyun (userId,nickname,avatarUrl,commentId,content,times,likedCount,parentCommentId) values ("%s","%s","%s","%s","%s","%s","%s","%s")' % (item['userId'],item['nickname'],item['avatarUrl'],item['commentId'],pymysql.escape_string(item['content']),item['times'],item['likedCount'],item['parentCommentId'])

        try:
            self.cursor.execute(sql)
            #提交
            self.conn.commit()
        except Exception as e:
            self.f.write(str(e))
            self.conn.rollback()

        return item

    def close_spider(self,spider):
        # 关闭连接
        self.cursor.close()
        self.conn.close()