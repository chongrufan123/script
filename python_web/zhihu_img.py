###************************************************************************
	# File Name: test3.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月05日 星期五 12时44分36秒
  # notes: 
###***********************************************************************

import urllib.request as urlreq
from bs4 import BeautifulSoup as BS
import urllib.parse
import easygui as g
import re

def get_url(url):
    head = {}
    head['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
    req = urllib.request.Request(url=url, headers=head)
    res = urlreq.urlopen(req)
    http = res.read()
    return http

def get_img(http, filepath):
    print(http)
    img = get_url(http)
    filename = http.split('/')[-1]
    filename = filepath + '//' + filename 
    filename = re.search('.*\.jpg', filename)
    filename = filename.group()
    with open(filename, 'wb') as f:
        f.write(img)

if __name__ == '__main__':
    url = input('请输入网址: ')
    http = get_url(url).decode('utf-8')
    soup = BS(http)
    figure = soup.find_all('figure')
    filepath = g.diropenbox("图片")
    for each in figure:
        url_img = each.img['src']
        get_img(url_img, filepath)
