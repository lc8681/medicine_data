# coding:utf-8

import time
import json
import csv
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
    driver.implicitly_wait(300)
    # driver.fullscreen_window()
    driver.find_element(By.ID, "keyword").click()
    driver.find_element(By.ID, "keyword").send_keys("鄂2")
    sleep(5)
    driver.find_element(By.NAME, "Submit").click()
    sleep(5)
    driver.execute_script("window.scrollTo(0,476)")
    sleep(20)
    while True:
        for m in range(0, 15):
            final_list = []
            a = driver.find_elements_by_partial_link_text("鄂2")
            a[m].click()
            sleep(5)
            while True:
                if "images/data_fanhui.gif" in driver.find_element(By.CSS_SELECTOR, "div > img").get_attribute('src'):
                    b = driver.find_elements_by_tag_name("td")
                    for x in b[918:956]:
                        final_list.append(x.get_attribute("textContent"))
                    with open('HB.csv', 'a+', newline='', encoding='gbk')as f:
                        f_csv = csv.writer(f, dialect='excel')
                        try:
                            f_csv.writerow(
                                [final_list[1], final_list[3], final_list[5], final_list[7], final_list[9], final_list[11],
                                 final_list[13],
                                 final_list[15], final_list[17], final_list[19], final_list[21], final_list[23], final_list[25],
                                 final_list[27],
                                 final_list[29], final_list[31], final_list[33], final_list[35], final_list[37]])
                        except:
                            pass
                    print(final_list)
                    driver.find_element(By.CSS_SELECTOR, "div > img").click()
                    sleep(2)
                    break

        sleep(2)
        for p in driver.find_elements(By.CSS_SELECTOR, "td > img"):
            if "images/dataanniu_07.gif" in p.get_attribute('src'):
                p.click()
                break


if __name__ == '__main__':
    # csv_header = ['编号', '社会信用代码/组织机构代码', '分类码', '省份', '企业名称', '法定代表人', '企业负责人', '质量负责人', '注册地址', '生产地址',
    #               '生产范围', '发证日期', '有效期至', '发证机关', '签发人', '日常监管机构', '日常监管人员', '监督举报电话', '备注']
    # with open('HB.csv', 'a+', newline='', encoding='gbk')as f:
    #     f_csv = csv.writer(f, dialect='excel')
    #     f_csv.writerow(csv_header)
    test_test()