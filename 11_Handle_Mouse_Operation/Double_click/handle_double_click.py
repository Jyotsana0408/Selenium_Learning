import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://www.w3schools.com/TAgs/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()

driver.switch_to.frame("iframeResult") #Switch to frame

field_1 = driver.find_element(By.XPATH,"//input[@id='field1']")
field_1.clear()
field_1.send_keys("welcome")

copy_button = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

act = ActionChains(driver)
act.double_click(copy_button).perform() #double action on the element

time.sleep(3)
print("Testing Done!")
driver.quit()