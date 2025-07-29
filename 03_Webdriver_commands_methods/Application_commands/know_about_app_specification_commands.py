"""
get() method in Selenium :
    your gateway to the web—it’s how you tell the browser where to go.
    What get() Does-  Loads a specified URL in the browser.
    Usage: It's typically the first command in a Selenium script to open a web page.
    Example:
        from selenium import webdriver
        driver = webdriver.Chrome()
        driver.get("https://example.com")  # Opens the website
        After calling get(), Selenium waits for the page to load before continuing.

title command:
    Purpose:
        Retrieve the title of the current web page.
    Usage:
        print(driver.title)
    Example:
        driver.get("https://www.google.com")
        print(driver.title)  # Output: Google

current_url:
    Purpose:
        Returns the URL of the current page loaded in the browser.
    Usage:
        print(driver.current_url)
    Example:
        driver.get("https://www.geeksforgeeks.org")
        print(driver.current_url)  # Output: https://www.geeksforgeeks.org/

page_source:
    Purpose:
        Returns the HTML source code of the current page as a string.
    Usage:
        html = driver.page_source
        print(html)
    Example:
        driver.get("https://example.com")
        html_code = driver.page_source
        with open("source.html", "w", encoding="utf-8") as f:
            f.write(html_code)

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


Method	            Returns	                Behavior
find_element()	    Single WebElement	    Throws exception if not found
find_elements()	    List of WebElements	    Returns empty list if none found
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)
driver1 = webdriver.Chrome(service=service_obj)
# get method
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

# title command
print("Title of web page is: ",driver.title) #OrangeHRM

# current_url command
print("URL of current web page is: ",driver.current_url) # https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

# page_source command
print(driver.page_source)

driver1.get("https://demo.nopcommerce.com/")

# find_element
element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
element.send_keys("T-shirts")

time.sleep(2)
print("Testing done!")
driver.quit()