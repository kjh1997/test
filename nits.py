from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
from bs4 import BeautifulSoup
import re
import time
import math
name = input("이름")
print(name)
chromedriverpath = "C:/Users/kjh19/OneDrive/바탕 화면/test/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriverpath)
driver.get("https://www.ntis.go.kr/ThMain.do")
main = driver.window_handles 
for handle in main: 
    if handle != main[0]: 
        driver.switch_to_window(handle) 
        driver.close()
driver.switch_to_window(driver.window_handles[0])
driver.find_element_by_class_name('mainloginbtn').click()
print(driver.window_handles)
driver.switch_to_window(driver.window_handles[1])
driver.find_element_by_name('userid').send_keys("aam411")
driver.find_element_by_name('password').send_keys("whdgns1002@")
driver.find_element_by_xpath('/html/body/div/form/input').click()
time.sleep(3)
main = driver.window_handles 
for handle in main: 
    if handle != main[0]: 
        driver.switch_to_window(handle) 
        driver.close()
driver.switch_to_window(driver.window_handles[0])

driver.find_element_by_xpath('/html/body/div[2]/nav/div/form/div[2]/button[3]').click()
driver.find_element_by_xpath('/html/body/div[2]/nav/div/form/div[2]/ul[3]/li[2]/a').click()
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/input').send_keys(name)
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/button').click()
driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/form/div[3]/div[2]/div[1]/div/a[1]').click()
driver.switch_to_window(driver.window_handles[1])
html=  driver.page_source
soup= BeautifulSoup(html,'html.parser')
a = soup.find('button',id = 'paper')
text = a.get_text()
b = text.rfind('/')
c= text.rfind('건')
num = math.ceil(int(text[b+1:c])/10)
print(num)
driver.find_element_by_xpath('/html/body/form[1]/nav/div[2]/button[2]').click()
title = []
time.sleep(2)
for i in range(num):
    time.sleep(1)
    i+=1
    i = str(i)
    js = "fn_egov_link_page('" + i + "');"
    driver.execute_script("fn_egov_link_page('" + i + "');")
    print(js)
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    pages  = soup.select('#paperInfo > li > p')   #완성본
    for num, page in enumerate(pages[:10]):
        title = page.text
        title = re.sub('&nbsp; | &nbsp;| \n|\t|\r','',title)
        print(num, "번째 title :",title)
    
    refer = soup.select('#paperInfo > li')  
    for num, ref in enumerate(refer[:10]):
        ref.p.decompose()
        refs = ref.get_text(separator='|br|', strip=True).split('|br|')
        print(num,"번째 coau",refs[0])
        print(num,"번째 refs",refs[1])
        print(type(refs))

        #----------------------노력의 결과-------------------------
    # for num, ref in enumerate(refer[:1]):
    #     print(num,"번")
    #     ref.p.decompose()
    #     refs = ref.text
    #     print("ref",ref)
    #     print(type(ref))
    #     print("ref text",ref.text[0])
    #     print("refs",refs)
    #     print(type(refs))
        # print("ref : " , refs)
#  for num, ref in enumerate(refer[:1]):
#         print(num,"번")
#         ref.p.decompose()
#         print(type(ref))
#         print(ref.text[0]
#         # print("ref : " , refs)
#/html/body/form[1]/div/div/div[2]/div[2]/dl/dd/ul/li[6]/text()[1]
#/html/body/form[1]/div/div/div[2]/div[2]/dl/dd/ul/li[6]/text()[2]
    # titles = driver.find_element_by_xpath('/html/body/form[1]/div/div/div[2]/div[2]/dl/dd/ul/li[1]/p/a[1]/span')
    # reference = driver.find_element_by_xpath('/html/body/form[1]/div/div/div[2]/div[2]/dl/dd/ul/li[1]')
    #coauthor = driver.find_element_by_xpath('/html/body/form[1]/div/div/div[2]/div[2]/dl/dd/ul/li[1]')
    #time.sleep(1)
    #print(title)
    #print(coauthor)
    #print(reference)
    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    # titles  = soup.select('#paperInfo > li:nth-child(1) > p > a:nth-child(2) > span')
    # title=[]
    # for i in titles:
    #     temp= i.replace("\t","").replace("\n","")
    #     title.append(temp)
    # print(titles)
#     for text in titles:
#         title.append(text)
#     time.sleep(2)
# print(title).

# if len(a) >= 1:
#     driver.find_element_by_xpath('/html/body/form[1]/nav/div[2]/button[2]').click()
#     text = driver.find_element_by_xpath('/html/body/form[1]/nav/div[2]/button[2]/text()')
#     b = text.rfind('/')
#     c= text.rfind('건')
#     d = text[b+1:c]
#     print(d)
# driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/button').click()
# driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/button').click()
# driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/button').click()

