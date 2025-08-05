"""

A datepicker :
    user interface component that allows users to select a date from a calendar pop-up or inline calendar.
    It's commonly used in forms, scheduling tools, and any application where date input is required.

How a Datepicker Works, It typically consists of:
    A text input field where the selected date appears
    A calendar pop-up that opens when the input is focused or clicked
    Optional navigation controls to change month and year

Users can:
    Click a date to select it
    Use arrows to navigate months/years
    See feedback in the input field once a date is chosen

Popular Datepicker Libraries
    Library	            Description
    jQuery UI	        Classic datepicker with wide browser support and customization options
    Air Datepicker	    Lightweight ES6-based calendar with CSS variables and keyboard navigation Air Datepicker
    React Datepicker	Reusable React component with time picker, localization, and styling options React Datepicker on npm
    MUI Datepicker	    Material UI component for React with desktop, mobile, and static variants MUI Date Picker

"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

# MM/DD/YYYY
# driver.find_element(By.XPATH,'//*[@id="datepicker"]').send_keys("05/04/2001")

year = "2020"
month = "May"
date = "4"

driver.find_element(By.XPATH,'//*[@id="datepicker"]').click() #opens datepicker

while True:
    m = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    y = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if m==month and y==year:
        break
    else:
        # driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click() #Next arrow - future dates
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click() #Previous arrow - past dates

# select date
dates = driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for d in dates:
    if d.text == date:
        d.click()
        break

time.sleep(2)
print("Testing done!")
driver.quit()