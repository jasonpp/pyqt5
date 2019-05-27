import time

from selenium import webdriver

#1.Initial one driver
from selenium.webdriver.common.by import By

now = lambda :time.time()
start = now()
# Setup no title option and initial one browser
option = webdriver.ChromeOptions()
option.add_argument("headless")
driver = webdriver.Chrome(options=option)


#2. Setup a url from peking forign university bbs

filmList = []
itemList = []
m = 0
for i in range(0,5):
    url = "https://maoyan.com/films?showType=2&offset="+str(i*30)
    filmList.append(url)


#3.  Define a function to do sth


def search_2():
    # 3.1 open one browser
    for i in range(0,5):
        driver.get(filmList[i])
        #不声明global m ，那么你用m默认就是局部变量m，把你爹坑死了......................
        global m
        getItemFilmName()
        m = m + 1
    # print(now()-start)
    return itemList



def getItemFilmName():
    j = 0
    films = driver.find_elements_by_tag_name('dd')
    for item in films:
        #  #app > div > div.movies-panel > div.movies-list > dl > dd:nth-child(1) > div.channel-detail.movie-item-title > a
        resultItem = item.find_element_by_css_selector('div.channel-detail.movie-item-title > a')#.movie-list > dd:nth-child(1) > div:nth-child(2)
        j = j + 1
        k = 30*m + j
        finnalResultItem = resultItem.text+ '--------->'+str(k)
        itemList.append(finnalResultItem)

if __name__ == '__main__':
    search_2()
    driver.close()
