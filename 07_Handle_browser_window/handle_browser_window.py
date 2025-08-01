import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

window_id = driver.current_window_handle
print(window_id) #first time - 7D29AD81E5D4F23945420A5AE38488A5, second time - E312CC33BD1658F13D52F02413A18EFA

driver.find_element(By.LINK_TEXT, 'Click Here').click()
window_ids = driver.window_handles

# Approach 1
print(window_ids) #['9AFB208CE4BF4C15453D37D3F72C95DA', 'EB9ADF4A17FA7C98C97BC9EE9647E719']

parent_window_id  = window_ids[0]
child_window_id  = window_ids[1]
print(parent_window_id, child_window_id)

driver.switch_to.window(child_window_id)
print("title of child window: ",driver.title)

driver.switch_to.window(parent_window_id)
print("title of parent window: ",driver.title)

# Approach 2
for win_id  in window_ids:
    driver.switch_to.window(win_id)
    print(driver.title)

# Based on user choice close selected browser windows
for win_id  in window_ids:
    driver.switch_to.window(win_id)
    if driver.title=="New Window":
        driver.close()

time.sleep(3)
print("Testing done!")
driver.quit()