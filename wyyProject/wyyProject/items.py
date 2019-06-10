# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WyyprojectItem(scrapy.Item):
    # 网易云评论字段
    # 用户id
    userId = scrapy.Field()
    # 用户名
    nickname = scrapy.Field()
    # 用户头像图片链接（临时决定下载的，说不定以后能做为样本用得到）
    avatarUrl = scrapy.Field()
    # 评论id（网易云存储id的标识）
    commentId = scrapy.Field()
    # 评论内容
    content = scrapy.Field()
    # 评论时间（这里是时间戳的格式）
    times = scrapy.Field()
    # 点赞数
    likedCount = scrapy.Field()
    # 父评论id（应该是回复评论是的被回复那条评论的id，有点拗口）
    parentCommentId = scrapy.Field()
