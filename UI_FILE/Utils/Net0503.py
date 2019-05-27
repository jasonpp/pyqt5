import time
import urllib.request

from selenium.webdriver import  ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()

preferences = {"download.default_directory":"D:\PycharmProjects\pyqt5",
               "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True}
option.add_experimental_option("prefs",preferences)
# option.add_argument('headless')
# driver = webdriver.Chrome(options=option)

driver = webdriver.Chrome(options=option)


url = "http://v.douyin.com/6BGCtx/"

driver.get(url)


driver.find_element_by_xpath('//*[@id="pageletReflowVideo"]/div/div[1]/div').click()

html = driver.find_element_by_class_name('player').get_attribute('src')

driver.get(html)

print(html)


# actions = ActionChains(driver)
#
# actions.context_click()
#
# actions.cli



# print(html)
#
# actions = ActionChains(driver)
#
# element = driver.find_element(By.TAG_NAME,'video')
#
# actions.context_click(element)
#
# actions.send_keys(Keys.CONTROL,'s')
#
# actions.send_keys(Keys.ENTER)
#
# time.sleep(15)

# driver.get(html)







# driver.find_element(By.TAG_NAME,'html').send_keys(Keys.CONTROL,'s')
# driver.find_element(By.TAG_NAME,'html').send_keys(Keys.ENTER)


# urllib.request.urlretrieve(html,'D:/'+ str(round(time.time())) + '.mp4') # Download
# urllib.request.urlretrieve(html,'D:/video.mp4') # Download
# time.sleep(5)
#
# driver.quit()




