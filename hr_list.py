# coding:utf-8

import requests
import json
import csv
from time import sleep


def getData():
    for i in range(218, 265):
        url = 'http://bmfw.www.gov.cn/access/interfaces/wxTransferPort.do?callback=jQuery011283275899112044_1567923313462&requestUrl=http://10.128.0.71:8080/if/managementorg/search.do&datas=dhzkh"cPage":' + str(i) + ',"areacode":"0","name":""dhykh&heads=&_=1567923448451'
        res = requests.get(url)
        a = res.text
        b = a[39:][:-1]
        print(b)
        print('#######    ' + str(i))
        c = json.loads(b)
        for m in c['list']:
            city = m['area'].replace('\xa0', '').replace('\u200d', '')
            allName = m['groupName'].replace('\xa0', '').replace('\u200d', '')
            address = m['address'].replace('\xa0', '').replace('\u200d', '')
            tel = m['tel'].replace('\xa0', '').replace('\u200d', '')
            print([city, allName, address, tel])
            with open('人才服务机构名录.csv', 'a+', newline='', encoding='gbk')as f:
                f_csv = csv.writer(f, dialect='excel')
                f_csv.writerow([city, allName, address, tel])
            sleep(0.5)


if __name__ == '__main__':
    # csv_header = ['所在地区', '机构全称', '通信地址', '联系电话']
    # with open('人才服务机构名录.csv', 'a+', newline='', encoding='gbk')as f:
    #     f_csv = csv.writer(f, dialect='excel')
    #     f_csv.writerow(csv_header)
    getData()
    # a = 'jQuery05097498126733411_1567957812553({"commonPage":{"page_sum":264,"current_page_sum":5,"page_size":15,"page_num":37,"result_count":3958},"list":[{"iid":541,"groupName":"广宁县人才服务中心","address":"广宁县南街镇城西开区广宁县人社局","tel":"0758-8618133","area":"肇庆市","areaCode":"00617"},{"iid":542,"groupName":"怀集县人才服务中心　","address":"怀集县登云路人社局","tel":"0758-5593082","area":"肇庆市","areaCode":"00617"},{"iid":543,"groupName":"肇庆高新技术产业开发区人才服务中心","address":"肇庆高新区政德大街91号人力资源市场","tel":"0758-3638038","area":"肇庆市","areaCode":"00617"},{"iid":544,"groupName":"清远市人才智力市场","address":"清远市新城十八号区银泉路社科大厦九楼","tel":"0763-6880996","area":"清远市","areaCode":"00618"},{"iid":545,"groupName":"潮州市人才管理办公室","address":"潮州市春荣路玉兰园综合楼三楼","tel":"0768-2139885","area":"潮州市","areaCode":"00619"},{"iid":546,"groupName":"揭阳市人才交流管理局","address":"揭阳市榕城区东山建阳路中段（原劳动保障大楼）","tel":"0663-8232520","area":"揭阳市","areaCode":"00620"},{"iid":547,"groupName":"揭阳市榕城区人才管理办公室","address":"榕城区人力资源和社会保障局三楼","tel":"0663-8652491","area":"揭阳市","areaCode":"00620"},{"iid":548,"groupName":"揭阳市揭东区人才交流服务中心","address":"揭阳市揭东区人社局302室","tel":"0663-3273019","area":"揭阳市","areaCode":"00620"},{"iid":549,"groupName":"普宁市人才管理办公室","address":"普宁市流沙大道西46号党政办公大楼附属楼6楼","tel":"0663-2255717","area":"揭阳市","areaCode":"00620"},{"iid":550,"groupName":"揭阳空港经济区人才交流服务中心","address":"空港区管委办公大楼11楼","tel":"0663-8778246","area":"揭阳市","areaCode":"00620"},{"iid":551,"groupName":"揭阳市蓝城区人才交流服务中心","address":"蓝城区政务中心二楼213","tel":"0663-8252288","area":"揭阳市","areaCode":"00620"},{"iid":552,"groupName":"揭阳市揭西县人才管理办公室","address":"揭西县人力资源和社会保障局604室","tel":"0663-5593678","area":"揭阳市","areaCode":"00620"},{"iid":553,"groupName":"揭阳市惠来县人才交流服务中心","address":"惠来县东华路北人社局人才交流中心","tel":"0663-6624085","area":"揭阳市","areaCode":"00620"},{"iid":554,"groupName":"揭阳市大南山华侨管理区人才交流服务中心","address":"揭阳市惠来县大南山华侨管理区区管委大院","tel":"0663-6450206","area":"揭阳市","areaCode":"00620"},{"iid":555,"groupName":"云浮市人才工作服务局(云浮市人才智力市场)","address":"广东省云浮市云城区育华路兴隆西二巷3号人才大楼首层","tel":"0766-8921733","area":"云浮市","areaCode":"00621"}]})'
    # b = a.split('jQuery05097498126733411_1567957812553(')
    # c = b[1]
    # print(c[:-1])

