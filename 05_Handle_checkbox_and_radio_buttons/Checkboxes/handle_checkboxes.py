
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("E:/Jyotsna/Selenium_Learning/Selenium_Learning/05_Handle_checkbox_and_radio_buttons/Checkboxes/checkbox.html")

driver.maximize_window()

# 1) Select specific checkbox
driver.find_element(By.XPATH,"//input[@id='apple']").click()

#  2) Select all the checkbox
check_boxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and @name='fruit']")
print(len(check_boxes))

# Approach 1
for i in range(len(check_boxes)):
    check_boxes[i].click()

# Approach 2
for check_box in check_boxes:
    check_box.click()

# 3) Select multiple checkbox based upon user choice
for check_box in check_boxes:
    fruit_name = check_box.get_attribute('id')
    if fruit_name == 'apple' or fruit_name =='banana':
        check_box.click()

# 4) Select last 2 checkbox
for i in range(len(check_boxes)-2,len(check_boxes)):
    check_boxes[i].click()

# 5) Select first 2 checkbox
for i in range(len(check_boxes)):
    if i<2:
        check_boxes[i].click()

# 6) Unselect/clear all the checkbox
for check_box in check_boxes:
    if check_box.is_selected():
        check_box.click()


time.sleep(4)
print("Testing done!")
driver.quit()