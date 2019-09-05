# coding:utf-8

import time
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


def test_test():
    driver = webdriver.Firefox()
    driver.get(
        "http://app1.sfda.gov.cn/datasearch/face3/base.jsp?tableId=34&tableName=TABLE34&title=%D2%A9%C6%B7%C9%FA%B2%FA%C6%F3%D2%B5&bcId=118103348874362715907884020353")
    sleep(5)
    driver.find_element(By.ID, "keyword").click()
    driver.find_element(By.ID, "keyword").send_keys("甘")
    driver.find_element(By.NAME, "Submit").click()
# sleep(5)
# driver.delete_all_cookies()
# sleep(1)
# driver.find_element_by_id('keyword').send_keys(Keys.RETURN)
# driver.find_element_by_name('Submit').click()

# def getId(pageNum):
#     homeData = urllib.request.urlopen("http://syj.beijing.gov.cn/eportal/ui?pageId=331136&filter_LIKE_XKZH"
#                                       "=&filter_LIKE_TITLE=&filter_EQ_FZJG=&currentPage=" + pageNum + "&pageSize=20")
#     response = homeData.read()
#     html = BeautifulSoup(response, 'html.parser')
#
#     for i in html.select('td a[href]'):
#         if "/eportal/ui?pageId=331623&exampleId=" in i['href']:
#             ListId.append(i['href'][-32:])
#     for x in ListId:
#         if x not in finalListId:
#             finalListId.append(x)
#
#
# def getDetail():
#     for i in finalListId:
#         detailList = []
#         detailData = urllib.request.urlopen(
#             "http://syj.beijing.gov.cn/eportal/ui?pageId=331623&exampleId=" + i)
#         response = detailData.read()
#         html = BeautifulSoup(response, 'html.parser')
#         for x in html.select('tbody tr td'):
#             detailList.append(x.get_text())
#         print(detailList)
#         with open('bj.csv', 'a+', newline='', encoding="gbk") as f:
#             f_csv = csv.writer(f, dialect='excel')
#             try:
#                 f_csv.writerow([detailList[0], detailList[1], detailList[2], detailList[4], detailList[5], detailList[6],
#                                 detailList[7], detailList[8], detailList[11], detailList[12], detailList[13],
#                                 detailList[14],
#                                 detailList[15],
#                                 detailList[-10], detailList[-9], detailList[-7], detailList[-5], detailList[-3],
#                                 detailList[-2],
#                                 detailList[-1]])
#             except:
#                 pass

        # sleep(1)

if __name__ == '__main__':
    test_test()
# if __name__ == '__main__':
#     csv_header = ['许可证号', '企业名称', '企业类型', '注册地址', '生产地址', '法定代表人', '企业负责人', '质量负责人', '分类码', '生产地址和范围',
#                   '发证机关', '签发人', '发证日期', '有效期至', '状态说明', 'GMP信息-证书编号', '企业名称', '地址', '认证范围',
#                   '发证机关', '发证日期', '有效期至']
#     with open('bj.csv', 'a+', newline='', encoding='gbk')as f:
#         f_csv = csv.writer(f, dialect='excel')
#         f_csv.writerow(csv_header)
#     # for i in range(1, 13):
#     #     getId(str(i))
#     #     sleep(1)
#     # print(finalListId)
#     # sleep(2)
#     getDetail()