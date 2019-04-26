import os
from urllib import request
from lxml import etree

from cmdb import models


def crow(i):
    #  构造第i页的网址
    url = 'https://movie.douban.com/top250?start=' + str(25 * i)
    #  发送请求，获得返回的html代码并保存在变量html中
    html = request.urlopen(url).read().decode('utf-8')
    # 将返回的字符串格式的html代码转换成xpath能处理的对象
    html = etree.HTML(html)
    # 先定位到li标签，datas是一个包含25个li标签的list，就是包含25部电影信息的list
    datas = html.xpath('//ol[@class="grid_view"]/li')

    a = 0
    for data in datas:
        try:
            data_title = data.xpath('div/div[2]/div[@class="hd"]/a/span[1]/text()')
            data_info = data.xpath('div/div[2]/div[@class="bd"]/p[1]/text()')
            data_score = data.xpath('div/div[2]/div[@class="bd"]/div/span[@class="rating_num"]/text()')
            data_num = data.xpath('div/div[2]/div[@class="bd"]/div/span[4]/text()')
            data_picurl = data.xpath('div/div[1]/a/img/@src')

            # 封面图片保存路径和文件名
            pic_name = './static/imgs/' + str(i * 25 + a + 1) + '.jpg'

            # 下载封面图片到本地，路径为pic_name
            if not os.path.exists(pic_name):
                request.urlretrieve(data_picurl[0], filename=pic_name)

            # 插入数据到数据库
            models.MovieInfo.objects.create(ranking=str(i * 25 + a + 1),
                                            title=data_title[0],
                                            personnel_info=data_info[0].strip(),
                                            year=data_info[1].strip().split('/')[0],
                                            country=data_info[1].strip().split('/')[1],
                                            type=data_info[1].strip().split('/')[2],
                                            score=data_score[0],
                                            num=data_num[0])
        except:
            continue
        finally:
            a += 1


def static_crawler_main():
    for i in range(10):
        crow(i)
