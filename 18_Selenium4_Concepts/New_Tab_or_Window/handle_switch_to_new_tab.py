import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

# New Tab - Selenium4: Opens a new tab and switches to new tab
driver.get("https://opencart.com/")
driver.switch_to.new_window('tab')
driver.get("https://demo.nopcommerce.com/")

# New Browser Window - Selenium4: Opens a new window and switches to new window
driver.get("https://opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://demo.nopcommerce.com/")

time.sleep(3)
print("Testing done!")
driver.quit()