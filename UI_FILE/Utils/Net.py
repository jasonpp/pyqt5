import  time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# option = webdriver.ChromeOptions()
# option.add_argument("headless")
# driver = webdriver.Chrome(chrome_options=option)

driver = webdriver.Chrome()

url = "https://www.365yg.com/a6684202657655030280#mid=1621620435631111"

def getRealUrl(url):
    driver.get(url)

    driver.find_element(By.CLASS_NAME, "xgplayer-start").click()

    # return driver.find_element(By.TAG_NAME,"source").get_attribute("src")
    # return driver.find_element_by_xpath('//*[@id="tt_video_69beb"]/video').get_attribute("src")



if __name__ == '__main__':
    getRealUrl(url)
    time.sleep(5)
    driver.close()


