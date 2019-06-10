# import wordcloud
#
# w = wordcloud.WordCloud()
# w.generate('zhuyuanwang and yw')
# w.to_file('test1.png')

# from wordcloud import WordCloud
# f = open(r'wordcloud.txt','r',encoding='utf-8').read()
# wordcloud = WordCloud(background_color="white",width=5000, height=1500, margin=2).generate(f)
#
#
# import matplotlib.pyplot as plt
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()
# wordcloud.to_file('test.png')
# # 保存图片,但是在第三模块的例子中 图片大小将会按照 mask 保存

import jieba
import wordcloud
from scipy.misc import imread

def make_cloud(input_file, output_file, **kwargs):

      width = kwargs.get("width")
      height = kwargs.get("height")
      background_color = kwargs.get("background_color")
      font_path = kwargs.get("font_path")
      max_words = kwargs.get("max_words")

      f = open(input_file, "r", encoding="utf-8")
      data = f.read()
      f.close()

      ls = jieba.lcut(data)                   # 分词
      txt = " ".join(ls)                      # 将列表中的单词连接成一个字符串

      w = wordcloud.WordCloud(width=width, height=height, background_color=background_color, font_path=font_path,max_words=max_words)
      w.generate(txt)
      w.to_file(output_file)


def make_cloud_png(input_file, output_file, png_file, **kwargs):

      width = kwargs.get("width")
      height = kwargs.get("height")
      background_color = kwargs.get("background_color")
      font_path = kwargs.get("font_path")
      max_words = kwargs.get("max_words")
      mask = imread(png_file)

      f = open(input_file, "r", encoding="utf-8")
      data = f.read()
      f.close()

      ls = jieba.lcut(data)                   # 分词
      txt = " ".join(ls)                      # 将列表中的单词连接成一个字符串

      w = wordcloud.WordCloud(width=width, height=height, background_color=background_color, font_path=font_path,max_words=max_words, mask=mask)
      w.generate(txt)
      w.to_file(output_file)