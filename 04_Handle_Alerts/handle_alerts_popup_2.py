
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://mypage.rediff.com/login/dologin")

driver.maximize_window()

driver.find_element(By.XPATH,"//input[@value='Submit']").click() #Submit button
time.sleep(4)
driver.switch_to.alert.accept() # switch to an alert window and close the alert window

time.sleep(2)
print("Testing done!")
driver.quit()
