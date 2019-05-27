import time

from selenium import webdriver

#1.Initial one driver
from selenium.webdriver.common.by import By

now = lambda:time.time()
start = now()
# 1. Setup no title option and initial one browser
option = webdriver.ChromeOptions()
option.add_argument("headless")
driver = webdriver.Chrome(options=option)


# 1.1 Click the cityname
# driver.get('https://maoyan.com/films?showType=1&offset=0')
# driver.find_element_by_class_name('city-name').click()
# driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/ul/li[2]/div/a[1]').click()


#2. Setup a url from peking forign university bbs

filmList = []
itemList = []
m = 0
for i in range(0,10):
    url = "https://maoyan.com/board/4?offset="+str(i*10)
    filmList.append(url)


#3.  Define a function to do sth


def search_3():
    # 3.1 open one browser
    for i in range(0,10):
        driver.get(filmList[i])
        #不声明global m ，那么你用m默认就是局部变量m，把你爹坑死了......................
        getItemFilmName()
        global m
        m = m + 1
    # print(now()-start)
    return itemList



def getItemFilmName():
    j = 0
    films = driver.find_elements_by_tag_name('dd')
    for item in films:
        ##app > div > div.movies-panel > div.movies-list > dl > dd:nth-child(1) > div.channel-detail.movie-item-title > a
        # resultItem = item.find_element_by_css_selector('.channel-detail movie-item-title div:nth-child(2) > a:nth-child(1)')#.movie-list > dd:nth-child(1) > div:nth-child(2)
        resultItem = item.find_element_by_css_selector('a > img.board-img').get_attribute('alt')#.movie-list > dd:nth-child(1) > div:nth-child(2)
        j = j + 1
        k = 10*m + j
        finnalResultItem = resultItem+ '--------->'+str(k)
        itemList.append(finnalResultItem)
        # print(resultItem)

if __name__ == '__main__':
    search_3()
    driver.close()
