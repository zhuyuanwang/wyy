# -*- coding: utf-8 -*-
import scrapy,json,time
from ..settings import DEFAULT_REQUEST_HEADERS
from ..items import WyyprojectItem

class WyySpider(scrapy.Spider):
    name = 'wyy'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/']

    def start_requests(self):
        start_urls = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_513360721?csrf_token='
        form_data = {
            'params': 'NWv4IO6Ynrlad2I1rXzETh6j63uonEwIjxoM + A2JKsEYtwrYDlZXjgNPjOXqyL3FzTWPFa5F5rWXalH5TYhZ / fPq7Sa2yKOOxkAhHJ4cqvJ5Y5TZxD6DPEVG2WQ + I + X70G0DlTjCeLnBkErsXu5SpnHzPbhwGjKkvfcLjcVB2u8uDH9 + ETRKTphE6gKi9G + W',
            'encSecKey': 'b8036b450ae5524c4c5a4f2855ca7f88fc0420d892b3a27a579b7bb659bd659e6b9f00ac3d4ce85c33fb3733c93dbfbad287cf565747bcd64517034a5d4cc0b868f97ec0551d1a7597b9dc520a6cd631fd7b50f939b5555de80cb6ddf69817fa47182d078f6e7968b52cb5e963f775f99c0902fd85ec9bbfc6ed3fe6592650f8',
        }
        yield scrapy.FormRequest(url=start_urls,headers=DEFAULT_REQUEST_HEADERS,formdata=form_data,callback=self.parse_info)

    def parse_info(self, response):
        item = WyyprojectItem()
        # 将网页响应的源码转化为json格式,以便使用字典取值
        datajson = json.loads(response.text)
        # 获取评论列表
        Comments = datajson['hotComments']
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
