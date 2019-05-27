import time

from selenium import webdriver

#1.Initial one driver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#2. Setup a url from peking forign university bbs
url1 = "http://shisu.myubbs.com"

#3.  Define a function to do sth

def search(url):

    # 3.1 open one browser
    driver.get(url=url1)

    # 3.2 Find one element and click it
    driver.find_element_by_xpath('//*[@id="category_2"]/table/tbody/tr[1]/td[1]/dl/dt/a').click()


    # 3.3 Still click the title of the news
    driver.find_element_by_xpath('//*[@id="stickthread_63189"]/tr/th/a[4]').click()

    # 3.4 Print all the lasted comments
    result = driver.find_elements_by_class_name('t_f')
    # result = driver.find_elements_by_xpath('//*[@id="postmessage_201352"]')
    print("Comments in total:",len(result))
    for item in result:
        print(item.text+"\n")

if __name__ == '__main__':
    search(url1)

