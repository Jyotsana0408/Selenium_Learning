"""
driver.find_element():
    Returns: The first matching element.
    Use case: When you're sure there's only one element you need.
    Raises: NoSuchElementException if no match is found.
    Example:
        from selenium.webdriver.common.by import By
        element = driver.find_element(By.ID, "login-button")

driver.find_elements():
    Returns: A list of all matching elements.
    Use case: When multiple elements share the same locator (e.g., list items, buttons).
    Returns: An empty list if no match is found (no exception).
    Example:
        from selenium.webdriver.common.by import By
        elements = driver.find_elements(By.CLASS_NAME, "menu-item")
        for el in elements:
            print(el.text)


Comparison Table: find_element() vs find_elements():

    Aspect	                    find_element()	                            find_elements()

    Purpose	                    Finds one matching element	                Finds all matching elements
    Return Type	                Returns a WebElement object	                Returns a list of WebElement objects
    If No Match Found	        Throws NoSuchElementException	            Returns an empty list
    First Match Behavior	    Returns first match only	                Returns all matches
    Use Case	                Ideal for unique elements	                Ideal for repeated elements (e.g., list items)
    Performance	                Slightly faster for single element	        Slightly slower due to list creation
    Iteration Support	        Not iterable	                            Can be iterated using loops
    Error Handling	            Requires try-except for missing elements	Can check list length to avoid errors
    Common Methods Used With	.click(), .send_keys(), .text	            .text, .get_attribute(), loop-based actions
    Test Scenarios	            Login button, search bar, submit form	    Product cards, menu items, image galleries

"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# find_element method

# 1) find_element with locator matching with single web element
element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
element.send_keys("Apple MacBook Pro 13-inch")
print("Done")

# 2) find_element with locator matching with multiple web element
element_1 = driver.find_element(By.XPATH, "//div[@class='footer']//a") #prints first link from the footer "Sitemap"
print(element_1.text)

# 3) find_element - element not available then throw NoSuchElementException
# login_element = driver.find_element(By.LINK_TEXT, "Logs in") - NoSuchElementException: Message: no such element: Unable to locate element
# login_element.click()

# find_elements method

# 1) find_elements with locator matching with single web element
element_2 = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
print(len(element_2))
element_2[0].send_keys("Apple MacBook Pro 13-inch")

# 2) find_elements with locator matching with multiple web element
element_3 = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(len(element_3))
print(element_3[0].text)
for i in element_3:
    print(i.text)

# 3) find_elements - Returns an empty list
login_element = driver.find_elements(By.LINK_TEXT, "Logs in")
print(len(login_element))
print(type(login_element))

time.sleep(2)
print("Testing done!")
driver.quit()