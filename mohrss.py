# coding:utf-8


import urllib.request
from bs4 import BeautifulSoup
import csv
from urllib.parse import unquote
from time import sleep


urlList = []



def getUrl():
    homeUrl = urllib.request.urlopen('http://chrm.mohrss.gov.cn/chinamap/index.html')
    response = homeUrl.read()
    html = BeautifulSoup(response, 'html.parser')
    for i in html.find_all('a', href=True):
        urlList.append(i['href'])


def getData():
    for i in urlList:
        text = unquote(i)
        city = text[39:][:-4]
        print(city)
        detailUrl = urllib.request.urlopen(i)
        response = detailUrl.read()
        html = BeautifulSoup(response, 'html.parser')
        for x in html.findAll(attrs={'style': r'height:45.0pt;border-top:none;width:232pt'}):
            print(x)
            detailList = []
            # if x.get_text().replace('\n', '').replace('\r', '') != '' or \
            #         x.get_text() != '北京市流动人员人事档案管理服务机构一览表' or x.get_text() != '机构全称' or x.get_text() != '通信地址' or x.get_text() != '联系电话':
            #     detailList.append(x.get_text().replace('\n', '').replace('\r', ''))
            # print(detailList)
            # with open('流动人员人事档案管理服务机构.csv', 'a+', newline='', encoding='gbk')as f:
            #     f_csv = csv.writer(f, dialect='excel')
            #     f_csv.writerow([city, detailList[0], detailList[1], detailList[2]])
        sleep(10)


if __name__ == '__main__':
    # csv_header = ['所在地区', '机构全称', '通信地址', '联系电话']
    # with open('流动人员人事档案管理服务机构.csv', 'a+', newline='', encoding='gbk')as f:
    #     f_csv = csv.writer(f, dialect='excel')
    #     f_csv.writerow(csv_header)
    getUrl()
    getData()