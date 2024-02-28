from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("H:\Drivers\chromedriver_win32(4)\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.close()