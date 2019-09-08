# coding:utf-8

import urllib.request
from bs4 import BeautifulSoup
import csv
from time import sleep
import re

ListId = []
finalListId = []


def getHomeURL():
    for x in range(1, 8):
        homeData = urllib.request.urlopen("http://college.gaokao.com/schlist/c7/p" + str(x))
        response = homeData.read()
        html = BeautifulSoup(response, 'html.parser')
        for i in html.select('dl dt a[href]'):
            if "http://college.gaokao.com/school/" in i['href']:
                ListId.append(i['href'])
    for url in ListId:
        if url not in finalListId:
            finalListId.append(url)
    print(finalListId)


def getDetail():
    for i in finalListId:
        # i = "http://college.gaokao.com/school/164/"
        detailDataUrl = i
        schoolDataUrl = "http://college.gaokao.com/school/tinfo/" + i[33:] + "schspe/"
        detailData = urllib.request.urlopen(detailDataUrl)
    #     detailData = urllib.request.urlopen("http://college.gaokao.com/school/2665/")
        schoolData = urllib.request.urlopen(schoolDataUrl)
        # schoolData = urllib.request.urlopen("http://college.gaokao.com/school/tinfo/2665/schspe/")
        detailDataResponse = detailData.read()
        schoolDataResponse = schoolData.read()
        html = BeautifulSoup(detailDataResponse, 'html.parser')
        soup = BeautifulSoup(schoolDataResponse, 'html.parser')
        basicData = []
        detailList = []

        [s.extract() for s in html("a")]
        [s.extract() for s in soup("dt")]
        try:
            for o in html.select('.bg_sez h2'):
                basicData.append(o.get_text().replace('\r\n', '').replace(' ', '').replace('\n', ''))
        except:
            pass

        try:
            for x in html.select('.left .basic_infor li'):
                basicData.append(x.get_text().split("：")[1])
        except:
            pass
        try:
            for z in html.select('.left .contact p'):
                basicData.extend(z.get_text().replace('\r\n\t', '').replace('\xa0', '').replace('\n', '').replace('\xa0\xa0\xa0', '').replace(chr(0x3000), "").split("："))
        except:
            pass
        try:
            for n in soup.find_all(class_='plan_con'):
                detailList.append(list(filter(None, (n.get_text().split('\n')))))
        except:
            pass
        try:
            basicData.remove('通讯地址')
        except:
            try:
                basicData.remove('学校地址')
            except:
                pass
        bachelor = []
        college = []
        try:
            for k in basicData:
                if "博士" in k:
                    basicData.remove(k)
            print(basicData)

            for m in detailList[0][1:]:
                if "专科类" in m:
                    break
                else:
                    bachelor.append(m.replace('\r', ''))
            print(bachelor)

            for x in detailList[0][1:]:
                if x not in bachelor:
                    college.append(x.replace('\r', ''))

            print(college[1:])
        except:
            pass
        try:
            all_data = [basicData[0], basicData[2], basicData[3], bachelor, college, basicData[4],
                        basicData[5],
                        basicData[6], detailDataUrl]
            with open('学校.csv', 'a+', newline='', encoding='gbk')as f:
                f_csv = csv.writer(f, dialect='excel')
                f_csv.writerow(all_data)
        except Exception as e:
            print(e)

        sleep(2)



if __name__ == '__main__':
    # csv_header = ['学校名称', '隶属于', '所在地', '本科', '专科', '通讯地址', '联系电话', '电子邮箱', '学校网址/传真/邮编', '查询网址']
    # with open('学校.csv', 'a+', newline='', encoding='gbk')as f:
    #     f_csv = csv.writer(f, dialect='excel')
    #     f_csv.writerow(csv_header)
    getHomeURL()
    getDetail()
    # a = "http://college.gaokao.com/school/23/"
    # print(a.replace('\r', ''))
