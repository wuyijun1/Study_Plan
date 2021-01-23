# 2020-02-05
# 下载网站荣耀所有英雄的所有皮肤
import requests
import json
from lxml import etree
import re
import os

try:
    os.makedirs('.\img')
except Exception as e:
    pass
url_json = "https://pvp.qq.com/web201605/js/herolist.json"  # 数据接口
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
response = requests.get(url=url_json, headers=headers)  # 请求数据
data_str = response.text  # 文本化数据
data_list = json.loads(data_str)  # 列表化数据
for data_dict in data_list:  # 取每一个列表
    ename = data_dict['ename']  # ID
    cname = data_dict['cname']  # 英雄名字
    try:
        skin_name = data_dict['skin_name'].split('|')  # 以|分割字符串
    except Exception as e:
        pass
    url = f"https://pvp.qq.com/web201605/herodetail/{ename}.shtml"  # 英雄网页地址
    response = requests.get(url=url, headers=headers)  # 请求数据
    response.encoding = response.apparent_encoding  # 解码内容
    html = etree.HTML(response.text)  # HTML化内容
    data_imgname = html.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')  # 定位皮肤名
    data_imgname = str(data_imgname).split('|')  # 分割字符串
    data_imgname_list = []  # 构建空列表
    for i in data_imgname:  # 展开皮肤列表
        i = i.replace("[", "").replace("]", "").replace("'", "")  # 字符串清洗
        data_imgname_list.append(i.split('&')[0])  # 添加到列表
    for i in range(len(data_imgname_list)):  # 展开英雄皮肤列表
        img_url = f"http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i + 1}.jpg"  # 构建图片地址
        name = f"{cname}-{data_imgname_list[i]}"  # 构建文件名
        print("正在下载：",name)
        img_data = requests.get(img_url, headers=headers)  # 请求数据
        with open(f".\img\{name}.jpg", mode="wb") as f:  # 打开文件
            f.write(img_data.content)  # 写入内容
input("全部下载完成，任意键退出")
