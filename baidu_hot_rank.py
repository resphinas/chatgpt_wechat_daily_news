# *- coding: utf-8 -*
"""
@File   : baidu_hot_rank.py
@Author : JMz
@Date   : 2023/7/31 0031 2023/07/31
"""
import pickle
import re

import requests
from bs4 import BeautifulSoup

url = 'http://top.baidu.com/buzz?b=1&fr=topindex'


def getSoup(Url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }  # 设置请求头
    proxy = {'http': 'http://101.4.136.34:82'}  # 设置代理 http-协议类型 101.4.136.34-代理ip  82-代理端口
    # urls = requests.get(url, headers=headers)
    r = requests.get(url, headers=headers, timeout=30)
    r.encoding = r.apparent_encoding  # 获取网页的编码格式
    # context = r.text  # 获取HTML网页
    soup = BeautifulSoup(r.text, 'html.parser')  # 解析网页
    return soup


def getContext():
    news = []
    soup = getSoup(url)
    # 获取<div class='category-wrap_iQLoo horizontal_1eKyQ'></div>所有标签项
    info_clear_all = soup.find_all('div', class_='category-wrap_iQLoo horizontal_1eKyQ')
    for a in info_clear_all:
        # 获取标题
        label_a_title = a.find('div', class_='c-single-text-ellipsis')  # 获取标题所在的a标签
        title = label_a_title.text.replace(' ', '').strip().replace('\n', '')  # 获取标题
        # print('标题:' + title)

        # 获取热搜指数
        # hot_index = a.find('div', class_='hot-index_1Bl1a')
        # # print(hot_index)
        # hot_index_num = hot_index.text.replace(' ', '').strip().replace('\n', '')
        # print('热搜指数:' + hot_index_num)


        hot_html = a.find('a', class_='img-wrapper_29V76')
        # print(hot_html)
        # hot_html = '<a class="img-wrapper_29V76" href="https://www.baidu.com/s?wd=%E4%BF%83%E8%BF%9B%E6%B0%91%E8%90%A5%E7%BB%8F%E6%B5%8E%E5%81%9A%E5%A4%A7%E5%81%9A%E4%BC%98%E5%81%9A%E5%BC%BA&amp;sa=fyb_news&amp;rsv_dl=fyb_news" target="_blank"> <div class="index_1Ew5p c-index-bg1"> <img alt="true" class="top-icon_15tUE" src="//fyb-pc-static.cdn.bcebos.com/static/asset/whitet@2x_0fd85d7c9f42d73571bd1168903afb74.png"/> </div> <img alt="" src="https://fyb-2.cdn.bcebos.com/hotboard_image/0e127d29a68e9a4fd230fc519b1658dd?x-bce-process=image/resize,m_fill,w_256,h_170"/> <div class="border_3WfEn"></div> </a>'
        hot_html_str = None
        if hot_html != None:
            pattern = r'<a class="img-wrapper_29V76" href="([^"]+)"'
            matches = re.findall(pattern, str(hot_html))
            # print('网址:' + matches[0])
            hot_html_str = '网址:' + matches[0]
        news.append(title + '\n' + hot_html_str)

    # print(len(info_clear_all))

    try:
        with open('baidu_hot.txt', 'rb') as f:
            bhr = pickle.load(f)
    except:
        bhr = {}
        # print(cjb)

    news_list = []
    for item in news:
        if item not in bhr:
            news_list.append(item)
    with open('baidu_hot.txt', 'wb') as f:
        pickle.dump(news, f)

    news_message = "百度热搜榜:\n\n"

    if news_list == []:
        return None
    for i in range(len(news_list)):
        if len(news_list) > 1:
            add_string = str(i+1) + "、"
        else:
            add_string = ""
        news_message += f"{add_string}{news_list[i]}\n"
    return news_message


if __name__ == "__main__":
    hot_rank_list = getContext()
    print(hot_rank_list)