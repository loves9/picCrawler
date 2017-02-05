# coding=utf-8

import urllib
import re

# 通过url获取网页内容
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

# 获取页面中的图片
def getImagesByHtml(html):
    reg = r'src="(.+?\.jpg)"'
    imageReg = re.compile(reg)
    imageList = re.findall(imageReg, html)
    x = 0
    for imageUrl in imageList:
        urllib.urlretrieve(imageUrl, '%s.jpg' % x)
        x+=1
    return imageList

html = getHtml("http://tieba.baidu.com/p")

print getImagesByHtml(html)
