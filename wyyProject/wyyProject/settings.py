# -*- coding: utf-8 -*-

# Scrapy settings for wyyProject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wyyProject'

SPIDER_MODULES = ['wyyProject.spiders']
NEWSPIDER_MODULE = 'wyyProject.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wyyProject (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wyyProject.middlewares.WyyprojectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'wyyProject.middlewares.WyyprojectDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'wyyProject.pipelines.WyyprojectPipeline': 300,
   'wyyProject.pipelines.MysqlPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DEFAULT_REQUEST_HEADERS = {
    # ':authority':'music.163.com',
    # ':method':'POST',
    # ':path':'/weapi/v1/resource/comments/R_SO_4_513360721?csrf_token=',
    # ':scheme':'https',
    # 'accept':'*/*',
    # 'accept-encoding':'gzip, deflate, br',
    # 'accept-language':'zh-CN,zh;q=0.9',
    # 'content-type':'application/x-www-form-urlencoded',
    'cookie':'mail_psc_fingerprint=c699d20ffc94bfe9e35f6d1480fb092c; _iuqxldmzr_=32; _ntes_nnid=2fd082474d70ea9626c97f56aef4f361,1558504090875; _ntes_nuid=2fd082474d70ea9626c97f56aef4f361; WM_TID=Xu%2BEEScpa3dERFVUBQc5mea9RyNgFNDK; usertrack=CrH7DlzrRwoa14jpAyPkAg==; UM_distinctid=16b0220187d310-0ce1e5f5f2a201-6313363-144000-16b0220187e6a4; Province=0; City=0; __gads=ID=a70da7c4d0047dc9:T=1559108788:S=ALNI_MaUKOFDQCIzeH9VjL9Posu9gi07GA; vinfo_n_f_l_n3=7da8de0063e9fefd.1.3.1559108787963.1559133616127.1559206820174; NNSSPID=50452a9bf18f4d08b8afd6c37012ae44; P_INFO=m17746572170@163.com|1559646533|0|mail163|00&99|not_found&1559645865&mail163#not_found&null#10#0#0|177170&1|urs&mail163|17746572170@163.com; JSESSIONID-WYYY=%2FTaRsHCs3vSHl1qOvmI5iXezdPku9wHQyuMzp945aov0wdwOxa%2BWO6ED7WJTOu%5CVIA4biEjkYlgyMOwKvZrl2OeuvRkRRp95ZuzdDYeS4qNnv3A5Gp%5C0HVFCtvnPOXQ9c2Nz1SgBh7CHR7V245Q4wUA0%2FgyI4dv69nv3Ag%2F2fYK5qh6w%3A1559794405831; WM_NI=MgB1kQxWkcRUTwHrd2%2BiDZ1MeZGM6WWkcy1oFQkd269biKkoK4rdlm4%2F8g%2FIaXqsootS4oU2CEHXRsPzLHRd6QsUYYKcAM%2FpqNpW42eUbU9L86K4cgdN6qd4hXg%2B0oCEY2Y%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea2c65e959df7a8e53cf49e8ab3c84e979a8fafb763f3b68793d864fc8de198b42af0fea7c3b92a8fb98ed2ea5bbc89a584d15f98a98893e73ae9b78cbbb447a78689aeb55d95b5ad9ab465868fa585b13efbbea7acea6589ecbe85ef67f8f1f888ae43a388bf94ee65b88dfc90d83a819b88b9d17994a684a9d170f68fbdb6dc5389bd8faeae7cb392c0b8b73aa78baeb6bc48fcea85d5e26da892fa92e740ac88a9ccb365819b97d3dc37e2a3',
    'origin':'https://music.163.com',
    'referer':'https://music.163.com/song?id=513360721',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
}



# 2019年6月10日17:26:11  亲测使用splash无效
# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
# }
#
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_splash.SplashCookiesMiddleware': 723,
#     'scrapy_splash.SplashMiddleware': 725,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810
# }
#
# SPLASH_URL = 'http://192.168.99.100:8050'
#
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'