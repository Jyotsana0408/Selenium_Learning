import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

outer_frame = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_frame)

inner_frame = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(inner_frame)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("welcome")

# driver.switch_to.parent_frame() #directly switch to parent frame(outerframe)

time.sleep(3)
print("Testing done!")
driver.quit()