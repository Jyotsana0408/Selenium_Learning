"""
In Selenium (especially with Python), conditional logic isn't built into the WebDriver itself
it's implemented using standard Python control flow.
But Selenium does provide methods that help you evaluate conditions based on the state of web elements.
Here's how you can combine them:

Common Conditional Methods in Selenium :
These methods return True or False, making them perfect for if, while, or try-except blocks.

    Method	            Purpose
    is_displayed()	    Checks if an element is visible on the page
    is_enabled()	    Checks if an element is enabled for interaction
    is_selected()	    Checks if a checkbox or radio button is selected
    get_attribute()	    Retrieves attribute values to validate conditions
    get_text()	        Gets visible text from an element for comparison
    find_elements()	    Returns a list—useful for checking if elements exist

"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/register")

driver.maximize_window()

search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")

# is_displayed()
print("Display Status: ",search_box.is_displayed()) #True
# is_enabled()
print("Enabled Status: ",search_box.is_enabled()) #True

# is_selected() - for radio buttons and checkbox
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")
rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")

print("\nDefault Radio buttons status")
print("Status of female radio button: ",rd_female.is_selected()) #False
print("Status of male radio button: ",rd_male.is_selected()) #False

rd_female.click() # Selects female radio button

print("\nAfter selecting any Radio button status")
print("Status of female radio button: ",rd_female.is_selected()) #True
print("Status of male radio button: ",rd_male.is_selected()) #False

time.sleep(2)
print("Testing done!")
driver.quit()