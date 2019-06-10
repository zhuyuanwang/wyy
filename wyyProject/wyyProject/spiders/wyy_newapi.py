# -*- coding: utf-8 -*-
import scrapy,json,time,random
from ..settings import DEFAULT_REQUEST_HEADERS
from ..items import WyyprojectItem

class WyySpider(scrapy.Spider):
    name = 'wyy_newapi'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/']

    def start_requests(self):
        #
        # offset就是（评论页数-1） * 20  2019年6月10日17:47:48  目前总页数为：12421
        for page in range(1,500):   #先爬取前500页
            time.sleep(random.random())
            offset = (page - 1) * 20
            start_url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_513360721?limit=100&offset={}'.format(str(offset))
            yield scrapy.Request(url=start_url,headers=DEFAULT_REQUEST_HEADERS,callback=self.parse_info)

    def parse_info(self, response):
        time.sleep(random.random())
        # print(response.text)
        item = WyyprojectItem()
        # 将网页响应的源码转化为json格式,以便使用字典取值
        datajson = json.loads(response.text)
        Comments = datajson['comments']
        # 获取评论列表
        for comment in Comments:
            userId = comment['user']['userId']
            nickname = comment['user']['nickname']
            avatarUrl = comment['user']['avatarUrl']
            commentId = comment['commentId']
            content = comment['content']
            times = comment['time']
            likedCount = comment['likedCount']
            parentCommentId = comment['parentCommentId']
            # 将时间戳转为时间
            timestamp = str(times)[:10]
            timearray = time.localtime(int(timestamp))
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timearray)
            item['userId'] = userId
            item['nickname'] = nickname
            item['avatarUrl'] = avatarUrl
            item['commentId'] = commentId
            item['content'] = content
            item['times'] = otherStyleTime
            item['likedCount'] = likedCount
            item['parentCommentId'] = parentCommentId

            yield item
