import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# This will open the Register page in the same tab
# driver.find_element(By.LINK_TEXT,"Register").click()

# This will open the Register page in different tab
registration_link = Keys.CONTROL+Keys.RETURN
driver.find_element(By.LINK_TEXT,"Register").send_keys(registration_link)

time.sleep(3)
print("Testing done!")
driver.quit()