"""

Select class--->

To interact with a dropdown menu in Selenium using Python, you use the Select class provided by selenium.webdriver.support.ui.

Key Methods in Select Class -

    Method	                    Description
    select_by_visible_text()	Selects option by the text shown to user
    select_by_value()	        Selects option by the value attribute
    select_by_index()	        Selects option by its position (0-based)

"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("E:/Jyotsna/Selenium_Learning/Selenium_Learning/05_Handle_checkbox_and_radio_buttons/Dropdown/dropdown.html")

driver.maximize_window()

country = driver.find_element(By.XPATH,"//select[@id='country']")
dropdown_country = Select(country)

dropdown_country.select_by_visible_text("France")

dropdown_country.select_by_value("UK")

dropdown_country.select_by_index(1)

# Total number of dropdowns and print it
all_options = dropdown_country.options
print("Total number of options- ",len(all_options))

for options in all_options:
    print(options.text)

# Without using built-in function select options
for options in all_options:
    if options.text=="Germany":
        options.click()
        break

total_options = driver.find_elements(By.XPATH,"//select[@id='country']/option")
print("Total number of options are - ",len(total_options))

time.sleep(2)
print("Testing done!")
driver.quit()