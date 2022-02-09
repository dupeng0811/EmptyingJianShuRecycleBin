from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_argument(r'user-data-dir=C:\Users\Dupeng\AppData\Local\Google\Chrome\User Data\Default')
# driver = webdriver.Chrome(options = option)
driver = webdriver.Chrome('C:\Work\我的项目\EmptyingJianShuRecycleBin\chromedriver.exe',options=option)
driver.implicitly_wait(10)
driver.get("https://www.jianshu.com/writer#/recycle/")

sreach_windows = driver.current_window_handle
time.sleep(10)
while 1:
    driver.get("https://www.jianshu.com/writer#/recycle/")
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[3]/span[2]').click()
    time.sleep(5)

