from selenium import webdriver

# 1.Initial one driver

driver = webdriver.Chrome()


#2. Setup a url which from froign university bbs

url1 = "http://shisu.myubbs.com"


#3. Define one function

def search(url):
    # 3.1 Open a browser
    driver.get(url1)

    # 3.2 Find one element and click it
    driver.find_element_by_xpath('//*[@id="category_2"]/table/tbody/tr[1]/td[1]/dl/dt/a').click()

    # 3.3 Continue click the button
    driver.find_element_by_xpath('//*[@id="stickthread_63189"]/tr/th/a[4]').click()

    # 3.4 Print all items in comments below
    reult = driver.find_elements_by_class_name('t_f')
    print(len(reult)) #Print the count of the result
    for item in reult:
        print(item.text)

if __name__ == '__main__':
    search(url1)

