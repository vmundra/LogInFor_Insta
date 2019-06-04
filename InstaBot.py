from selenium import webdriver

from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

name = input("pls provide ur username:")
ur_pass = input("pls provide ur password:")

driver = webdriver.Chrome()
url = "https://www.instagram.com"
driver.get(url)
time.sleep(4)

login = driver.find_element_by_link_text("Log in")
login.click()
time.sleep(2)


username = driver.find_element_by_name('username')
username.send_keys(name)

password = driver.find_element_by_name('password')
password.send_keys(ur_pass)



time.sleep(2)


loginbutton = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]')
loginbutton.click()

time.sleep(5)








